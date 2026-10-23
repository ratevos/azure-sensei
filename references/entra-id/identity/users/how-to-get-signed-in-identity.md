# Get signed in identity

> Source: https://learn.microsoft.com/en-us/entra/identity/users/how-to-get-signed-in-identity  
> Microsoft doc last updated: 04/11/2025


## Overview

This article gives simple steps to get the identity of the currently signed in account. You can use this identity information later to grant role-based access control access to the signed in account to either manage data or resources in Azure.

The current Azure CLI session could be signed in with a human identity (your account), a managed identity, a workload identity, or a service principal. No matter what type of identity you use with Azure CLI, to steps to get the details of the identity can be similar. For more information, see [Microsoft Entra identity fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts#identity).

## Prerequisites

- An Azure account with an active subscription. [Create an account for free](https://azure.microsoft.com/pricing/purchase-options/azure-account?cid=msft_learn).

::: zone pivot="interface-cli"

::: zone-end

::: zone pivot="interface-portal"

::: zone-end

::: zone pivot="interface-shell"

::: zone-end

## Get signed in account identity

Use the command line to query the graph for information about your account's unique identifier.

::: zone pivot="interface-cli"

1. Get the details for the currently logged-in account using [`az ad signed-in-user`](https://learn.microsoft.com/en-us/cli/azure/ad/signed-in-user#az-ad-signed-in-user-show).

    ```azurecli-interactive
    az ad signed-in-user show
    ```

1. The command outputs a JSON response containing various fields.

    ```json
    {
      "@odata.context": "<https://graph.microsoft.com/v1.0/$metadata#users/$entity>",
      "businessPhones": [],
      "displayName": "Kai Carter",
      "givenName": "Kai",
      "id": "aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb",
      "jobTitle": "Senior Sales Representative",
      "mail": "<kai@adventure-works.com>",
      "mobilePhone": null,
      "officeLocation": "Redmond",
      "preferredLanguage": null,
      "surname": "Carter",
      "userPrincipalName": "<kai@adventure-works.com>"
    }
    ```

    > [!TIP]
    > Record the value of the `id` field. In this example, that value would be `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`. This value can then be used in various scripts to grant your current account role-based access control permissions to Azure resources.

::: zone-end

::: zone pivot="interface-portal"

Use the in-portal panes for Microsoft Entra ID to get details of your currently signed-in user account.

1. Sign in to the Azure portal (<https://portal.azure.com>).

1. On the **Home** pane, locate and select the **Microsoft Entra ID** option.

    

    > [!TIP]
    > If this option isn't listed, select **More services** and then search for **Microsoft Entra ID** using the search term **"Entra"**.

1. Within the **Overview** pane for the Microsoft Entra ID tenant, select **Users** inside the **Manage** section of the service menu.

    

1. In the list of users, select the identity (user) that you want to get more details about.

    

    > [!NOTE]
    > This screenshot illustrates an example user named *"Kai Carter"* with a principal of `kai@adventure-works.com`.

1. On the details pane for the specific user, observe the value of the **Object ID** property.

    

    > [!TIP]
    > Record the value of the **Object ID** property. In this example, that value would be `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`. This value can then be used in various scripts to grant your current account role-based access control permissions to Azure resources.

::: zone-end

::: zone pivot="interface-shell"

1. Get the details for the currently logged-in account using [`Get-AzADUser`](https://learn.microsoft.com/en-us/powershell/module/az.resources/get-azaduser).

    ```azurepowershell-interactive
    Get-AzADUser -SignedIn | Format-List `
        -Property Id, DisplayName, Mail, UserPrincipalName
    ```

1. The command outputs a list response containing various fields.

    ```output
    Id                : aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb
    DisplayName       : Kai Carter
    Mail              : kai@adventure-works.com
    UserPrincipalName : kai@adventure-works.com
    ```

    > [!TIP]
    > Record the value of the `id` field. In this example, that value would be `aaaaaaaa-0000-1111-2222-bbbbbbbbbbbb`. This value can then be used in various scripts to grant your current account role-based access control permissions to Azure resources.

::: zone-end
