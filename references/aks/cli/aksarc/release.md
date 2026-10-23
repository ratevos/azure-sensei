# az aksarc release

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc/release  
> Microsoft doc last updated: unknown

Manage VHD images for provisioned clusters.

Subgroups and commands: `az_aksarc_release_download`, `az_aksarc_release_save`

## az aksarc release download  (Preview; extension: aks-preview etc.)

Downloads the VHD images from a release.

**Required parameters**

- `--staging-folder` — Local directory path to store release files.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--audience` — Release catalog audience. Default value is stable. Default: stable.
- `--catalog` — Release catalog name. Default value is aks-hybrid-stable-catalogs-ext. Default: aks-hybrid-stable-catalogs-ext.
- `--change-reference` — The related change reference ID for this resource operation.
- `--extract-release` — Extracts the OS image release files after download, for backward compatibility with older versions. Note: This feature will be deprecated in the future.
- `--mode` — Minimum(default) downloads only Linux images. Full option downloads windows images also. Default: minimum.
- `--version` — Release version to be downloaded. If not specified, it defaults to latest release.

*DownloadLatestRelease*
```azurecli
az aksarc release download --staging-folder ./aksarc-release
```

## az aksarc release save  (Preview; extension: aks-preview etc.)

Provisions the downloaded VHD images to the arc resource bridge.

**Required parameters**

- `--staging-folder` — Directory path to import release files.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — Path to the Arc resource bridge appliance config file, resourceName-appliance.yaml. On Azure Local devices, this can be found running Get-ArcHciConfig command in Powershell.

*SaveRelease*
```azurecli
az aksarc release save --config-file ./work/resourceName-appliance.yaml --staging-folder ./aksarc-release
```
