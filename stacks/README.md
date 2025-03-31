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

