#!/usr/bin/env bash
# Sparse-clone the official Microsoft docs repos used by build_refs.py.
# Usage: MS_DOCS_SRC=/tmp/src ./fetch_sources.sh && python3 build_refs.py <skill>/references
set -euo pipefail
SRC="${MS_DOCS_SRC:-/tmp/src}"; mkdir -p "$SRC"; cd "$SRC"
sparse() { local url=$1 dir=$2; shift 2; rm -rf "$dir"
  git clone -q --depth 1 --filter=blob:none --sparse "$url" "$dir"
  (cd "$dir" && git sparse-checkout set --no-cone "$@"); echo "fetched $dir"; }
G=https://github.com/MicrosoftDocs
sparse $G/entra-docs entra-docs /docs/identity/conditional-access/ /docs/identity/authentication/ \
  /docs/id-governance/privileged-identity-management/ '/docs/id-governance/*.md' /docs/id-protection/ /docs/identity/hybrid/ \
  /docs/identity/enterprise-apps/ /docs/identity/role-based-access-control/ /docs/identity/monitoring-health/ \
  /docs/identity/users/ '/docs/fundamentals/*.md' /docs/includes/
sparse $G/office-docs-powershell office-docs-powershell /exchange/docs-conceptual/ /exchange/exchange-ps/ExchangePowerShell/
sparse $G/azure-aks-docs azure-aks-docs /articles/aks/ /includes/
sparse $G/azure-docs azure-docs /articles/azure-resource-manager/management/ /articles/role-based-access-control/ \
  /articles/governance/policy/ /articles/governance/management-groups/ /includes/
sparse $G/microsoft-365-docs microsoft-365-docs /microsoft-365/admin/ /microsoft-365/enterprise/ \
  /microsoft-365/baseline-security-mode/ /microsoft-365/security/ /microsoft-365/includes/ /includes/
P=docs-ref-autogen/Latest-version/latest
sparse $G/azure-docs-cli azure-docs-cli "/$P/aks*" "/$P/keyvault*" "/$P/role*" "/$P/policy*" "/$P/group*" \
  "/$P/lock*" "/$P/tag*" "/$P/account/management-group*" "/$P/ad/*" "/$P/ad.yml" "/$P/identity*"
V=/api-reference/v1.0
sparse https://github.com/microsoftgraph/microsoft-graph-docs-contrib graph \
  "$V/resources/conditionalaccess*" "$V/api/conditionalaccess*" "$V/resources/*namedlocation*" "$V/api/*namedlocation*" \
  "$V/resources/authenticationstrength*" "$V/api/authenticationstrength*" "$V/resources/unifiedrole*" "$V/api/rbacapplication*" \
  "$V/resources/privilegedaccessgroup*" "$V/resources/riskyuser*" "$V/resources/authenticationmethodspolicy*" \
  "$V/api/authenticationmethodspolicy*" "$V/includes/snippets/powershell/" "$V/includes/permissions/" "$V/api/" "$V/includes/rbac-for-apis/" /concepts/permissions-reference.md /concepts/permissions-overview.md
