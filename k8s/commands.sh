# login azure
az login

# set subscription
az account set --subscription 24266d0b-0add-41f2-9300-251baba58df4

# download cluster credentials
az aks get-credentials --resource-group helm-deploy-rg --name azure-advisor --overwrite-existing

# list all deployments
kubectl get deployments --all-namespaces=true

# list all deployments in specific namespace
kubectl get deployments --namespace azure-advisor-namespace

#list details about specific deployment
kubectl describe deployment <deployment-name> --namespace <namespace-name>

# Get logs for all pods with specific label
kubectl logs -l <label-key>=<label-value>