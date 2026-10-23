# privilegedAccessGroup resource type

> Source: https://learn.microsoft.com/en-us/graph/api/resources/privilegedaccessgroup?view=graph-rest-1.0  
> Microsoft doc last updated: 07/22/2024


Namespace: microsoft.graph

The entry point for all resources related to Privileged Identity Management (PIM) for groups.

Inherits from [entity](../resources/entity.md).

## Methods
None.

## Properties
|Property|Type|Description|
|:---|:---|:---|
|id|String|The unique identifier of an object in PIM governance for a group. Inherited from [entity](../resources/entity.md).|

## Relationships
|Relationship|Type|Description|
|:---|:---|:---|
|assignmentScheduleInstances|[privilegedAccessGroupAssignmentScheduleInstance](../resources/privilegedaccessgroupassignmentscheduleinstance.md) collection|The instances of assignment schedules to activate a just-in-time access.|
|assignmentScheduleRequests|[privilegedAccessGroupAssignmentScheduleRequest](../resources/privilegedaccessgroupassignmentschedulerequest.md) collection|The schedule requests for operations to create, update, delete, extend, and renew an assignment.|
|assignmentSchedules|[privilegedAccessGroupAssignmentSchedule](../resources/privilegedaccessgroupassignmentschedule.md) collection|The assignment schedules to activate a just-in-time access.|
|eligibilityScheduleInstances|[privilegedAccessGroupEligibilityScheduleInstance](../resources/privilegedaccessgroupeligibilityscheduleinstance.md) collection|The instances of eligibility schedules to activate a just-in-time access.|
|eligibilityScheduleRequests|[privilegedAccessGroupEligibilityScheduleRequest](../resources/privilegedaccessgroupeligibilityschedulerequest.md) collection|The schedule requests for operations to create, update, delete, extend, and renew an eligibility.|
|eligibilitySchedules|[privilegedAccessGroupEligibilitySchedule](../resources/privilegedaccessgroupeligibilityschedule.md) collection|The eligibility schedules to activate a just-in-time access.|

## JSON representation
The following JSON representation shows the resource type.

``` json
{
  "@odata.type": "#microsoft.graph.privilegedAccessGroup",
  "id": "String (identifier)"
}
```
