# conditionalAccessApplications resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessapplications?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents the applications and user actions included in and excluded from the conditional access policy.

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| excludeApplications | String collection | Can be one of the following: <li> The list of client IDs (**appId**) explicitly excluded from the policy.<li> `Office365` - For the list of apps included in `Office365`, see [Apps included in Conditional Access Office 365 app suite](https://learn.microsoft.com/en-us/entra/identity/conditional-access/reference-office-365-application-contents) <li> `MicrosoftAdminPortals` - For more information, see [Conditional Access Target resources: Microsoft Admin Portals](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#microsoft-admin-portals)|
| includeApplications | String collection | Can be one of the following: <li> The list of client IDs (**appId**) the policy applies to, unless explicitly excluded (in **excludeApplications**) <li> `All` <li> `Office365` - For the list of apps included in `Office365`, see [Apps included in Conditional Access Office 365 app suite](https://learn.microsoft.com/en-us/entra/identity/conditional-access/reference-office-365-application-contents) <li> `MicrosoftAdminPortals` - For more information, see [Conditional Access Target resources: Microsoft Admin Portals](https://learn.microsoft.com/en-us/entra/identity/conditional-access/concept-conditional-access-cloud-apps#microsoft-admin-portals) |
| applicationFilter | [conditionalAccessFilter](conditionalaccessfilter.md) | Filter that defines the dynamic-application-syntax rule to include/exclude cloud applications. A filter can use custom security attributes to include/exclude applications. |
| includeUserActions | String collection | User actions to include. Supported values are `urn:user:registersecurityinfo` and `urn:user:registerdevice` |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "excludeApplications": ["String"],
  "includeApplications": ["String"],
  "applicationFilter": {"@odata.type": "microsoft.graph.conditionalAccessFilter"},
  "includeUserActions": ["String"]
}
```
