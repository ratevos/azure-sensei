# conditionalAccessUsers resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccessusers?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

Represents users, groups, and roles included in and excluded from the policy scope.

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
| excludeGroups | String collection | Group IDs excluded from scope of policy. |
| excludeGuestsOrExternalUsers | [conditionalAccessGuestsOrExternalUsers](conditionalaccessguestsorexternalusers.md) | Internal guests or external users excluded from the policy scope. Optionally populated. |
| excludeRoles | String collection | Role IDs excluded from scope of policy. |
| excludeUsers | String collection | User IDs excluded from scope of policy and/or `GuestsOrExternalUsers`. |
| includeGroups | String collection | Group IDs in scope of policy unless explicitly excluded. |
| includeGuestsOrExternalUsers | [conditionalAccessGuestsOrExternalUsers](conditionalaccessguestsorexternalusers.md) | Internal guests or external users included in the policy scope. Optionally populated. |
| includeRoles | String collection | Role IDs in scope of policy unless explicitly excluded. |
| includeUsers | String collection | User IDs in scope of policy unless explicitly excluded, `None`, `All`, or `GuestsOrExternalUsers`. |

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "excludeGroups": ["String"],
  "excludeGuestsOrExternalUsers": {"@odata.type": "microsoft.graph.conditionalAccessGuestOrExternalUsers"},
  "excludeRoles": ["String"],
  "excludeUsers": ["String"],
  "includeGroups": ["String"],
  "includeGuestsOrExternalUsers": {"@odata.type": "microsoft.graph.conditionalAccessGuestOrExternalUsers"},
  "includeRoles": ["String"],
  "includeUsers": ["String"]  
}
```
