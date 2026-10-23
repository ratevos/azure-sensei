# az aks connection update

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/connection/update  
> Microsoft doc last updated: unknown

Update a aks connection.

Subgroups and commands: `az_aks_connection_update_app-insights`, `az_aks_connection_update_appconfig`, `az_aks_connection_update_cognitiveservices`, `az_aks_connection_update_confluent-cloud`, `az_aks_connection_update_cosmos-cassandra`, `az_aks_connection_update_cosmos-gremlin`, `az_aks_connection_update_cosmos-mongo`, `az_aks_connection_update_cosmos-sql`, `az_aks_connection_update_cosmos-table`, `az_aks_connection_update_eventhub`, `az_aks_connection_update_keyvault`, `az_aks_connection_update_mongodb-atlas`, `az_aks_connection_update_mysql`, `az_aks_connection_update_mysql-flexible`, `az_aks_connection_update_neon-postgres`, `az_aks_connection_update_postgres`, `az_aks_connection_update_postgres-flexible`, `az_aks_connection_update_redis`, `az_aks_connection_update_redis-enterprise`, `az_aks_connection_update_servicebus`, `az_aks_connection_update_signalr`, `az_aks_connection_update_sql`, `az_aks_connection_update_storage-blob`, `az_aks_connection_update_storage-file`, `az_aks_connection_update_storage-queue`, `az_aks_connection_update_storage-table`, `az_aks_connection_update_webpubsub`

## az aks connection update app-insights  (Preview)

Update a aks to app-insights connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update app-insights -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update app-insights --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update appconfig  (Preview)

Update a aks to appconfig connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update appconfig -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update appconfig --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update cognitiveservices  (Preview)

Update a aks to cognitiveservices connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cognitiveservices -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cognitiveservices --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update confluent-cloud  (Preview)

Update a aks to confluent-cloud connection.

**Required parameters**

- `--connection` — Name of the connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--bootstrap-server` — Kafka bootstrap server url.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kafka-key` — Kafka API-Key (key).
- `--kafka-secret` — Kafka API-Key (secret).
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--schema-key` — Schema registry API-Key (key).
- `--schema-registry` — Schema registry url.
- `--schema-secret` — Schema registry API-Key (secret).
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.

*Update the client-type of a bootstrap server connection*
```azurecli
az aks connection update confluent-cloud -g ClusterRG -n MyCluster --connection MyConnection --client python
```

*Update the auth configurations of a bootstrap server connection*
```azurecli
az aks connection update confluent-cloud -g ClusterRG -n MyCluster --connection MyConnection --bootstrap-server xxx.eastus.azure.confluent.cloud:9092 --kafka-key Name --kafka-secret Secret
```

*Update the client-type of a schema registry connection*
```azurecli
az aks connection update confluent-cloud -g ClusterRG -n MyCluster --connection MyConnection_schema --client python
```

*Update the auth configurations of a schema registry connection*
```azurecli
az aks connection update confluent-cloud -g ClusterRG -n MyCluster --connection MyConnection_schema --schema-registry https://xxx.eastus.azure.confluent.cloud --schema-key Name --schema-secret Secret
```

## az aks connection update cosmos-cassandra  (Preview)

Update a aks to cosmos-cassandra connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cosmos-cassandra -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cosmos-cassandra --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update cosmos-gremlin  (Preview)

Update a aks to cosmos-gremlin connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cosmos-gremlin -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cosmos-gremlin --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update cosmos-mongo  (Preview)

Update a aks to cosmos-mongo connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cosmos-mongo -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cosmos-mongo --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update cosmos-sql  (Preview)

Update a aks to cosmos-sql connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cosmos-sql -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cosmos-sql --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update cosmos-table  (Preview)

Update a aks to cosmos-table connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update cosmos-table -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update cosmos-table --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update eventhub  (Preview)

Update a aks to eventhub connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update eventhub -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update eventhub --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update keyvault  (Preview)

Update a aks to keyvault connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update keyvault -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update keyvault --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update mongodb-atlas  (Preview)

Update a aks to mongodb-atlas connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The connection string for secret auth.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update mongodb-atlas -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update mongodb-atlas --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update mysql  (Preview and Deprecated)

Update a aks to mysql connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update mysql -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update mysql --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update mysql-flexible  (Preview)

Update a aks to mysql-flexible connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update mysql-flexible -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update mysql-flexible --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update neon-postgres  (Preview)

Update a aks to neon-postgres connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update neon-postgres -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update neon-postgres --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update postgres  (Preview and Deprecated)

Update a aks to postgres connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update postgres -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update postgres --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update postgres-flexible  (Preview)

Update a aks to postgres-flexible connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update postgres-flexible -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update postgres-flexible --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update redis  (Preview)

Update a aks to redis connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update redis -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update redis --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update redis-enterprise  (Preview)

Update a aks to redis-enterprise connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update redis-enterprise -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update redis-enterprise --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update servicebus  (Preview)

Update a aks to servicebus connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update servicebus -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update servicebus --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update signalr  (Preview)

Update a aks to signalr connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update signalr -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update signalr --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update sql  (Preview)

Update a aks to sql connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update sql -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update sql --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update storage-blob  (Preview)

Update a aks to storage-blob connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update storage-blob -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update storage-blob --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update storage-file  (Preview)

Update a aks to storage-file connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update storage-file -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update storage-file --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update storage-queue  (Preview)

Update a aks to storage-queue connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update storage-queue -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update storage-queue --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update storage-table  (Preview)

Update a aks to storage-table connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update storage-table -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update storage-table --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```

## az aks connection update webpubsub  (Preview)

Update a aks to webpubsub connection.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--id` — The resource id of the connection. ['--resource-group', '--name', '--connection'] are required if '--id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Update the client type of a connection with resource name*
```azurecli
az aks connection update webpubsub -g ClusterRG -n MyCluster --connection MyConnection --client-type dotnet
```

*Update the client type of a connection with resource id*
```azurecli
az aks connection update webpubsub --id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.Web/sites/{site}/providers/Microsoft.ServiceLinker/linkers/{linker} --client-type dotnet
```
