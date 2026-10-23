# Execute-AzureADLabelSync

> Source: https://learn.microsoft.com/powershell/module/exchangepowershell/execute-azureadlabelsync  
> Microsoft doc last updated: unknown


## SYNOPSIS
This cmdlet is available only in Security & Compliance PowerShell. For more information, see [Security & Compliance PowerShell](https://learn.microsoft.com/powershell/exchange/scc-powershell).

Use the Execute-AzureADLabelSync cmdlet to start the synchronization of sensitivity labels into Microsoft Entra ID. This allows the application of sensitivity labels to Microsoft Teams sites, Microsoft 365 Groups, and SharePoint sites. This cmdlet is required if you were using sensitivity labels before September 2019.

For information about the parameter sets in the Syntax section below, see [Exchange cmdlet syntax](https://learn.microsoft.com/powershell/exchange/exchange-cmdlet-syntax).

## SYNTAX

```
Execute-AzureADLabelSync [<CommonParameters>]
```

## DESCRIPTION
To use this cmdlet in Security & Compliance PowerShell, you need to be assigned permissions. For more information, see [Permissions in the Microsoft Purview compliance portal](https://learn.microsoft.com/purview/microsoft-365-compliance-center-permissions).

## EXAMPLES

### Example 1
```powershell
Execute-AzureADLabelSync
```

This example initializes the synchronization of sensitivity labels into Microsoft Entra ID.

## PARAMETERS

### CommonParameters
This cmdlet supports the common parameters: -Debug, -ErrorAction, -ErrorVariable, -InformationAction, -InformationVariable, -OutVariable, -OutBuffer, -PipelineVariable, -Verbose, -WarningAction, and -WarningVariable. For more information, see [about_CommonParameters](https://go.microsoft.com/fwlink/p/?LinkID=113216).

## INPUTS

## OUTPUTS

## NOTES

## RELATED LINKS
