import requests
import yaml
import time
import os

from testcontainers.k3s import K3SContainer
from testcontainers.postgres import PostgresContainer
from kubernetes import client, config

def get_service_url(k3s, config_dict, service_name, namespace="default", port=8080):
    config.load_kube_config_from_dict(config_dict)
    v1 = client.CoreV1Api()
    service = v1.read_namespaced_service(service_name, namespace)

    if service.spec.type == "NodePort":
        node_port = service.spec.ports[0].node_port
        cluster_ip = k3s.get_container_host_ip()
        return f"http://{cluster_ip}:{node_port}"

    elif service.spec.type == "LoadBalancer" and service.status.load_balancer.ingress:
        external_ip = service.status.load_balancer.ingress[0].ip
        return f"http://{external_ip}:{port}"

    return None

def wait_for_pod_ready(kubeconfig_dict, namespace="default", timeout=180):
    """
    Wait for all pods in the namespace to be fully ready.
    """
    config.load_kube_config_from_dict(kubeconfig_dict)
    v1 = client.CoreV1Api()

    end_time = time.time() + timeout
    while time.time() < end_time:
        pods = v1.list_namespaced_pod(namespace=namespace)
        all_ready = True

        for pod in pods.items:
            if pod.status.phase != "Running":
                all_ready = False
                break

            for container in pod.status.container_statuses or []:
                if not container.ready:
                    all_ready = False
                    break

        if all_ready:
            return True

        time.sleep(5)

    raise TimeoutError("Timeout waiting for pods to be ready")


def test_kubernetes_app():
    import sqlalchemy
    
    # Spin up PostgreSQL Container
    with PostgresContainer("postgres:15.0") as postgres:
        postgres_host = postgres.get_container_host_ip()
        postgres_port = postgres.get_exposed_port(5432)

        engine = sqlalchemy.create_engine(postgres.get_connection_url())
        with engine.begin() as connection:
            result = connection.execute(sqlalchemy.text("select version()"))
            version, = result.fetchone()

            assert version.startswith("PostgreSQL 15.0"), "PostgreSQL version mismatch"