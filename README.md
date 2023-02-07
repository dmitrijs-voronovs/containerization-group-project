# VU Containerization course

Author: Dmitrijs Voronovs
Group: 31 (1 member)

## Diagram

K8s setup:
<img width="875" alt="image" src="https://user-images.githubusercontent.com/53301511/217375216-1e0952a3-eb6c-4ae8-85bb-a4d120ca83f5.png">

## Context

For demonstration purposes I am using **minikube**. As I have tried **microk8s** and **GKE**, I have to make sure that my kubernetes CLI is in the right context:

```shell
kubectl config get-contexts
kubectl config use-context minikube
```

## Commands

### Docker-compose: Run project locally, build, push

As I have configured docker-compose, I can use it to run, build and push containers conveniently
build images:

```shell
docker-compose up
docker-compose build
docker-compose push
```

### Kubernetes-minikube: start, stop

```shell
kubectl apply -f k8s/
kubectl apply -f k8s/cert
kubectl apply -f k8s/network-policies
```

In order to apply roles, they should be generated beforehand

```shell
kubectl apply -f k8s/roles
```

### Helm chart

```shell
cd helm
helm install my-todo-app ./todo-app
helm list
```

Edit values file > change **deployment > ui > tag** to **v2-canary**

```shell
helm upgrade my-todo-app
helm uninstall my-todo-app
```

### Google Cloud Platform

```shell
kubectl config get-contexts
kubectl config use-context gke_todo-app-containerization_europe-central2-c_cluster-1
# run all kubernetes objects
kubectl apply -f k8s/
kubectl apply -f k8s/cert
kubectl apply -f k8s/roles
kubectl apply -f k8s/network-policies
# override with gke-specific objects
kubectl apply -f k8s/gke
```
