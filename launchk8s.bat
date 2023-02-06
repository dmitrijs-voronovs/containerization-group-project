@REM # kubectl apply -f k8s

cd k8s

kubectl apply -f db-pv.yaml
kubectl apply -f db-pvc.yaml
kubectl apply -f db-config.yaml
kubectl apply -f db-secret.yaml
kubectl apply -f db.yaml
kubectl apply -f db-service.yaml
kubectl apply -f ui.yaml
kubectl apply -f ui-service.yaml
kubectl apply -f ingress.yaml
timeout 10
kubectl apply -f api.yaml
kubectl apply -f api-service.yaml