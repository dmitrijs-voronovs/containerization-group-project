# Container-Group31

1. backend frontend db
2. https
3. secure k8s related features

## Run locally

1. create a backend image

```sh
cd backend
docker build -t backend:v1 .
```

2. create a frontend image

```sh
cd frontend
docker build -t frontend:v2 .
```

3. run `docker-compose up`

```sh
cd app-yaml
docker-compose up -d
```
