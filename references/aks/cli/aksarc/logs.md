# az aksarc logs

> Source: https://learn.microsoft.com/en-us/cli/azure/aksarc/logs  
> Microsoft doc last updated: unknown

Deprecated. Use 'az aksarc get-logs' instead.

Subgroups and commands: `az_aksarc_logs_hci`

## az aksarc logs hci  (Deprecated; extension: aks-preview etc.)

Collect logs from provisioned clusters and the underlying infrastructure.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--credentials-dir --ssh-key` — Path to SSH credentials to connect to nodes, either id_rsa file or directory is accepted.
- `--ip --ips` — IP addresses of nodes (control plane nodes or worker nodes) from which logs need to be collected.
- `--kubeconfig` — Path to kubeconfig file to connect to the cluster.
- `--out-dir` — Output directory to store collected logs. If not specified, logs will be stored in the current directory.

*Collect logs with IP address and SSH credentials*
```azurecli
az aksarc logs hci --ip 192.168.200.31 192.168.200.32 --ssh-key ~/.ssh --out-dir ./logs
```

*Collect logs with kubeconfig and SSH credentials, kubeconfig is only used to collect IP addresses, and ssh-key file path is used instead of directory*
```azurecli
az aksarc logs hci --kubeconfig ~/.kube/config --ssh-key ~/.ssh/id_rsa --out-dir ./logs
```
