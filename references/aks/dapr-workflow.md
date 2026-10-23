# Deploy Workflows with the Dapr Extension for AKS

> Source: https://learn.microsoft.com/en-us/azure/aks/dapr-workflow  
> Microsoft doc last updated: 02/06/2026


With Dapr Workflow, you can easily orchestrate messaging, state management, and failure-handling logic across various microservices. Dapr Workflow can help you create long-running, fault-tolerant, and stateful applications.  

In this guide, you use the [provided order processing workflow example][dapr-workflow-sample] to:

> - Create an Azure Container Registry and an AKS cluster for this sample.
> - Install the Dapr extension on your AKS cluster.
> - Deploy the sample application to AKS. 
> - Start and query workflow instances using HTTP API calls.

The workflow example is an ASP.NET Core project with:
- A [`Program.cs` file][dapr-program] that contains the setup of the app, including the registration of the workflow and workflow activities.
- Workflow definitions found in the [`Workflows` directory][dapr-workflow-dir].
- Workflow activity definitions found in the [`Activities` directory][dapr-activities-dir].

## Prerequisites

- An [Azure subscription](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn) with Owner or Admin role
- [An Azure Kubernetes Service Role-Based Access Control Admin role](https://learn.microsoft.com/en-us/azure/role-based-access-control/built-in-roles#azure-kubernetes-service-rbac-admin) 
- The latest version of the [Azure CLI][install-cli]
- The latest version of [Dapr][dapr]
- Latest [Docker][docker]
- Latest [Helm][helm]

## Set up the environment

### Clone the sample project

Clone the example workflow application. 

```bash
git clone https://github.com/Azure-Samples/dapr-workflows-aks-sample.git
```

Navigate to the sample's root directory.

```bash
cd dapr-workflows-aks-sample
```

### Create a Kubernetes cluster

Create a resource group to hold the AKS cluster.

```bash
az group create --name <your-resource-group> --location eastus
```

Create an AKS cluster.

```bash
az aks create --resource-group <your-resource-group> --name <your-AKS-cluster> --node-count 2 --generate-ssh-keys 
```

[Make sure `kubectl` is installed and pointed to your AKS cluster.][kubectl] If you use the Azure Cloud Shell, `kubectl` is already installed. 

For more information, see the [Deploy an AKS cluster][cluster] tutorial.

## Deploy the application to AKS

### Install Dapr on your AKS cluster

Install the Dapr extension on your AKS cluster. Before you start, make sure you:
- [Install or update the `k8s-extension`][k8s-ext]
- [Register the `Microsoft.KubernetesConfiguration` service provider][k8s-sp]

```bash
az k8s-extension create --cluster-type managedClusters --cluster-name myAKSCluster --resource-group <your-resource-group> --name dapr --extension-type Microsoft.Dapr
```

After a few minutes, the output shows the Dapr connection to your AKS cluster. Next, initialize Dapr on your cluster.

```bash
dapr init -k
```

Verify that Dapr is installed:

```bash
kubectl get pods -A
```

### Deploy the Redis actor state store component

Navigate to the `Deploy` directory in your forked version of the sample:

```bash
cd Deploy
```

Deploy the Redis component:

```bash
helm repo add bitnami https://charts.bitnami.com/bitnami
helm install redis bitnami/redis
kubectl apply -f redis.yaml
```

### Run the application

Once Redis is deployed, deploy the application to AKS:

```bash
kubectl apply -f deployment.yaml
```

Expose the Dapr sidecar and the sample app:

```bash
kubectl apply -f service.yaml
export APP_URL=$(kubectl get svc/workflows-sample -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
export DAPR_URL=$(kubectl get svc/workflows-sample-dapr -o jsonpath='{.status.loadBalancer.ingress[0].ip}')
```

Verify that the above commands were exported:

```bash
echo $APP_URL
echo $DAPR_URL
```

## Start the workflow

Now that the application and Dapr are deployed to the AKS cluster, you can now start and query workflow instances. Restock items in the inventory using the following API call to the sample app:

```bash
curl -X GET $APP_URL/stock/restock
```

Start the workflow:

```bash
curl -i -X POST $DAPR_URL/v1.0/workflows/dapr/OrderProcessingWorkflow/start \
  -H "Content-Type: application/json" \
  -H "dapr-app-id: dwf-app" \
  -d '{"Name": "Paperclips", "TotalCost": 99.95, "Quantity": 1}'
```

Expected output includes an auto-generated instance ID:

```
HTTP/1.1 202 Accepted
Content-Type: application/json
Traceparent: 00-00000000000000000000000000000000-0000000000000000-00
Date: Tue, 23 Apr 2024 15:35:00 GMT
Content-Length: 21

 {"instanceID":"<generated-id>"}
```

Check the workflow status:

```bash
curl -i -X GET $DAPR_URL/v1.0/workflows/dapr/OrderProcessingWorkflow/<instance-id> \
  -H "dapr-app-id: dwf-app"
```

Expected output:

```json
HTTP/1.1 200 OK
Content-Type: application/json
Traceparent: 00-00000000000000000000000000000000-0000000000000000-00
Date: Tue, 23 Apr 2024 15:51:02 GMT
Content-Length: 580
```

Monitor the application logs:

```bash
kubectl logs -l run=workflows-sample -c workflows-sample --tail=20
```

Expected output:

```
{
  "instanceID":"1234",
  "workflowName":"OrderProcessingWorkflow",
  "createdAt":"2024-04-23T15:35:00.156714334Z",
  "lastUpdatedAt":"2024-04-23T15:35:00.176459055Z",
  "runtimeStatus":"COMPLETED",
  "dapr.workflow.input":"{ \"input\" : {\"Name\": \"Paperclips\", \"TotalCost\": 99.95, \"Quantity\": 1}}",
  "dapr.workflow.output":"{\"Processed\":true}"
}
```

Notice that the workflow status is marked as completed.

## Next step

> [Configure the Dapr extension on your AKS cluster][dapr-config]

[deploy-cluster]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
[install-cli]: https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
[k8s-ext]: https://learn.microsoft.com/en-us/azure/aks/dapr#add-the-azure-cli-extension-for-cluster-extensions
[cluster]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster
[k8s-sp]: https://learn.microsoft.com/en-us/azure/aks/dapr#register-the-kubernetesconfiguration-resource-provider
[dapr-config]: https://learn.microsoft.com/en-us/azure/aks/dapr-settings
[dapr-migration]: https://learn.microsoft.com/en-us/azure/aks/dapr-migration
[kubectl]: https://learn.microsoft.com/en-us/azure/aks/tutorial-kubernetes-deploy-cluster#connect-to-cluster-using-kubectl

[dapr-program]: https://github.com/Azure-Samples/dapr-workflows-aks-sample/blob/main/Program.cs
[dapr-workflow-sample]: https://github.com/Azure-Samples/dapr-workflows-aks-sample
[dapr-workflow-dir]: https://github.com/Azure-Samples/dapr-workflows-aks-sample/blob/main/Workflows/OrderProcessingWorkflow.cs
[dapr-activities-dir]: https://github.com/Azure-Samples/dapr-workflows-aks-sample/tree/main/Activities
[deployment-yaml]: https://github.com/Azure/dapr-workflows-aks-sample/blob/main/Deploy/deployment.yaml
[docker]: https://docs.docker.com/get-docker/
[helm]: https://helm.sh/docs/intro/install/
[dapr]: https://docs.dapr.io/getting-started/install-dapr-cli/
