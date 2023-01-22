# Container-Group31

1. backend frontend db
2. https
3. secure k8s related features

## Run locally

1. create a backend image
2.

```sh
cd backend
docker build -t backend:v1 .
```

1. create a frontend image
2.

```sh
cd frontend
docker build -t frontend:v2 .
```

1. run `docker-compose up`

```sh
cd app-yaml
docker-compose up -d
```
