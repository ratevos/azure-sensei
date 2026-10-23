# az aks maintenanceconfiguration

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/maintenanceconfiguration  
> Microsoft doc last updated: unknown

Commands to manage maintenance configurations in managed Kubernetes cluster.

> > [!NOTE]
> This command group has commands that are defined in both Azure CLI and at least one extension. Install each extension to benefit from its extended capabilities. [Learn more](https://learn.microsoft.com/cli/azure/azure-cli-extensions-overview) about extensions.

Subgroups and commands: `az_aks_maintenanceconfiguration_add`, `az_aks_maintenanceconfiguration_add(aks-preview)`, `az_aks_maintenanceconfiguration_delete`, `az_aks_maintenanceconfiguration_delete(aks-preview)`, `az_aks_maintenanceconfiguration_list`, `az_aks_maintenanceconfiguration_list(aks-preview)`, `az_aks_maintenanceconfiguration_show`, `az_aks_maintenanceconfiguration_show(aks-preview)`, `az_aks_maintenanceconfiguration_update`, `az_aks_maintenanceconfiguration_update(aks-preview)`

## az aks maintenanceconfiguration add

Add a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — The maintenance configuration json file.
- `--day-of-month` — Specify on which day of the month the maintenance occurs. E.g. 1 indicates the 1st of the month. Applicable to absolute monthly schedule type only. Not applicable to default maintenance configuration.
- `--day-of-week` — Specify on which day of the week the maintenance occurs. E.g. "Monday". Applicable to weekly and relative monthly schedule types.
- `--duration` — The length of maintenance window range from 4 to 24 hours.
- `--interval-days` — The number of days between each set of occurrences for daily schedule type. Not applicable to default maintenance configuration.
- `--interval-months` — The number of months between each set of occurrences. Applicable to absolute and relative monthly schedule types. Not applicable to default maintenance configuration.
- `--interval-weeks` — The number of weeks between each set of occurrences. Applicable to weekly schedule types only. Cannot be specified for default maintenance configuration (the interval is always 1 week).
- `--schedule-type` — Choose either 'Daily', 'Weekly', 'AbsoluteMonthly' or 'RelativeMonthly' for your maintenance schedule. For default maintenance configuration, only 'Weekly' is supported.
- `--start-date` — The date the maintenance configuration activates. If not specified, the maintenance window will be active right away. Supported for all configuration types, including default.".
- `--start-hour` — The start of a 1-hour maintenance window, e.g. 1 means 1:00am-2:00am (legacy timeInWeek format, default config only). See examples for the maintenanceWindow alternative.
- `--start-time` — The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. '--utc-offset' applies to this field. For example, '02:00' with '--utc-offset +02:00' means UTC time '00:00'.
- `--utc-offset` — The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'. Supported for all configuration types, including default.
- `--week-index` — Specify on which instance of the allowed days specified in '--day-of-week' the maintenance occurs. Applicable to relative monthly schedule type only. Not applicable to default maintenance configuration.
- `--weekday` — A day in week on which maintenance is allowed (legacy timeInWeek format, default config only). See examples for the maintenanceWindow alternative.

*Add default maintenance configuration with --weekday and --start-hour.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --weekday Monday  --start-hour 1
  The maintenance is allowed on Monday 1:00am to 2:00am
```

*Add default maintenance configuration with --weekday. The maintenance is allowd on any time of that day.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --weekday Monday
  The maintenance is allowed on Monday.
```

*Add default maintenance configuration with maintenance configuration json file*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on UTC time Tuesday 1:00am - 3:00 am and Wednesday 1:00am - 2:00am, 6:00am-7:00am
    No maintenance is allowed from 2020-11-26T03:00:00Z to 2020-11-30T12:00:00Z and from 2020-12-26T03:00:00Z to 2020-12-26T12:00:00Z even if they are allowed in the above weekly setting
    {
          "timeInWeek": [
            {
              "day": "Tuesday",
              "hourSlots": [
                1,
                2
              ]
            },
            {
              "day": "Wednesday",
              "hourSlots": [
                1,
                6
              ]
            }
          ],
          "notAllowedTime": [
            {
              "start": "2021-11-26T03:00:00Z",
              "end": "2021-11-30T12:00:00Z"
            },
            {
              "start": "2021-12-26T03:00:00Z",
              "end": "2021-12-26T12:00:00Z"
            }
          ]
  }
```

*Add default maintenance configuration with weekly maintenanceWindow schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --schedule-type Weekly --day-of-week Monday --duration 4 --start-time 09:00
  The maintenance is allowed on Monday from 09:00 to 13:00 (UTC) every week. Use --utc-offset to adjust the timezone and --start-date to set an activation date.
```

*Add aksManagedNodeOSUpgradeSchedule maintenance configuration with daily schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Daily --interval-days 2 --duration 12 --utc-offset=-08:00 --start-date 2023-01-16 --start-time 00:00
  The maintenance is allowed from 00:00 to 12:00 (adjusted with UTC offset: -08:00) every two days, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedNodeOSUpgradeSchedule maintenance configuration with weekly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Weekly --day-of-week Friday --interval-weeks 3 --duration 8 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on Friday from 09:30 to 17:30 (adjusted with UTC offset: +05:30) every three weeks, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with absolute monthly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type AbsoluteMonthly --day-of-month 15 --interval-months 1 --duration 6 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the 15th of the month from 09:30 to 15:30 (adjusted with UTC offset: +05:30) every month, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with relative monthly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type RelativeMonthly --day-of-week Tuesday --week-index Last --interval-months 3 --duration 6 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the last Tuesday from 09:30 to 15:30 in default UTC time every 3 months, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with json file.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on the 1st of the month from 09:00 to 13:00 (adjusted with UTC offset: -08:00) every 3 months, and this configuration will be effective from 2023-01-16.
    No maintenance is allowed from 2022-12-23 to 2023-01-05 and from 2023-11-23 to 2023-11-26 even if they are allowed in the above monthly setting
    {
        "maintenanceWindow": {
            "schedule": {
                "absoluteMonthly": {
                    "intervalMonths": 3,
                    "dayOfMonth": 1
                }
            },
            "durationHours": 4,
            "utcOffset": "-08:00",
            "startTime": "09:00",
            "notAllowedDates": [
                {
                    "start": "2022-12-23",
                    "end": "2023-01-05"
                },
                {
                    "start": "2023-11-23",
                    "end": "2023-11-26"
                }
            ]
        }
    }
```

## az aks maintenanceconfiguration add  (extension: aks-preview etc.)

Add a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — The maintenance configuration json file.
- `--day-of-month` — Specify on which day of the month the maintenance occurs. E.g. 1 indicates the 1st of the month. Applicable to absolute monthly schedule type only.
- `--day-of-week` — Specify on which day of the week the maintenance occurs. E.g. "Monday". Applicable to weekly and relative monthly schedule types.
- `--duration` — The length of maintenance window range from 4 to 24 hours.
- `--interval-days` — The number of days between each set of occurrences for daily schedule type.
- `--interval-months` — The number of months between each set of occurrences. Applicable to absolute and relative monthly schedule types.
- `--interval-weeks` — The number of weeks between each set of occurrences. Applicable to weekly schedule types only.
- `--maintenance-window-id` — Resource ID of a shared MaintenanceWindow resource to link this maintenance configuration to. When set, the schedule lives in the referenced MaintenanceWindow and inline schedule arguments cannot be used. Cannot be combined with --config-file (set the maintenanceWindowId property in the JSON instead
- `--schedule-type` — Choose either 'Daily', 'Weekly', 'AbsoluteMonthly' or 'RelativeMonthly' for your maintenance schedule. Only applicable to 'aksManagedAutoUpgradeSchedule' and 'aksManagedNodeOSUpgradeSchedule' maintenance configuration.
- `--start-date` — The date the maintenance configuration activates. If not specified, the maintenance window will be active right away.".
- `--start-hour` — The start time of 1 hour window which maintenance is allowd. E.g. 1 means it's allowd between 1:00 am and 2:00 am. Applicable to default maintenance configuration only.
- `--start-time` — The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. '--utc-offset' applies to this field. For example, '02:00' with '--utc-offset +02:00' means UTC time '00:00'.
- `--utc-offset` — The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'.
- `--week-index` — Specify on which instance of the allowed days specified in '--day-of-week' the maintenance occurs. Applicable to relative monthly schedule type only.
- `--weekday` — A day in week on which maintenance is allowed. E.g. Monday. Applicable to default maintenance configuration only.

*Add default maintenance configuration with --weekday and --start-hour.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --weekday Monday  --start-hour 1
  The maintenance is allowed on Monday 1:00am to 2:00am
```

*Add default maintenance configuration with --weekday. The maintenance is allowd on any time of that day.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --weekday Monday
  The maintenance is allowed on Monday.
```

*Add default maintenance configuration with maintenance configuration json file*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n default --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on UTC time Tuesday 1:00am - 3:00 am and Wednesday 1:00am - 2:00am, 6:00am-7:00am
    No maintenance is allowed from 2020-11-26T03:00:00Z to 2020-11-30T12:00:00Z and from 2020-12-26T03:00:00Z to 2020-12-26T12:00:00Z even if they are allowed in the above weekly setting
    {
          "timeInWeek": [
            {
              "day": "Tuesday",
              "hourSlots": [
                1,
                2
              ]
            },
            {
              "day": "Wednesday",
              "hourSlots": [
                1,
                6
              ]
            }
          ],
          "notAllowedTime": [
            {
              "start": "2021-11-26T03:00:00Z",
              "end": "2021-11-30T12:00:00Z"
            },
            {
              "start": "2021-12-26T03:00:00Z",
              "end": "2021-12-26T12:00:00Z"
            }
          ]
  }
```

*Add aksManagedNodeOSUpgradeSchedule maintenance configuration with daily schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Daily --interval-days 2 --duration 12 --utc-offset=-08:00 --start-date 2023-01-16 --start-time 00:00
  The maintenance is allowed from 00:00 to 12:00 (adjusted with UTC offset: -08:00) every two days, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedNodeOSUpgradeSchedule maintenance configuration with weekly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Weekly --day-of-week Friday --interval-weeks 3 --duration 8 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on Friday from 09:30 to 17:30 (adjusted with UTC offset: +05:30) every three weeks, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with absolute monthly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type AbsoluteMonthly --day-of-month 15 --interval-months 1 --duration 6 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the 15th of the month from 09:30 to 15:30 (adjusted with UTC offset: +05:30) every month, and this configuration will be effective from 2023-01-16.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with relative monthly schedule.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type RelativeMonthly --day-of-week Tuesday --week-index Last --interval-months 3 --duration 6 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the last Tuesday from 09:30 to 15:30 in default UTC time every 3 months, and this configuration will be effective from 2023-01-16.
```

*Link a maintenance configuration to a shared MaintenanceWindow resource.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --maintenance-window-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.ContainerService/maintenanceWindows/myWindow
  The schedule lives in the referenced MaintenanceWindow resource and is shared across configurations. Inline schedule arguments cannot be combined with --maintenance-window-id.
```

*Add aksManagedAutoUpgradeSchedule maintenance configuration with json file.*
```azurecli
az aks maintenanceconfiguration add -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on the 1st of the month from 09:00 to 13:00 (adjusted with UTC offset: -08:00) every 3 months, and this configuration will be effective from 2023-01-16.
    No maintenance is allowed from 2022-12-23 to 2023-01-05 and from 2023-11-23 to 2023-11-26 even if they are allowed in the above monthly setting
    {
        "maintenanceWindow": {
            "schedule": {
                "absoluteMonthly": {
                    "intervalMonths": 3,
                    "dayOfMonth": 1
                }
            },
            "durationHours": 4,
            "utcOffset": "-08:00",
            "startTime": "09:00",
            "notAllowedDates": [
                {
                    "start": "2022-12-23",
                    "end": "2023-01-05"
                },
                {
                    "start": "2023-11-23",
                    "end": "2023-11-26"
                }
            ]
        }
    }
```

## az aks maintenanceconfiguration delete

Delete a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks maintenanceconfiguration delete  (extension: aks-preview etc.)

Delete a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.

## az aks maintenanceconfiguration list

List maintenance configurations in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenanceconfiguration list  (extension: aks-preview etc.)

List maintenance configurations in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenanceconfiguration show

Show the details of a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenanceconfiguration show  (extension: aks-preview etc.)

Show the details of a maintenance configuration in managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenanceconfiguration update

Update a maintenance configuration of a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — The maintenance configuration json file.
- `--day-of-month` — Specify on which day of the month the maintenance occurs. E.g. 1 indicates the 1st of the month. Applicable to absolute monthly schedule type only. Not applicable to default maintenance configuration.
- `--day-of-week` — Specify on which day of the week the maintenance occurs. E.g. "Monday". Applicable to weekly and relative monthly schedule types.
- `--duration` — The length of maintenance window range from 4 to 24 hours.
- `--interval-days` — The number of days between each set of occurrences for daily schedule type. Not applicable to default maintenance configuration.
- `--interval-months` — The number of months between each set of occurrences. Applicable to absolute and relative monthly schedule types. Not applicable to default maintenance configuration.
- `--interval-weeks` — The number of weeks between each set of occurrences. Applicable to weekly schedule types only. Cannot be specified for default maintenance configuration (the interval is always 1 week).
- `--schedule-type` — Choose either 'Daily', 'Weekly', 'AbsoluteMonthly' or 'RelativeMonthly' for your maintenance schedule. For default maintenance configuration, only 'Weekly' is supported.
- `--start-date` — The date the maintenance configuration activates. If not specified, the maintenance window will be active right away. Supported for all configuration types, including default.".
- `--start-hour` — The start of a 1-hour maintenance window, e.g. 1 means 1:00am-2:00am (legacy timeInWeek format, default config only). See examples for the maintenanceWindow alternative.
- `--start-time` — The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. '--utc-offset' applies to this field. For example, '02:00' with '--utc-offset +02:00' means UTC time '00:00'.
- `--utc-offset` — The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'. Supported for all configuration types, including default.
- `--week-index` — Specify on which instance of the allowed days specified in '--day-of-week' the maintenance occurs. Applicable to relative monthly schedule type only. Not applicable to default maintenance configuration.
- `--weekday` — A day in week on which maintenance is allowed (legacy timeInWeek format, default config only). See examples for the maintenanceWindow alternative.

*Update default maintenance configuration with --weekday and --start-hour.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --weekday Monday  --start-hour 1
  The maintenance is allowed on Monday 1:00am to 2:00am
```

*Update default maintenance configuration with --weekday.The maintenance is allowd on any time of that day.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --weekday Monday
  The maintenance is allowed on Monday.
```

*Update default maintenance configuration with maintenance configuration json file*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on UTC time Tuesday 1:00am - 3:00 am and Wednesday 1:00am - 2:00am, 6:00am-7:00am
    No maintenance is allowed from 2020-11-26T03:00:00Z to 2020-11-30T12:00:00Z and from 2020-12-26T03:00:00Z to 2020-12-26T12:00:00Z even if they are allowed in the above weekly setting
    {
          "timeInWeek": [
            {
              "day": "Tuesday",
              "hourSlots": [
                1,
                2
              ]
            },
            {
              "day": "Wednesday",
              "hourSlots": [
                1,
                6
              ]
            }
          ],
          "notAllowedTime": [
            {
              "start": "2021-11-26T03:00:00Z",
              "end": "2021-11-30T12:00:00Z"
            },
            {
              "start": "2021-12-26T03:00:00Z",
              "end": "2021-12-26T12:00:00Z"
            }
          ]
  }
```

*Update default maintenance configuration with weekly maintenanceWindow schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --schedule-type Weekly --day-of-week Monday --duration 4 --start-time 09:00
  The maintenance is allowed on Monday from 09:00 to 13:00 (UTC) every week. Use --utc-offset to adjust the timezone and --start-date to set an activation date.
```

*Update aksManagedNodeOSUpgradeSchedule maintenance configuration with daily schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Daily --interval-days 2 --duration 12 --utc-offset=-08:00 --start-date 2023-01-16 --start-time 00:00
  The maintenance is allowed from 00:00 to 12:00 (adjusted with UTC offset: -08:00) every two days. This configuration will be effective from 2023-01-16.
```

*Update aksManagedNodeOSUpgradeSchedule maintenance configuration with weekly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Weekly --day-of-week Friday --interval-weeks 3 --duration 8 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on Friday from 09:30 to 17:30 (adjusted with UTC offset: +05:30) every three weeks. This configuration will be effective from 2023-01-16.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with absolute monthly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type AbsoluteMonthly --day-of-month 15 --interval-months 1 --duration 6 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the 15th of the month from 09:30 to 15:30 (adjusted with UTC offset: +05:30) every month. This configuration will be effective from 2023-01-16.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with relative monthly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type RelativeMonthly --day-of-week Tuesday --week-index Last --interval-months 3 --duration 6 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the last Tuesday from 09:30 to 15:30 in default UTC time every 3 months. This configuration will be effective from 2023-01-16.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with json file.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on the 1st of the month from 09:00 to 13:00 (adjusted with UTC offset: -08:00) every 3 months, and this configuration will be effective from 2023-01-16.
    No maintenance is allowed from 2022-12-23 to 2023-01-05 and from 2023-11-23 to 2023-11-26 even if they are allowed in the above monthly setting
    {
        "maintenanceWindow": {
            "schedule": {
                "absoluteMonthly": {
                    "intervalMonths": 3,
                    "dayOfMonth": 1
                }
            },
            "durationHours": 4,
            "utcOffset": "-08:00",
            "startTime": "09:00",
            "notAllowedDates": [
                {
                    "start": "2022-12-23",
                    "end": "2023-01-05"
                },
                {
                    "start": "2023-11-23",
                    "end": "2023-11-26"
                }
            ]
        }
    }
```

## az aks maintenanceconfiguration update  (extension: aks-preview etc.)

Update a maintenance configuration of a managed Kubernetes cluster.

**Required parameters**

- `--cluster-name` — The cluster name.
- `--name -n` — The config name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — The maintenance configuration json file.
- `--day-of-month` — Specify on which day of the month the maintenance occurs. E.g. 1 indicates the 1st of the month. Applicable to absolute monthly schedule type only.
- `--day-of-week` — Specify on which day of the week the maintenance occurs. E.g. "Monday". Applicable to weekly and relative monthly schedule types.
- `--duration` — The length of maintenance window range from 4 to 24 hours.
- `--interval-days` — The number of days between each set of occurrences for daily schedule type.
- `--interval-months` — The number of months between each set of occurrences. Applicable to absolute and relative monthly schedule types.
- `--interval-weeks` — The number of weeks between each set of occurrences. Applicable to weekly schedule types only.
- `--maintenance-window-id` — Resource ID of a shared MaintenanceWindow resource to link this maintenance configuration to. When set, the schedule lives in the referenced MaintenanceWindow and inline schedule arguments cannot be used. Cannot be combined with --config-file (set the maintenanceWindowId property in the JSON instead
- `--schedule-type` — Choose either 'Daily', 'Weekly', 'AbsoluteMonthly' or 'RelativeMonthly' for your maintenance schedule. Only applicable to 'aksManagedAutoUpgradeSchedule' and 'aksManagedNodeOSUpgradeSchedule' maintenance configuration.
- `--start-date` — The date the maintenance configuration activates. If not specified, the maintenance window will be active right away.".
- `--start-hour` — The start time of 1 hour window which maintenance is allowd. E.g. 1 means it's allowd between 1:00 am and 2:00 am. Applicable to default maintenance configuration only.
- `--start-time` — The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. '--utc-offset' applies to this field. For example, '02:00' with '--utc-offset +02:00' means UTC time '00:00'.
- `--utc-offset` — The UTC offset in format +/-HH:mm. For example, '+05:30' for IST and '-07:00' for PST. If not specified, the default is '+00:00'.
- `--week-index` — Specify on which instance of the allowed days specified in '--day-of-week' the maintenance occurs. Applicable to relative monthly schedule type only.
- `--weekday` — A day in week on which maintenance is allowed. E.g. Monday. Applicable to default maintenance configuration only.

*Update default maintenance configuration with --weekday and --start-hour.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --weekday Monday  --start-hour 1
  The maintenance is allowed on Monday 1:00am to 2:00am
```

*Update default maintenance configuration with --weekday.The maintenance is allowd on any time of that day.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --weekday Monday
  The maintenance is allowed on Monday.
```

*Update default maintenance configuration with maintenance configuration json file*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n default --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on UTC time Tuesday 1:00am - 3:00 am and Wednesday 1:00am - 2:00am, 6:00am-7:00am
    No maintenance is allowed from 2020-11-26T03:00:00Z to 2020-11-30T12:00:00Z and from 2020-12-26T03:00:00Z to 2020-12-26T12:00:00Z even if they are allowed in the above weekly setting
    {
          "timeInWeek": [
            {
              "day": "Tuesday",
              "hourSlots": [
                1,
                2
              ]
            },
            {
              "day": "Wednesday",
              "hourSlots": [
                1,
                6
              ]
            }
          ],
          "notAllowedTime": [
            {
              "start": "2021-11-26T03:00:00Z",
              "end": "2021-11-30T12:00:00Z"
            },
            {
              "start": "2021-12-26T03:00:00Z",
              "end": "2021-12-26T12:00:00Z"
            }
          ]
  }
```

*Update aksManagedNodeOSUpgradeSchedule maintenance configuration with daily schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Daily --interval-days 2 --duration 12 --utc-offset=-08:00 --start-date 2023-01-16 --start-time 00:00
  The maintenance is allowed from 00:00 to 12:00 (adjusted with UTC offset: -08:00) every two days. This configuration will be effective from 2023-01-16.
```

*Update aksManagedNodeOSUpgradeSchedule maintenance configuration with weekly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedNodeOSUpgradeSchedule --schedule-type Weekly --day-of-week Friday --interval-weeks 3 --duration 8 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on Friday from 09:30 to 17:30 (adjusted with UTC offset: +05:30) every three weeks. This configuration will be effective from 2023-01-16.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with absolute monthly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type AbsoluteMonthly --day-of-month 15 --interval-months 1 --duration 6 --utc-offset +05:30 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the 15th of the month from 09:30 to 15:30 (adjusted with UTC offset: +05:30) every month. This configuration will be effective from 2023-01-16.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with relative monthly schedule.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --schedule-type RelativeMonthly --day-of-week Tuesday --week-index Last --interval-months 3 --duration 6 --start-date 2023-01-16 --start-time 09:30
  The maintenance is allowed on the last Tuesday from 09:30 to 15:30 in default UTC time every 3 months. This configuration will be effective from 2023-01-16.
```

*Link a maintenance configuration to a shared MaintenanceWindow resource.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --maintenance-window-id /subscriptions/00000000-0000-0000-0000-000000000000/resourceGroups/MyResourceGroup/providers/Microsoft.ContainerService/maintenanceWindows/myWindow
  The schedule lives in the referenced MaintenanceWindow resource and is shared across configurations. Inline schedule arguments cannot be combined with --maintenance-window-id.
```

*Update aksManagedAutoUpgradeSchedule maintenance configuration with json file.*
```azurecli
az aks maintenanceconfiguration update -g MyResourceGroup --cluster-name test1 -n aksManagedAutoUpgradeSchedule --config-file ./test.json
    The content of json file looks below. It means the maintenance is allowed on the 1st of the month from 09:00 to 13:00 (adjusted with UTC offset: -08:00) every 3 months, and this configuration will be effective from 2023-01-16.
    No maintenance is allowed from 2022-12-23 to 2023-01-05 and from 2023-11-23 to 2023-11-26 even if they are allowed in the above monthly setting
    {
        "maintenanceWindow": {
            "schedule": {
                "absoluteMonthly": {
                    "intervalMonths": 3,
                    "dayOfMonth": 1
                }
            },
            "durationHours": 4,
            "utcOffset": "-08:00",
            "startTime": "09:00",
            "notAllowedDates": [
                {
                    "start": "2022-12-23",
                    "end": "2023-01-05"
                },
                {
                    "start": "2023-11-23",
                    "end": "2023-11-26"
                }
            ]
        }
    }
```
