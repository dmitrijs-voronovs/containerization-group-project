set username=%1

kubectl config set-credentials %username% --client-certificate=%username%.crt --client-key=%username%.key
kubectl config set-context %username%-context --cluster=minikube --user=%username%
kubectl config view