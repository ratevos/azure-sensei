# az aks maintenancewindow

> Source: https://learn.microsoft.com/en-us/cli/azure/aks/maintenancewindow  
> Microsoft doc last updated: unknown

Commands to manage MaintenanceWindow peer ARM resources.

Subgroups and commands: `az_aks_maintenancewindow_create`, `az_aks_maintenancewindow_delete`, `az_aks_maintenancewindow_list`, `az_aks_maintenancewindow_show`, `az_aks_maintenancewindow_update`, `az_aks_maintenancewindow_wait`

## az aks maintenancewindow create  (extension: aks-preview etc.)

Create a MaintenanceWindow.

**Required parameters**

- `--name -n` — The maintenance window name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — Path to a JSON file describing the MaintenanceWindow body. Use when you need to set fields without dedicated flags (e.g. notAllowedDates / blackout date ranges).
- `--day-of-month` — Day of month the maintenance occurs. e.g. 15. AbsoluteMonthly schedule only.
- `--day-of-week` — Day of week the maintenance occurs. e.g. Monday. Weekly or RelativeMonthly schedules only.
- `--duration` — The length of the maintenance window in hours. Range 4-24.
- `--interval-days` — Number of days between occurrences. Daily schedule only.
- `--interval-months` — Number of months between occurrences. AbsoluteMonthly or RelativeMonthly schedules only.
- `--interval-weeks` — Number of weeks between occurrences. Weekly schedule only.
- `--location -l` — Location for the MaintenanceWindow. Defaults to the resource group's location when omitted.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--schedule-type` — Recurrence type. One of Daily, Weekly, AbsoluteMonthly or RelativeMonthly.
- `--start-date` — The date the maintenance window activates. e.g. 2026-06-01. If not specified, the window activates immediately.
- `--start-time` — The start time of the maintenance window. Accepted values are from '00:00' to '23:59'. --utc-offset applies to this field.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--utc-offset` — The UTC offset in format +/-HH:mm. For example, '+05:30' for IST or '-07:00' for PST. Default is '+00:00'.
- `--week-index` — Instance of the day-of-week the maintenance occurs (First, Second, Third, Fourth, Last). RelativeMonthly schedule only.

*Create a weekly Saturday window (the canonical "production weekends" shape).*
```azurecli
az aks maintenancewindow create -g rg-maintenance -n production-weekends -l eastus \
  --schedule-type Weekly --day-of-week Saturday --interval-weeks 1 \
  --start-time "02:00" --duration 8 --utc-offset=-07:00 \
  --tags environment=production
```

*Create a daily window every 2 days from a specific start date.*
```azurecli
az aks maintenancewindow create -g rg-maintenance -n nightly -l eastus \
  --schedule-type Daily --interval-days 2 \
  --start-date 2026-06-01 --start-time "00:00" --duration 6 --utc-offset=-08:00
```

*Create an absolute monthly window on the 15th.*
```azurecli
az aks maintenancewindow create -g rg-maintenance -n monthly-15 -l eastus \
  --schedule-type AbsoluteMonthly --day-of-month 15 --interval-months 1 \
  --start-time "09:30" --duration 6 --utc-offset=+05:30
```

*Create a relative monthly window on the last Friday.*
```azurecli
az aks maintenancewindow create -g rg-maintenance -n last-friday -l eastus \
  --schedule-type RelativeMonthly --day-of-week Friday --week-index Last --interval-months 1 \
  --start-time "01:00" --duration 4 --utc-offset=+00:00
```

*Create a weekly window with blackout dates via a config file.*
```azurecli
az aks maintenancewindow create -g rg-maintenance -n weekly-with-holidays -l eastus \
  --config-file ./mw-body.json
  The contents of mw-body.json:
  {
    "properties": {
      "schedule": { "weekly": { "intervalWeeks": 1, "dayOfWeek": "Saturday" } },
      "startTime": "02:00",
      "durationHours": 8,
      "utcOffset": "-07:00",
      "notAllowedDates": [
        { "start": "2026-12-23", "end": "2027-01-05" },
        { "start": "2026-07-04", "end": "2026-07-05" }
      ]
    }
  }
```

## az aks maintenancewindow delete  (extension: aks-preview etc.)

Delete a MaintenanceWindow.

**Required parameters**

- `--name -n` — The maintenance window name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--yes -y` — Do not prompt for confirmation. Default: False.

## az aks maintenancewindow list  (extension: aks-preview etc.)

List MaintenanceWindows in a resource group, or across the subscription if --resource-group is omitted.

**Optional parameters**

- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenancewindow show  (extension: aks-preview etc.)

Show a MaintenanceWindow.

**Required parameters**

- `--name -n` — The maintenance window name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

## az aks maintenancewindow update  (extension: aks-preview etc.)

Update a MaintenanceWindow.

**Required parameters**

- `--name -n` — The maintenance window name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--config-file` — Path to a JSON file describing the MaintenanceWindow body. When supplied, the JSON wholly defines the resource on create, or replaces the existing `properties` block on update. This is the only path that can set fields without dedicated flags (notAllowedDates, etc.).
- `--day-of-month` — Day of month the maintenance occurs for AbsoluteMonthly schedule.
- `--day-of-week` — Day of week the maintenance occurs for Weekly or RelativeMonthly schedule.
- `--duration` — The length of the maintenance window in hours. Range 4-24.
- `--interval-days` — The number of days between each set of occurrences for Daily schedule.
- `--interval-months` — The number of months between each set of occurrences for AbsoluteMonthly or RelativeMonthly schedule.
- `--interval-weeks` — The number of weeks between each set of occurrences for Weekly schedule.
- `--location -l` — Location. Values from: `az account list-locations`. You can configure the default location using `az configure --defaults location=<location>`.
- `--no-wait` — Do not wait for the long-running operation to finish. Default: False.
- `--schedule-type` — Recurrence type: Daily, Weekly, AbsoluteMonthly or RelativeMonthly.
- `--start-date` — The date the maintenance window activates. e.g. 2026-06-01.
- `--start-time` — The start time of the maintenance window. e.g. 09:30.
- `--tags` — Space-separated tags: key[=value] [key[=value] ...]. Use "" to clear existing tags.
- `--utc-offset` — The UTC offset in format +/-HH:mm. e.g. -08:00 or +05:30.
- `--week-index` — Instance of the weekday specified in --day-of-week the maintenance occurs for RelativeMonthly schedule.

*Update only tags (existing schedule is preserved).*
```azurecli
az aks maintenancewindow update -g rg-maintenance -n production-weekends --tags environment=staging
```

*Update only the schedule's day-of-week (existing duration / start-time / tags preserved).*
```azurecli
az aks maintenancewindow update -g rg-maintenance -n production-weekends \
  --schedule-type Weekly --day-of-week Sunday --interval-weeks 1
```

*Change duration only (existing schedule shape preserved).*
```azurecli
az aks maintenancewindow update -g rg-maintenance -n production-weekends --duration 6
```

*Replace blackout dates via a config file (preserves tags, location).*
```azurecli
az aks maintenancewindow update -g rg-maintenance -n production-weekends --config-file ./mw-body.json
  The contents of mw-body.json should include a complete properties block, e.g.:
  {
    "properties": {
      "schedule": { "weekly": { "intervalWeeks": 1, "dayOfWeek": "Saturday" } },
      "startTime": "02:00",
      "durationHours": 8,
      "utcOffset": "-07:00",
      "notAllowedDates": [ { "start": "2026-12-23", "end": "2027-01-05" } ]
    }
  }
```

## az aks maintenancewindow wait  (extension: aks-preview etc.)

Wait for a MaintenanceWindow to reach a desired state.

**Required parameters**

- `--name -n` — The maintenance window name.
- `--resource-group -g` — Name of resource group. You can configure the default group using `az configure --defaults group=<name>`.

**Optional parameters**

- `--acquire-policy-token` — Acquiring an Azure Policy token automatically for this resource operation.
- `--change-reference` — The related change reference ID for this resource operation.
- `--created` — Wait until created with 'provisioningState' at 'Succeeded'. Default: False.
- `--custom` — Wait until the condition satisfies a custom JMESPath query. E.g. provisioningState!='InProgress', instanceView.statuses[?code=='PowerState/running'].
- `--deleted` — Wait until deleted. Default: False.
- `--exists` — Wait until the resource exists. Default: False.
- `--interval` — Polling interval in seconds. Default: 30.
- `--timeout` — Maximum wait in seconds. Default: 3600.
- `--updated` — Wait until updated with provisioningState at 'Succeeded'. Default: False.

*Wait for a MaintenanceWindow to be created.*
```azurecli
az aks maintenancewindow wait -g rg-maintenance -n production-weekends --created
```
