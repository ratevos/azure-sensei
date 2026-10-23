# conditionalAccessSessionControls resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/conditionalaccesssessioncontrols?view=graph-rest-1.0  
> Microsoft doc last updated: 04/03/2024


Namespace: microsoft.graph

Represents session controls that are enforced after sign-in.
All the session controls inherit from [conditionalAccessSessionControl](conditionalaccesssessioncontrol.md).

## Properties

| Property     | Type        | Description |
|:-------------|:------------|:------------|
|applicationEnforcedRestrictions|[applicationEnforcedRestrictionsSessionControl](applicationenforcedrestrictionssessioncontrol.md)| Session control to enforce application restrictions. Only Exchange Online and Sharepoint Online support this session control. |
|cloudAppSecurity|[cloudAppSecuritySessionControl](cloudappsecuritysessioncontrol.md)| Session control to apply cloud app security.|
|disableResilienceDefaults|Boolean| Session control that determines whether it is acceptable for Microsoft Entra ID to extend existing sessions based on information collected prior to an outage or not.|
|persistentBrowser|[persistentBrowserSessionControl](persistentbrowsersessioncontrol.md)| Session control to define whether to persist cookies or not. All apps should be selected for this session control to work correctly. |
|signInFrequency|[signInFrequencySessionControl](signinfrequencysessioncontrol.md)| Session control to enforce signin frequency.|

## Relationships

None.

## JSON representation

The following JSON representation shows the resource type.

```json
{
  "applicationEnforcedRestrictions": {"@odata.type": "microsoft.graph.applicationEnforcedRestrictionsSessionControl"},
  "cloudAppSecurity": {"@odata.type": "microsoft.graph.cloudAppSecuritySessionControl"},
  "disableResilienceDefaults": false,
  "persistentBrowser": {"@odata.type": "microsoft.graph.persistentBrowserSessionControl"},
  "signInFrequency": {"@odata.type": "microsoft.graph.signInFrequencySessionControl"}
}
```
