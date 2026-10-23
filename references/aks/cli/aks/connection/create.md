# az aks connection create

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/connection/create  
> Microsoft doc last updated: unknown

Create a connection between a aks and a target resource.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_connection_create_app-insights`, `az_aks_connection_create_appconfig`, `az_aks_connection_create_cognitiveservices`, `az_aks_connection_create_confluent-cloud`, `az_aks_connection_create_cosmos-cassandra`, `az_aks_connection_create_cosmos-gremlin`, `az_aks_connection_create_cosmos-mongo`, `az_aks_connection_create_cosmos-sql`, `az_aks_connection_create_cosmos-table`, `az_aks_connection_create_eventhub`, `az_aks_connection_create_keyvault`, `az_aks_connection_create_mongodb-atlas`, `az_aks_connection_create_mysql`, `az_aks_connection_create_mysql-flexible`, `az_aks_connection_create_mysql-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_neon-postgres`, `az_aks_connection_create_postgres`, `az_aks_connection_create_postgres-flexible`, `az_aks_connection_create_postgres-flexible(serviceconnector-passwordless)`, `az_aks_connection_create_redis`, `az_aks_connection_create_redis-enterprise`, `az_aks_connection_create_servicebus`, `az_aks_connection_create_signalr`, `az_aks_connection_create_sql`, `az_aks_connection_create_sql(serviceconnector-passwordless)`, `az_aks_connection_create_storage-blob`, `az_aks_connection_create_storage-file`, `az_aks_connection_create_storage-queue`, `az_aks_connection_create_storage-table`, `az_aks_connection_create_webpubsub`

## az aks connection create app-insights  (Preview)

Create a aks connection to app-insights.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app-insights` — Name of the app insights. Required if '--target-id' is not specified.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--app-insights'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the app insights. Required if '--target-id' is not specified.

*Create a connection between aks and app-insights interactively*
```azurecli
az aks connection create app-insights
```

*Create a connection between aks and app-insights with resource name*
```azurecli
az aks connection create app-insights -g ClusterRG -n MyCluster --tg AppInsightsRG --app-insights MyAppInsights --secret
```

*Create a connection between aks and app-insights with resource id*
```azurecli
az aks connection create app-insights --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/microsoft.insights/components/{appinsights} --secret
```

## az aks connection create appconfig  (Preview)

Create a aks connection to appconfig.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--app-config` — Name of the app configuration. Required if '--target-id' is not specified.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--app-config'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the app configuration. Required if '--target-id' is not specified.
- `--use-appconfig-extension -e` — Install Azure App Configuration extension in the Kubernetes cluster. Default: False.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and appconfig interactively*
```azurecli
az aks connection create appconfig
```

*Create a connection between aks and appconfig with resource name*
```azurecli
az aks connection create appconfig -g ClusterRG -n MyCluster --tg AppconfigRG --app-config MyConfigStore --secret
```

*Create a connection between aks and appconfig with resource id*
```azurecli
az aks connection create appconfig --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.AppConfiguration/configurationStores/{config_store} --secret
```

## az aks connection create cognitiveservices  (Preview)

Create a aks connection to cognitiveservices.

**Optional parameters**

- `--account` — Name of the cognitive services account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cognitive services. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cognitiveservices interactively*
```azurecli
az aks connection create cognitiveservices
```

*Create a connection between aks and cognitiveservices with resource name*
```azurecli
az aks connection create cognitiveservices -g ClusterRG -n MyCluster --tg CognitiveServicesRG --account MyAccount --secret
```

*Create a connection between aks and cognitiveservices with resource id*
```azurecli
az aks connection create cognitiveservices --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.CognitiveServices/accounts/{account} --secret
```

## az aks connection create confluent-cloud  (Preview)

Create a aks connection to confluent-cloud.

**Required parameters**

- `--bootstrap-server` — Kafka bootstrap server url.
- `--kafka-key` — Kafka API-Key (key).
- `--kafka-secret` — Kafka API-Key (secret).
- `--schema-key` — Schema registry API-Key (key).
- `--schema-registry` — Schema registry url.
- `--schema-secret` — Schema registry API-Key (secret).

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the connection.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.

*Create a connection between aks and confluent-cloud*
```azurecli
az aks connection create confluent-cloud -g ClusterRG -n MyCluster --bootstrap-server xxx.eastus.azure.confluent.cloud:9092 --kafka-key Name --kafka-secret Secret --schema-registry https://xxx.eastus.azure.confluent.cloud --schema-key Name --schema-secret Secret
```

## az aks connection create cosmos-cassandra  (Preview)

Create a aks connection to cosmos-cassandra.

**Optional parameters**

- `--account` — Name of the cosmos database account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--key-space` — Name of the keyspace. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account', '--key-space'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cosmos-cassandra interactively*
```azurecli
az aks connection create cosmos-cassandra
```

*Create a connection between aks and cosmos-cassandra with resource name*
```azurecli
az aks connection create cosmos-cassandra -g ClusterRG -n MyCluster --tg CosmosRG --account MyAccount --key-space MyKeySpace --secret
```

*Create a connection between aks and cosmos-cassandra with resource id*
```azurecli
az aks connection create cosmos-cassandra --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DocumentDB/databaseAccounts/{account}/cassandraKeyspaces/{key_space} --secret
```

## az aks connection create cosmos-gremlin  (Preview)

Create a aks connection to cosmos-gremlin.

**Optional parameters**

- `--account` — Name of the cosmos database account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the database. Required if '--target-id' is not specified.
- `--graph` — Name of the graph. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account', '--database', '--graph'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cosmos-gremlin interactively*
```azurecli
az aks connection create cosmos-gremlin
```

*Create a connection between aks and cosmos-gremlin with resource name*
```azurecli
az aks connection create cosmos-gremlin -g ClusterRG -n MyCluster --tg CosmosRG --account MyAccount --database MyDB --graph MyGraph --secret
```

*Create a connection between aks and cosmos-gremlin with resource id*
```azurecli
az aks connection create cosmos-gremlin --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DocumentDB/databaseAccounts/{account}/gremlinDatabases/{database}/graphs/{graph} --secret
```

## az aks connection create cosmos-mongo  (Preview)

Create a aks connection to cosmos-mongo.

**Optional parameters**

- `--account` — Name of the cosmos database account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cosmos-mongo interactively*
```azurecli
az aks connection create cosmos-mongo
```

*Create a connection between aks and cosmos-mongo with resource name*
```azurecli
az aks connection create cosmos-mongo -g ClusterRG -n MyCluster --tg CosmosRG --account MyAccount --database MyDB --secret
```

*Create a connection between aks and cosmos-mongo with resource id*
```azurecli
az aks connection create cosmos-mongo --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DocumentDB/databaseAccounts/{account}/mongodbDatabases/{database} --secret
```

## az aks connection create cosmos-sql  (Preview)

Create a aks connection to cosmos-sql.

**Optional parameters**

- `--account` — Name of the cosmos database account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cosmos-sql interactively*
```azurecli
az aks connection create cosmos-sql
```

*Create a connection between aks and cosmos-sql with resource name*
```azurecli
az aks connection create cosmos-sql -g ClusterRG -n MyCluster --tg CosmosRG --account MyAccount --database MyDB --secret
```

*Create a connection between aks and cosmos-sql with resource id*
```azurecli
az aks connection create cosmos-sql --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DocumentDB/databaseAccounts/{account}/sqlDatabases/{database} --secret
```

## az aks connection create cosmos-table  (Preview)

Create a aks connection to cosmos-table.

**Optional parameters**

- `--account` — Name of the cosmos database account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--table` — Name of the table. Required if '--target-id' is not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account', '--table'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the cosmos database account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and cosmos-table interactively*
```azurecli
az aks connection create cosmos-table
```

*Create a connection between aks and cosmos-table with resource name*
```azurecli
az aks connection create cosmos-table -g ClusterRG -n MyCluster --tg CosmosRG --account MyAccount --table MyTable --secret
```

*Create a connection between aks and cosmos-table with resource id*
```azurecli
az aks connection create cosmos-table --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DocumentDB/databaseAccounts/{account}/tables/{table} --secret
```

## az aks connection create eventhub  (Preview)

Create a aks connection to eventhub.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--namespace` — Name of the eventhub namespace. Required if '--target-id' is not specified.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--namespace'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the eventhub. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and eventhub interactively*
```azurecli
az aks connection create eventhub
```

*Create a connection between aks and eventhub with resource name*
```azurecli
az aks connection create eventhub -g ClusterRG -n MyCluster --tg EventhubRG --namespace MyNamespace --secret
```

*Create a connection between aks and eventhub with resource id*
```azurecli
az aks connection create eventhub --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.EventHub/namespaces/{namespace} --secret
```

## az aks connection create keyvault  (Preview)

Create a aks connection to keyvault.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--enable-csi` — Use keyvault as a secrets store via a CSI volume. If specified, AuthType Arguments are not needed. Default: False.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Indicates whether to create a new keyvault when creating the aks connection. Default: False.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--vault'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the keyvault. Required if '--target-id' is not specified.
- `--vault` — Name of the keyvault. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and keyvault interactively*
```azurecli
az aks connection create keyvault
```

*Create a connection between aks and keyvault with resource name*
```azurecli
az aks connection create keyvault -g ClusterRG -n MyCluster --tg KeyvaultRG --vault MyVault --enable-csi
```

*Create a connection between aks and keyvault with resource id*
```azurecli
az aks connection create keyvault --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.KeyVault/vaults/{vault} --enable-csi
```

*Create a new keyvault and connect aks to it interactively*
```azurecli
az aks connection create keyvault --new
```

*Create a new keyvault and connect aks to it*
```azurecli
az aks connection create keyvault --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --new
```

## az aks connection create mongodb-atlas  (Preview)

Create a aks connection to mongodb-atlas.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The connection string for secret auth.
- `--server` — Name of the MongoDB Atlas server. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the MongoDB Atlas. Required if '--target-id' is not specified.

*Create a connection between aks and mongodb-atlas interactively*
```azurecli
az aks connection create mongodb-atlas
```

*Create a connection between aks and mongodb-atlas with resource name*
```azurecli
az aks connection create mongodb-atlas -g ClusterRG -n MyCluster --tg MongoDBAtlasRG --server MongoDBAtlasServer --secret secret=xx
```

## az aks connection create mysql  (Preview and Deprecated)

Create a aks connection to mysql.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the mysql database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the mysql server. Required if '--target-id' is not specified.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the mysql server. Required if '--target-id' is not specified.

*Create a connection between aks and mysql interactively*
```azurecli
az aks connection create mysql
```

*Create a connection between aks and mysql with resource name*
```azurecli
az aks connection create mysql -g ClusterRG -n MyCluster --tg MysqlRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and mysql with resource id*
```azurecli
az aks connection create mysql --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBForMySQL/servers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create mysql-flexible  (Preview)

Create a aks connection to mysql-flexible.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the mysql flexible database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the mysql flexible server. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the mysql flexible server. Required if '--target-id' is not specified.

*Create a connection between aks and mysql-flexible interactively*
```azurecli
az aks connection create mysql-flexible
```

*Create a connection between aks and mysql-flexible with resource name*
```azurecli
az aks connection create mysql-flexible -g ClusterRG -n MyCluster --tg MysqlRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and mysql-flexible with resource id*
```azurecli
az aks connection create mysql-flexible --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBforMySQL/flexibleServers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create mysql-flexible  (extension: aks-preview etc.)

Create a aks connection to mysql-flexible.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the mysql flexible database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Deleting existing users with the same name before creating a new user in database. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the mysql flexible server. Required if '--target-id' is not specified.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the mysql flexible server. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Create a connection between aks and mysql-flexible interactively*
```azurecli
az aks connection create mysql-flexible
```

*Create a connection between aks and mysql-flexible with resource name*
```azurecli
az aks connection create mysql-flexible -g ClusterRG -n MyCluster --tg MysqlRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and mysql-flexible with resource id*
```azurecli
az aks connection create mysql-flexible --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBforMySQL/flexibleServers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create neon-postgres  (Preview)

Create a aks connection to neon-postgres.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the sql database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the sql server. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.

*Create a connection between aks and neon-postgres interactively*
```azurecli
az aks connection create neon-postgres
```

*Create a connection between aks and neon-postgres with resource name*
```azurecli
az aks connection create neon-postgres -g ClusterRG -n MyCluster --server MyServer --database MyDB --secret name=XX secret=XX
```

## az aks connection create postgres  (Preview and Deprecated)

Create a aks connection to postgres.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of postgres database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Indicates whether to create a new postgres when creating the aks connection. Default: False.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of postgres server. Required if '--target-id' is not specified.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the postgres service. Required if '--target-id' is not specified.

*Create a connection between aks and postgres interactively*
```azurecli
az aks connection create postgres
```

*Create a connection between aks and postgres with resource name*
```azurecli
az aks connection create postgres -g ClusterRG -n MyCluster --tg PostgresRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and postgres with resource id*
```azurecli
az aks connection create postgres --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBforPostgreSQL/servers/{server}/databases/{database} --secret name=XX secret=XX
```

*Create a new postgres and connect aks to it interactively*
```azurecli
az aks connection create postgres --new
```

*Create a new postgres and connect aks to it*
```azurecli
az aks connection create postgres --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --new
```

## az aks connection create postgres-flexible  (Preview)

Create a aks connection to postgres-flexible.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of postgres flexible database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of postgres flexible server. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the flexible postgres service. Required if '--target-id' is not specified.

*Create a connection between aks and postgres-flexible interactively*
```azurecli
az aks connection create postgres-flexible
```

*Create a connection between aks and postgres-flexible with resource name*
```azurecli
az aks connection create postgres-flexible -g ClusterRG -n MyCluster --tg PostgresRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and postgres-flexible with resource id*
```azurecli
az aks connection create postgres-flexible --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create postgres-flexible  (extension: aks-preview etc.)

Create a aks connection to postgres-flexible.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of postgres flexible database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Deleting existing users with the same name before creating a new user in database. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of postgres flexible server. Required if '--target-id' is not specified.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the flexible postgres service. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Create a connection between aks and postgres-flexible interactively*
```azurecli
az aks connection create postgres-flexible
```

*Create a connection between aks and postgres-flexible with resource name*
```azurecli
az aks connection create postgres-flexible -g ClusterRG -n MyCluster --tg PostgresRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and postgres-flexible with resource id*
```azurecli
az aks connection create postgres-flexible --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.DBforPostgreSQL/flexibleServers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create redis  (Preview)

Create a aks connection to redis.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the redis database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the redis server. Required if '--target-id' is not specified.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the redis server. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and redis interactively*
```azurecli
az aks connection create redis
```

*Create a connection between aks and redis with resource name*
```azurecli
az aks connection create redis -g ClusterRG -n MyCluster --tg RedisRG --server MyServer --database MyDB --secret
```

*Create a connection between aks and redis with resource id*
```azurecli
az aks connection create redis --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Cache/redis/{server}/databases/{database} --secret
```

## az aks connection create redis-enterprise  (Preview)

Create a aks connection to redis-enterprise.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the redis enterprise database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the redis enterprise server. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the redis server. Required if '--target-id' is not specified.

*Create a connection between aks and redis-enterprise interactively*
```azurecli
az aks connection create redis-enterprise
```

*Create a connection between aks and redis-enterprise with resource name*
```azurecli
az aks connection create redis-enterprise -g ClusterRG -n MyCluster --tg RedisRG --server MyServer --database MyDB --secret
```

*Create a connection between aks and redis-enterprise with resource id*
```azurecli
az aks connection create redis-enterprise --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Cache/redisEnterprise/{server}/databases/{database} --secret
```

## az aks connection create servicebus  (Preview)

Create a aks connection to servicebus.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--namespace` — Name of the servicebus namespace. Required if '--target-id' is not specified.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--namespace'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the servicebus. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and servicebus interactively*
```azurecli
az aks connection create servicebus
```

*Create a connection between aks and servicebus with resource name*
```azurecli
az aks connection create servicebus -g ClusterRG -n MyCluster --tg ServicebusRG --namespace MyNamespace --secret
```

*Create a connection between aks and servicebus with resource id*
```azurecli
az aks connection create servicebus --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.ServiceBus/namespaces/{namespace} --secret
```

## az aks connection create signalr  (Preview)

Create a aks connection to signalr.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--signalr` — Name of the signalr service. Required if '--target-id' is not specified.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--signalr'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the signalr. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and signalr interactively*
```azurecli
az aks connection create signalr
```

*Create a connection between aks and signalr with resource name*
```azurecli
az aks connection create signalr -g ClusterRG -n MyCluster --tg SignalrRG --signalr MySignalR --secret
```

*Create a connection between aks and signalr with resource id*
```azurecli
az aks connection create signalr --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.SignalRService/SignalR/{signalr} --secret
```

## az aks connection create sql  (Preview)

Create a aks connection to sql.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the sql database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the sql server. Required if '--target-id' is not specified.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the sql server. Required if '--target-id' is not specified.

*Create a connection between aks and sql interactively*
```azurecli
az aks connection create sql
```

*Create a connection between aks and sql with resource name*
```azurecli
az aks connection create sql -g ClusterRG -n MyCluster --tg SqlRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and sql with resource id*
```azurecli
az aks connection create sql --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Sql/servers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create sql  (extension: aks-preview etc.)

Create a aks connection to sql.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--database` — Name of the sql database. Required if '--target-id' is not specified.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Deleting existing users with the same name before creating a new user in database. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--server` — Name of the sql server. Required if '--target-id' is not specified.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--server', '--database'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the sql server. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.
- `--yes -y` — Do not prompt for confirmation. Default: False.

*Create a connection between aks and sql interactively*
```azurecli
az aks connection create sql
```

*Create a connection between aks and sql with resource name*
```azurecli
az aks connection create sql -g ClusterRG -n MyCluster --tg SqlRG --server MyServer --database MyDB --secret name=XX secret=XX
```

*Create a connection between aks and sql with resource id*
```azurecli
az aks connection create sql --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Sql/servers/{server}/databases/{database} --secret name=XX secret=XX
```

## az aks connection create storage-blob  (Preview)

Create a aks connection to storage-blob.

**Optional parameters**

- `--account` — Name of the storage account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--new` — Indicates whether to create a new storage-blob when creating the aks connection. Default: False.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the storage account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and storage-blob interactively*
```azurecli
az aks connection create storage-blob
```

*Create a connection between aks and storage-blob with resource name*
```azurecli
az aks connection create storage-blob -g ClusterRG -n MyCluster --tg StorageRG --account MyAccount --secret
```

*Create a connection between aks and storage-blob with resource id*
```azurecli
az aks connection create storage-blob --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Storage/storageAccounts/{account}/blobServices/default --secret
```

*Create a new storage-blob and connect aks to it interactively*
```azurecli
az aks connection create storage-blob --new
```

*Create a new storage-blob and connect aks to it*
```azurecli
az aks connection create storage-blob --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --new
```

## az aks connection create storage-file  (Preview)

Create a aks connection to storage-file.

**Optional parameters**

- `--account` — Name of the storage account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the storage account. Required if '--target-id' is not specified.

*Create a connection between aks and storage-file interactively*
```azurecli
az aks connection create storage-file
```

*Create a connection between aks and storage-file with resource name*
```azurecli
az aks connection create storage-file -g ClusterRG -n MyCluster --tg StorageRG --account MyAccount --secret
```

*Create a connection between aks and storage-file with resource id*
```azurecli
az aks connection create storage-file --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Storage/storageAccounts/{account}/fileServices/default --secret
```

## az aks connection create storage-queue  (Preview)

Create a aks connection to storage-queue.

**Optional parameters**

- `--account` — Name of the storage account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the storage account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and storage-queue interactively*
```azurecli
az aks connection create storage-queue
```

*Create a connection between aks and storage-queue with resource name*
```azurecli
az aks connection create storage-queue -g ClusterRG -n MyCluster --tg StorageRG --account MyAccount --secret
```

*Create a connection between aks and storage-queue with resource id*
```azurecli
az aks connection create storage-queue --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Storage/storageAccounts/{account}/queueServices/default --secret
```

## az aks connection create storage-table  (Preview)

Create a aks connection to storage-table.

**Optional parameters**

- `--account` — Name of the storage account. Required if '--target-id' is not specified.
- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-endpoint` — Connect target service by service endpoint. Source resource must be in the VNet and target SKU must support service endpoint feature.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--account'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the storage account. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and storage-table interactively*
```azurecli
az aks connection create storage-table
```

*Create a connection between aks and storage-table with resource name*
```azurecli
az aks connection create storage-table -g ClusterRG -n MyCluster --tg StorageRG --account MyAccount --secret
```

*Create a connection between aks and storage-table with resource id*
```azurecli
az aks connection create storage-table --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.Storage/storageAccounts/{account}/tableServices/default --secret
```

## az aks connection create webpubsub  (Preview)

Create a aks connection to webpubsub.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--appconfig-id` — The app configuration id to store configuration.
- `--change-reference` — The related change reference ID for this resource operation.
- `--client-type` — The client type used on the aks.
- `--connection` — Name of the aks connection.
- `--connstr-props` — The additional connection string properties used to build connection string.
- `--customized-keys` — The customized keys used to change default configuration names. Key is the original name, value is the customized name.
- `--kube-namespace` — The kubernetes namespace where the connection information will be saved into (as kubernetes secret). Default: default.
- `--name -n` — Name of the managed cluster. Required if '--source-id' is not specified.None.
- `--no-recreate` — Skip executing creation operation when no updates to an existing connection. Default: False.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--opt-out` — Whether to disable some configuration steps. Use configinfo to disbale configuration information changes on source. Use publicnetwork to disable public network access configuration.Use auth to skip auth configuration such as enabling managed identity and granting RBAC roles.
- `--private-endpoint` — Connect target service by private endpoint. The private endpoint in source virtual network must be created ahead.
- `--resource-group -g` — The resource group which contains the managed cluster. Required if '--source-id' is not specified.None.
- `--secret` — The secret auth info.
- `--service-principal` — The service principal auth info.
- `--source-id` — The resource id of a aks. Required if ['--resource-group', '--name'] are not specified.
- `--target-id` — The resource id of target service. Required if ['--target-resource-group', '--webpubsub'] are not specified.
- `--target-resource-group --tg` — The resource group which contains the webpubsub. Required if '--target-id' is not specified.
- `--webpubsub` — Name of the webpubsub service. Required if '--target-id' is not specified.
- `--workload-identity` — The user-assigned managed identity used to create workload identity federation.

*Create a connection between aks and webpubsub interactively*
```azurecli
az aks connection create webpubsub
```

*Create a connection between aks and webpubsub with resource name*
```azurecli
az aks connection create webpubsub -g ClusterRG -n MyCluster --tg WebpubsubRG --webpubsub MyWebPubSub --secret
```

*Create a connection between aks and webpubsub with resource id*
```azurecli
az aks connection create webpubsub --source-id /subscriptions/{subscription}/resourceGroups/{source_resource_group}/providers/Microsoft.ContainerService/managedClusters/{cluster} --target-id /subscriptions/{subscription}/resourceGroups/{target_resource_group}/providers/Microsoft.SignalRService/WebPubSub/{webpubsub} --secret
```
