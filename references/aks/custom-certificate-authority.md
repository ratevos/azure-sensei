# Custom Certificate Authority (CA) in Azure Kubernetes Service (AKS)

> Source: https://learn.microsoft.com/en-us/azure/aks/custom-certificate-authority  
> Microsoft doc last updated: 08/26/2026


Custom Certificate Authority (CA) support lets you add up to 10 base64-encoded certificates to your node's trust store. For new clusters, the CA certificate content can't exceed 35 KB. You often need this feature when the node requires certificate authorities (CAs), such as when connecting to a private registry.

This article shows you how to create custom CAs and apply them to your AKS clusters.

> [!NOTE]
> The Custom CA feature adds your custom certificates to the trust store of the AKS node. Certificates added with this feature aren't available to containers running in pods. If you need the certificates inside containers, you need to add them separately by adding them to the image used by your pods or at runtime via scripting and a secret.

## Prerequisites

- An Azure subscription. If you don't have an Azure subscription, create a [free account](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).
- Azure CLI version 2.72.0 or later installed and configured. To find your CLI version, run the `az --version` command. If you need to install or upgrade, see [Install Azure CLI][install-azure-cli].
- A base64 encoded certificate string or a text file with certificate.

## Limitations

- Windows node pools aren't supported.
- Installing different CAs in the same cluster isn't supported.
- For new clusters, the CA certificate content can't exceed 35 KB.

## Create a certificate file

- Create a text file containing up to 10 blank line-separated certificates. For new clusters, the CA certificate content in the file can't exceed 35 KB. When you pass this file to your cluster, the certificates are installed in the trust stores of the AKS node.

    Example text file:

    ```txt
        -----BEGIN CERTIFICATE-----
        cert1
        -----END CERTIFICATE-----

        -----BEGIN CERTIFICATE-----
        cert2
        -----END CERTIFICATE-----
    ```

**Before proceeding to the next step, make sure that there are no blank spaces in your text file to avoid errors**.

## Pass custom CAs to your AKS cluster

- Pass certificates to your cluster using the [`az aks create`][az-aks-create] or [`az aks update`][az-aks-update] command with `--custom-ca-trust-certificates` set to the name of your certificate file.

    ```azurecli-interactive
    # Create a new cluster
    az aks create \
        --resource-group <resource-group-name> \
        --name <cluster-name> \
        --node-count 2 \
        --custom-ca-trust-certificates <path-to-certificate-file> \
        --generate-ssh-keys

    # Update an existing cluster
    az aks update \
        --resource-group <resource-group-name> \
        --name <cluster-name> \
        --custom-ca-trust-certificates <path-to-certificate-file>
    ```

    > [!NOTE]
    > This operation triggers a model update to ensure all existing nodes have the same CAs installed for correct provisioning. AKS creates new nodes, drains existing nodes, deletes existing nodes, and replaces them with nodes that have the new set of CAs installed.

## Verify CAs are installed

- Verify the CAs are installed using the [`az aks show`][az-aks-show] command.

    ```azurecli-interactive
    az aks show --resource-group <resource-group-name> --name <cluster-name> | grep securityProfile -A 4
    ```

    In the output, the `securityProfile` section should include your custom CA certificates. For example:

    ```output
      "securityProfile": {
        "azureKeyVaultKms": null,
        "customCaTrustCertificates": [
            "values"
    ```

## Resolve custom CA formatting errors

Adding certificates to a cluster can result in an error if the file with the certificates isn't formatted properly. You might see an error similar to the following example:

```output
failed to decode one of SecurityProfile.CustomCATrustCertificates to PEM after base64 decoding
```

If you encounter this error, you should check that your input file has no extra new lines, white spaces, or data other than correctly formatted certificates as shown in the example file.

## Resolve custom CA X.509 Certificate Signed by Unknown Authority errors

AKS requires certificates passed to be properly formatted and base64 encoded. Make sure the CAs you passed are properly base64 encoded and that files with CAs don't have CRLF line breaks.

## Restart containerd to pick up new certificates

If containerd doesn't pick up new certificates, run the `systemctl restart containerd` command from the node's shell. Once containerd restarts, the container runtime should pick up the new certificates.

## `enableCustomCATrust` (preview) retirement migration

> [!IMPORTANT]
> Starting on September 14, 2026, the preview property `enableCustomCATrust` will retire. After that date, the `enableCustomCATrust=true` node pool-level field will no longer enable the Custom Certificate Authority (CA) feature in AKS. The last preview API that supports this property is `2025-08-02-preview`. Existing node pools that still rely on `enableCustomCATrust=true` might experience failures during scaling operations or when certificates are updated. To avoid service disruption, update the impacted clusters and node pools and remove the preview property before September 14, 2026. For migration steps, see [`enableCustomCATrust` (preview) retirement migration](https://learn.microsoft.com/en-us/azure/aks/custom-certificate-authority#enablecustomcatrust-preview-retirement-migration). For more information on this retirement, see the [Retirement GitHub issue](https://github.com/Azure/AKS/issues/5826). To stay informed about announcements and updates, follow the [AKS release notes](https://github.com/Azure/AKS/releases).

### Remove the Custom CA Trust property from your node pools

Current Azure CLI releases don't include the `--disable-custom-ca-trust` option. To remove the retiring `enableCustomCATrust` property, use a generic resource update for each affected node pool. The `2025-08-02-preview` API is the last API version that exposes this property.

```azurecli
POOL_ID=$(az aks nodepool show \
  --resource-group <resource-group> \
  --cluster-name <cluster-name> \
  --name <node-pool-name> \
  --query id \
  --output tsv)

az resource update \
  --ids "$POOL_ID" \
  --api-version 2025-08-02-preview \
  --set properties.enableCustomCATrust=false
```

This command retrieves the complete node pool resource, updates `enableCustomCATrust`, and sends the updated resource back. It preserves the other node pool properties.

Verify that the property is disabled and that the node pool update succeeded:

```azurecli
az rest \
  --method get \
  --url "https://management.azure.com${POOL_ID}?api-version=2025-08-02-preview" \
  --query "properties.{enableCustomCATrust:enableCustomCATrust,provisioningState:provisioningState}" \
  --output json
```

Repeat these steps for every node pool where `enableCustomCATrust` is enabled. The expected output shows `enableCustomCATrust` set to `false` and `provisioningState` set to `Succeeded`.

If you want Custom CA Trust enabled on your clusters after this retirement, use `--custom-ca-trust-certificates` and provide a path to a certificate file.

## Related content

For more information on AKS security best practices, see [Best practices for cluster security and upgrades in Azure Kubernetes Service (AKS)][aks-best-practices-security-upgrades].

[aks-best-practices-security-upgrades]: https://learn.microsoft.com/en-us/azure/aks/operator-best-practices-cluster-security
[az-aks-create]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-create
[az-aks-update]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-update
[az-aks-show]: https://learn.microsoft.com/en-us/cli/azure/aks#az-aks-show
[install-azure-cli]:  https://learn.microsoft.com/en-us/cli/azure/install-azure-cli
