az aks get-credentials --resource-group helm-deploy-rg --name azure-advisor 

az aks list --resource-group helm-deploy-rg --output table

# install helm chart
helm install azure-advisor azure-advisor-helm

#install csi driver
kubectl apply -f https://raw.githubusercontent.com/kubernetes-sigs/secrets-store-csi-driver/main/deploy/rbac-secretproviderclass.yaml

