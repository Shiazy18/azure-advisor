#Enable workload identity on AKS
az aks update \
  --name azure-advisor \
  --resource-group helm-deploy-rg \
  --enable-workload-identity \
  --enable-oidc-issuer

#output
# {
#   "aadProfile": null,
#   "addonProfiles": {
#     "azureKeyvaultSecretsProvider": {
#       "config": null,
#       "enabled": false,
#       "identity": null
#     },
#     "azurepolicy": {
#       "config": null,
#       "enabled": false,
#       "identity": null
#     }
#   },
#   "agentPoolProfiles": [
#     {
#       "availabilityZones": null,
#       "capacityReservationGroupId": null,
#       "count": 2,
#       "creationData": null,
#       "currentOrchestratorVersion": "1.33.5",
#       "eTag": null,
#       "enableAutoScaling": true,
#       "enableEncryptionAtHost": null,
#       "enableFips": false,
#       "enableNodePublicIp": false,
#       "enableUltraSsd": null,
#       "gatewayProfile": null,
#       "gpuInstanceProfile": null,
#       "gpuProfile": null,
#       "hostGroupId": null,
#       "kubeletConfig": null,
#       "kubeletDiskType": "OS",
#       "linuxOsConfig": null,
#       "maxCount": 5,
#       "maxPods": 110,
#       "messageOfTheDay": null,
#       "minCount": 2,
#       "mode": "System",
#       "name": "agentpool",
#       "networkProfile": null,
#       "nodeImageVersion": "AKSUbuntu-2204gen2containerd-202601.07.0",
#       "nodeLabels": null,
#       "nodePublicIpPrefixId": null,
#       "nodeTaints": null,
#       "orchestratorVersion": "1.33.5",
#       "osDiskSizeGb": 150,
#       "osDiskType": "Ephemeral",
#       "osSku": "Ubuntu",
#       "osType": "Linux",
#       "podIpAllocationMode": null,
#       "podSubnetId": null,
#       "powerState": {
#         "code": "Running"
#       },
#       "provisioningState": "Succeeded",
#       "proximityPlacementGroupId": null,
#       "scaleDownMode": "Delete",
#       "scaleSetEvictionPolicy": null,
#       "scaleSetPriority": null,
#       "securityProfile": {
#         "enableSecureBoot": false,
#         "enableVtpm": false
#       },
#       "spotMaxPrice": null,
#       "status": null,
#       "tags": null,
#       "type": "VirtualMachineScaleSets",
#       "upgradeSettings": {
#         "drainTimeoutInMinutes": null,
#         "maxSurge": "10%",
#         "maxUnavailable": "0",
#         "nodeSoakDurationInMinutes": null,
#         "undrainableNodeBehavior": null
#       },
#       "virtualMachineNodesStatus": null,
#       "virtualMachinesProfile": null,
#       "vmSize": "Standard_D4ds_v5",
#       "vnetSubnetId": null,
#       "windowsProfile": null,
#       "workloadRuntime": null
#     }
#   ],
#   "aiToolchainOperatorProfile": null,
#   "apiServerAccessProfile": null,
#   "autoScalerProfile": {
#     "balanceSimilarNodeGroups": "false",
#     "daemonsetEvictionForEmptyNodes": false,
#     "daemonsetEvictionForOccupiedNodes": true,
#     "expander": "random",
#     "ignoreDaemonsetsUtilization": false,
#     "maxEmptyBulkDelete": "10",
#     "maxGracefulTerminationSec": "600",
#     "maxNodeProvisionTime": "15m",
#     "maxTotalUnreadyPercentage": "45",
#     "newPodScaleUpDelay": "0s",
#     "okTotalUnreadyCount": "3",
#     "scaleDownDelayAfterAdd": "10m",
#     "scaleDownDelayAfterDelete": "10s",
#     "scaleDownDelayAfterFailure": "3m",
#     "scaleDownUnneededTime": "10m",
#     "scaleDownUnreadyTime": "20m",
#     "scaleDownUtilizationThreshold": "0.5",
#     "scanInterval": "10s",
#     "skipNodesWithLocalStorage": "false",
#     "skipNodesWithSystemPods": "true"
#   },
#   "autoUpgradeProfile": {
#     "nodeOsUpgradeChannel": "NodeImage",
#     "upgradeChannel": "patch"
#   },
#   "azureMonitorProfile": {
#     "metrics": {
#       "enabled": true,
#       "kubeStateMetrics": {
#         "metricAnnotationsAllowList": "",
#         "metricLabelsAllowlist": ""
#       }
#     }
#   },
#   "azurePortalFqdn": "azure-advisor-dns-s89xs96o.portal.hcp.centralindia.azmk8s.io",
#   "bootstrapProfile": {
#     "artifactSource": "Direct",
#     "containerRegistryId": null
#   },
#   "currentKubernetesVersion": "1.33.5",
#   "disableLocalAccounts": false,
#   "diskEncryptionSetId": null,
#   "dnsPrefix": "azure-advisor-dns",
#   "eTag": null,
#   "enableRbac": true,
#   "extendedLocation": null,
#   "fqdn": "azure-advisor-dns-s89xs96o.hcp.centralindia.azmk8s.io",
#   "fqdnSubdomain": null,
#   "httpProxyConfig": null,
#   "id": "/subscriptions/24266d0b-0add-41f2-9300-251baba58df4/resourcegroups/helm-deploy-rg/providers/Microsoft.ContainerService/managedClusters/azure-advisor",
#   "identity": {
#     "delegatedResources": null,
#     "principalId": "d28ad0d9-0517-4d8f-83a2-4b71c69019a4",
#     "tenantId": "189de737-c93a-4f5a-8b68-6f4ca9941912",
#     "type": "SystemAssigned",
#     "userAssignedIdentities": null
#   },
#   "identityProfile": {
#     "kubeletidentity": {
#       "clientId": "22d521ef-9fa4-4cd2-97a3-727c12417c3f",
#       "objectId": "d09916fa-e181-4ac7-8714-a57ad45e0dbd",
#       "resourceId": "/subscriptions/24266d0b-0add-41f2-9300-251baba58df4/resourcegroups/MC_helm-deploy-rg_azure-advisor_centralindia/providers/Microsoft.ManagedIdentity/userAssignedIdentities/azure-advisor-agentpool"
#     }
#   },
#   "ingressProfile": null,
#   "kubernetesVersion": "1.33.5",
#   "linuxProfile": null,
#   "location": "centralindia",
#   "maxAgentPools": 100,
#   "metricsProfile": {
#     "costAnalysis": {
#       "enabled": false
#     }
#   },
#   "name": "azure-advisor",
#   "networkProfile": {
#     "advancedNetworking": null,
#     "dnsServiceIp": "10.0.0.10",
#     "ipFamilies": [
#       "IPv4"
#     ],
#     "loadBalancerProfile": {
#       "allocatedOutboundPorts": null,
#       "backendPoolType": "nodeIPConfiguration",
#       "effectiveOutboundIPs": [
#         {
#           "id": "/subscriptions/24266d0b-0add-41f2-9300-251baba58df4/resourceGroups/MC_helm-deploy-rg_azure-advisor_centralindia/providers/Microsoft.Network/publicIPAddresses/bfa752ea-9942-43d4-99de-a1d45a14d8c3",
#           "resourceGroup": "MC_helm-deploy-rg_azure-advisor_centralindia"
#         }
#       ],
#       "enableMultipleStandardLoadBalancers": null,
#       "idleTimeoutInMinutes": null,
#       "managedOutboundIPs": {
#         "count": 1,
#         "countIpv6": null
#       },
#       "outboundIPs": null,
#       "outboundIpPrefixes": null
#     },
#     "loadBalancerSku": "standard",
#     "natGatewayProfile": null,
#     "networkDataplane": "azure",
#     "networkMode": null,
#     "networkPlugin": "azure",
#     "networkPluginMode": "overlay",
#     "networkPolicy": "none",
#     "outboundType": "loadBalancer",
#     "podCidr": "10.244.0.0/16",
#     "podCidrs": [
#       "10.244.0.0/16"
#     ],
#     "serviceCidr": "10.0.0.0/16",
#     "serviceCidrs": [
#       "10.0.0.0/16"
#     ],
#     "staticEgressGatewayProfile": null
#   },
#   "nodeProvisioningProfile": {
#     "defaultNodePools": "Auto",
#     "mode": "Manual"
#   },
#   "nodeResourceGroup": "MC_helm-deploy-rg_azure-advisor_centralindia",
#   "nodeResourceGroupProfile": null,
#   "oidcIssuerProfile": {
#     "enabled": true,
#     "issuerUrl": "https://centralindia.oic.prod-aks.azure.com/189de737-c93a-4f5a-8b68-6f4ca9941912/99c619ef-6c2e-4c7b-b445-63ce47e774bf/"
#   },
#   "podIdentityProfile": null,
#   "powerState": {
#     "code": "Running"
#   },
#   "privateFqdn": null,
#   "privateLinkResources": null,
#   "provisioningState": "Succeeded",
#   "publicNetworkAccess": null,
#   "resourceGroup": "helm-deploy-rg",
#   "resourceUid": "696ba6dc25cb5c00018d3814",
#   "securityProfile": {
#     "azureKeyVaultKms": null,
#     "customCaTrustCertificates": null,
#     "defender": null,
#     "imageCleaner": {
#       "enabled": true,
#       "intervalHours": 168
#     },
#     "workloadIdentity": {
#       "enabled": true
#     }
#   },
#   "serviceMeshProfile": null,
#   "servicePrincipalProfile": {
#     "clientId": "msi",
#     "secret": null
#   },
#   "sku": {
#     "name": "Base",
#     "tier": "Free"
#   },
#   "status": null,
#   "storageProfile": {
#     "blobCsiDriver": null,
#     "diskCsiDriver": {
#       "enabled": true
#     },
#     "fileCsiDriver": {
#       "enabled": true
#     },
#     "snapshotController": {
#       "enabled": true
#     }
#   },
#   "supportPlan": "KubernetesOfficial",
#   "systemData": null,
#   "tags": null,
#   "type": "Microsoft.ContainerService/ManagedClusters",
#   "upgradeSettings": null,
#   "windowsProfile": {
#     "adminPassword": null,
#     "adminUsername": "azureuser",
#     "enableCsiProxy": true,
#     "gmsaProfile": null,
#     "licenseType": null
#   },
#   "workloadAutoScalerProfile": {
#     "keda": null,
#     "verticalPodAutoscaler": null
#   }
# }
  # Create User Assigned Managed Identity
az identity create \
    --name azure-advisor-mi \
    --resource-group helm-deploy-rg

#output 
# {
#   "clientId": "f781c567-188c-47cf-a6f0-ea812679c6a6",
#   "id": "/subscriptions/24266d0b-0add-41f2-9300-251baba58df4/resourcegroups/helm-deploy-rg/providers/Microsoft.ManagedIdentity/userAssignedIdentities/azure-advisor-mi",
#   "location": "centralindia",
#   "name": "azure-advisor-mi",
#   "principalId": "333f7539-3d5c-4a8b-a289-c1880650ca08",
#   "resourceGroup": "helm-deploy-rg",
#   "systemData": null,
#   "tags": {},
#   "tenantId": "189de737-c93a-4f5a-8b68-6f4ca9941912",
#   "type": "Microsoft.ManagedIdentity/userAssignedIdentities"
# }

# Grant RBAC to Azure Foundry

az role assignment create \
  --assignee f781c567-188c-47cf-a6f0-ea812679c6a6 \
  --role "Cognitive Services OpenAI User" \
  --scope "/subscriptions/24266d0b-0add-41f2-9300-251baba58df4/resourceGroups/rg-shivam-playin-w-ai/providers/Microsoft.CognitiveServices/accounts/shivam-playin-w-ai-resource"


# Assign the Managed Identity to AKS
az aks pod-identity add --resource-group helm-deploy-rg \
    --cluster-name azure-advisor \
    --namespace default \
    --name azure-advisor-mi-binding \
    --identity-resource-id $(az identity show --name azure-advisor-mi --resource-group helm-deploy-rg --query id -o tsv)    

    
