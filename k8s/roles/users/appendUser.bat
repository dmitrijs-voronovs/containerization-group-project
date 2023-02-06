@REM assign the first argument to the variable username
set username=%1

@REM openssl genrsa -out $1.key 2048
@REM openssl req -new -key $1.key -out $1.csr -subj "//CN=$1//O=group1"
@REM openssl x509 -req -in $1.csr -CA ./ca.crt -CAkey ./ca.key -CAcreateserial -out $1.crt -days 500

kubectl config set-credentials %username% --client-certificate=%username%.crt --client-key=%username%.key
kubectl config set-context %username%-context --cluster=minikube --user=%username%
kubectl config view