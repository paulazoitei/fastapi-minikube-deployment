#  Randomizer API

A lightweight **FastAPI** application that generates random values and manages items.  
Built with a clean architecture using routers, services, schemas, and configurable logging.

---

##  Features

###  Random Playground
- Generate a random number between **1 and `<max>`**
- Generate a random number **between `<min>` and `<max>`**
- Simple homepage endpoint

###  Item Management
- Add new items  
- View items + randomized order  
- Update an existing item  
- Delete an item  
- Uses **in-memory storage** (for demo purposes)

###  Logging
- Logging level is configurable using the `LOG_LEVEL` environment variable  
- Supports: `DEBUG`, `INFO`, `WARNING`, `ERROR`  
- Uses Python’s built-in `logging` module  
- Logging setup stored in `app/logging/`

---

##  Project Structure

```
app/
├─ main.py — FastAPI application entrypoint
├─ routers/ — API route definitions
├─ services/ — Business logic (ItemService, RandomService)
├─ schemas/ — Pydantic models
└─ logging/ — Logging setup
```

---

##  Running with Docker

### Build the Docker image
```bash
docker build -t paulazoitei/fastapi-minikube-deployment:1.0 .
```

### Run the container
```bash
docker run -p 8000:8000 paulazoitei/fastapi-minikube-deployment:1.0
```

Then open:

 http://localhost:8080/docs  
(Interactive Swagger UI)

---

##  Local Development

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run with FastAPI dev server
```bash
fastapi dev app/main.py
```


```

---

##  Logging Configuration

Control how much information your app logs:

```bash
export LOG_LEVEL=DEBUG
```


Default logging level: **DEBUG**

---

##  API Endpoints (Overview)

### Random

| Method | Path              | Description                   |
|--------|-------------------|-------------------------------|
| GET    | /                 | Welcome message               |
| GET    | /random/{max}     | Random number up to max       |
| GET    | /random/between   | Random number between values  |

### Items

| Method | Path            | Description               |
|--------|-----------------|---------------------------|
| POST   | /items/         | Add a new item            |
| GET    | /items/         | List items + random order |
| PUT    | /items/{name}   | Update an item            |
| DELETE | /items/{name}   | Delete an item            |

---

##  Dependencies

- FastAPI  
- Uvicorn  
- Pydantic  
- Python logging

---

##  API Documentation

Interactive documentation:

- Swagger UI → `/docs`  
- ReDoc → `/redoc`  

##  Minikube Installation Summary (Using `--driver=none`)

This section summarizes the essential commands used to install **kubectl**, **minikube**, and all required dependencies to run Minikube with the `--driver=none` driver.

The **`none` driver** runs Kubernetes components **directly on the host machine**, without a VM or Docker driver.  
This means:

- No Docker Desktop or VM needed  
- Kubernetes services run as system processes (kubelet, api-server, etc.)  
- Requires root privileges (`sudo`)  
- Needs additional dependencies: `conntrack`, `crictl`, `containerd`, and CNI plugins  

---

## 1 Install kubectl

## 2 Install Minikube


## 3 Install Required Dependencies for `--driver=none`

The none driver **requires additional system tools** because Kubernetes runs without a VM:


### Install conntrack
Required by kubelet networking.

```bash
sudo apt-get install conntrack -y
```

### Install crictl (CRI tool)
Minikube needs a CRI runtime tool when not using Docker driver.

```bash
curl -LO https://github.com/kubernetes-sigs/cri-tools/releases/download/v1.31.1/crictl-v1.31.1-linux-amd64.tar.gz
sudo tar zxvf crictl-v1.31.1-linux-amd64.tar.gz -C /usr/local/bin
crictl --version
```

### Install containerd (runtime for Kubernetes)
```bash
sudo apt install -y containerd
containerd --version
```

Configure containerd:

```bash
sudo mkdir -p /etc/containerd
containerd config default | sudo tee /etc/containerd/config.toml
sudo systemctl restart containerd
```

### Install CNI Plugins
Networking plugins required by Kubernetes.

```bash
CNI_PLUGIN_VERSION="v1.8.0"
CNI_PLUGIN_TAR="cni-plugins-linux-amd64-$CNI_PLUGIN_VERSION.tgz"
CNI_PLUGIN_INSTALL_DIR="/opt/cni/bin"

curl -LO "https://github.com/containernetworking/plugins/releases/download/$CNI_PLUGIN_VERSION/$CNI_PLUGIN_TAR"
sudo mkdir -p "$CNI_PLUGIN_INSTALL_DIR"
sudo tar -xf "$CNI_PLUGIN_TAR" -C "$CNI_PLUGIN_INSTALL_DIR"
rm "$CNI_PLUGIN_TAR"
```

---

## 4 Start Minikube with `--driver=none`

After dependencies are installed:

```bash
sudo minikube start --driver=none --container-runtime=containerd
```



##  Kubernetes Deployment (Minikube)

This project can be deployed to Kubernetes using a Deployment, Service, ConfigMap, and Ingress.

---

### 1 Deployment & Service

Apply:

```bash
kubectl apply -f k8s/fastapi.yaml
```



### 2 ConfigMap (logging level)

Apply:

```bash
kubectl apply -f k8s/fastapi-configmap.yaml
```

---

### 3 Ingress (Expose as fastapi.local)

Enable ingress:

```bash
minikube addons enable ingress
```

Apply ingress:

```bash
kubectl apply -f k8s/fastapi-ingress.yaml
```



---

### 4 Accessing the App

Add Minikube IP to hosts file:

```bash
sudo nano /etc/hosts
```

Add:

```txt
<minikube-ip>   fastapi.local
```

Then open:

 http://fastapi.local/docs

---

###  Useful Commands

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl describe pod fastapi-deployment-<version>
```










