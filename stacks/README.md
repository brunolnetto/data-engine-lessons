# 🧠 Data Lifecycle + Open-Source Tools (Medallion Architecture)

This table organizes the stages of the data lifecycle with open-source tools for each step, inspired by the *Medallion Architecture* pattern.

| 🧩 **Stage** | 🎯 **Objective** | 🛠️ **Possible Tools (OSS)** |
|-------------|------------------|------------------------------|
| **1. Data Ingestion (Raw)** | Collect and extract data from diverse sources | [Airbyte](https://airbyte.io), [Apache Nifi](https://nifi.apache.org/), [Meltano](https://meltano.com), [Kafka Connect](https://kafka.apache.org/) |
| **2. Storage (Data Lake)** | Store raw data in a cost-effective way | [MinIO](https://min.io), [Ceph](https://ceph.io), [HDFS](https://hadoop.apache.org/), [LakeFS](https://lakefs.io) |
| **3. Batch/Stream Processing** | Clean, parse, enrich and transform data | [Apache Spark](https://spark.apache.org/), [Flink](https://flink.apache.org/), [Pandas](https://pandas.pydata.org/), [Beam](https://beam.apache.org/) |
| **4. Lakehouse / Table Format** | Ensure consistency, versioning, ACID guarantees | [Delta Lake](https://delta.io), [Apache Iceberg](https://iceberg.apache.org/), [Apache Hudi](https://hudi.apache.org/) |
| **5. Modeling & Transformations (Silver/Gold)** | Business logic, metric definitions, domain rules | [dbt](https://www.getdbt.com/), [Dagster](https://dagster.io/), [SQLMesh](https://sqlmesh.com/) |
| **6. Orchestration & Scheduling** | Automate pipelines, monitor failures and dependencies | [Apache Airflow](https://airflow.apache.org/), [Prefect](https://www.prefect.io/), [Dagster](https://dagster.io) |
| **7. Data Quality & Observability** | Ensure data integrity, consistency, and reliability | [Great Expectations](https://greatexpectations.io/), [Soda](https://soda.io/), [Monte Carlo (OSS)](https://github.com/monte-carlo-data) |
| **8. Governance & Metadata** | Cataloging, lineage, classification, access control | [OpenMetadata](https://open-metadata.org), [Amundsen](https://www.amundsen.io/), [DataHub](https://datahubproject.io/) |
| **9. Data Access / Virtualization** | Expose data via SQL/REST, federate multiple sources | [Dremio](https://www.dremio.com/), [Trino](https://trino.io/), [Apache Drill](https://drill.apache.org/) |
| **10. Consumption / Visualization** | Dashboards, reporting, ad-hoc exploration | [Metabase](https://www.metabase.com/), [Apache Superset](https://superset.apache.org/), [Redash](https://redash.io/) |
| **11. Data Science & Experimentation** | Data exploration, model prototyping | [JupyterHub](https://jupyter.org/hub), [VSCode + Remote Dev](https://code.visualstudio.com/), [Polynote](https://polynote.org/) |
| **12. ML Lifecycle (Optional)** | Training, experiment tracking, and model deployment | [MLflow](https://mlflow.org/), [DVC](https://dvc.org/), [Kubeflow](https://www.kubeflow.org/), [ZenML](https://zenml.io/) |
| **13. Monitoring & Logging** | Observability, metrics, logs, traces | [Prometheus](https://prometheus.io), [Grafana](https://grafana.com), [Loki](https://grafana.com/oss/loki/), [OpenTelemetry](https://opentelemetry.io) |


---

## 🪄 Observações:

- 🥉 **Bronze Layer**: Estágios 1–3 (raw e staging).
- 🥈 **Silver Layer**: Estágio 4–5 (dados limpos e estruturados).
- 🥇 **Gold Layer**: Estágio 6 em diante (modelo de negócio, consumo, monitoramento).
- Ferramentas como **Spark, dbt e Airflow** podem ser utilizadas em múltiplas camadas, dependendo da arquitetura.



# Installation Requirements for Hosting Docker Compose and Kubernetes Stacks

## Prerequisites
Ensure your system meets the following requirements:

- **Operating System:** Linux (Ubuntu, Debian, CentOS) or Windows with WSL2
- **CPU & RAM:** At least 4 CPU cores and 8GB RAM (recommended for Kubernetes)
- **Disk Space:** At least 20GB free space

---

## Installing Dependencies

### **1️⃣ Install Docker & Docker Compose**

#### **Linux (Ubuntu/Debian-based)**
```bash
# Install dependencies
sudo apt update && sudo apt install -y ca-certificates curl gnupg

# Add Docker’s official GPG key
sudo install -m 0755 -d /etc/apt/keyrings
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo tee /etc/apt/keyrings/docker.gpg > /dev/null
sudo chmod a+r /etc/apt/keyrings/docker.gpg

# Add Docker repository
echo \  
  "deb [arch=$(dpkg --print-architecture) signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu \  
  $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

# Install Docker
sudo apt update && sudo apt install -y docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin

# Verify installation
docker --version
```

#### **Windows (WSL2)**
- Install **Docker Desktop** from [here](https://www.docker.com/products/docker-desktop/)
- Enable WSL2 support in Docker settings
- Run `docker --version` to verify installation

#### **Check Docker Compose version**
```bash
docker compose version
```

---

### **2️⃣ Install Minikube for Kubernetes**

#### **Linux (Ubuntu/Debian-based)**
```bash
# Download Minikube binary
curl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64

# Make it executable
chmod +x minikube-linux-amd64

# Move to system path
sudo mv minikube-linux-amd64 /usr/local/bin/minikube

# Verify installation
minikube version
```

#### **Windows (WSL2)**
```powershell
# Install Minikube using Chocolatey
choco install minikube

# Verify installation
minikube version
```

---

### **3️⃣ Install kubectl (Kubernetes CLI)**

#### **Linux (Ubuntu/Debian-based)**
```bash
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
chmod +x kubectl
sudo mv kubectl /usr/local/bin/
kubectl version --client
```

#### **Windows (WSL2)**
```powershell
# Install kubectl using Chocolatey
choco install kubernetes-cli

# Verify installation
kubectl version --client
```

---

### **4️⃣ Install Helm (Kubernetes Package Manager)**

#### **Linux (Ubuntu/Debian-based)**
```bash
curl https://raw.githubusercontent.com/helm/helm/main/scripts/get-helm-3 | bash
helm version
```

#### **Windows (WSL2)**
```powershell
# Install Helm using Chocolatey
choco install kubernetes-helm

# Verify installation
helm version
```

---

## **Running Docker Compose Stack**
Navigate to the directory containing your `docker-compose.yml` file and run:
```bash
docker compose up -d
```
To stop the stack:
```bash
docker compose down
```

---

## **Running Kubernetes Stack with Helm**
### **1️⃣ Start Minikube**
```bash
minikube start
```

### **2️⃣ Deploy Helm Chart**
Navigate to the directory with your Helm chart and run:
```bash
helm install my-stack ./helm-chart/
```
To list running Helm deployments:
```bash
helm list
```
To delete the deployment:
```bash
helm uninstall my-stack
```

---

## **Troubleshooting**

- **Docker daemon not running?** Start it with:
  ```bash
  sudo systemctl start docker
  ```
- **Minikube fails to start?** Try running with:
  ```bash
  minikube delete && minikube start --driver=none
  ```
- **Helm install fails?** Check logs with:
  ```bash
  kubectl get pods
  kubectl logs <pod-name>
  ```

---

## Conclusion
With these steps, you are now able to deploy applications using both **Docker Compose** and **Kubernetes with Helm**. 🎉 If you run into issues, check the official documentation for [Docker](https://docs.docker.com/), [Kubernetes](https://kubernetes.io/docs/), and [Helm](https://helm.sh/docs/). Happy coding! 🚀

