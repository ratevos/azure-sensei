# Block Microsoft Publisher

> Source: https://learn.microsoft.com/en-us/microsoft-365/baseline-security-mode/block-microsoft-publisher  
> Microsoft doc last updated: 06/25/2025


As a Microsoft 365 admin, you want to protect and secure your business environment. **Baseline security mode** helps you protect and secure your organization.

Publisher has a large attack surface and won't be included in Microsoft 365 starting in October 2026. Blocking Publisher now reduces security risk and aligns with Microsoft’s support strategy.

When you enable this setting, Microsoft Publisher won't launch. When users try to launch Publisher, they get an error message “Publisher could not start because of a security policy set by your organization.”

If you've already enabled this setting but need to revert to the default behavior, you can turn off this setting directly in the Microsoft 365 admin center.

## Turn off setting in the Microsoft 365 admin center

1. Go to the Microsoft 365 admin center at <a href="https://go.microsoft.com/fwlink/p/?linkid=2024339" target="_blank">https://admin.cloud.microsoft</a> and select Org settings.
1. Select Baseline Security Mode, find the **Block Microsoft Publisher** setting, and switch the toggle to **Off**.

## Office Cloud Policy service

Alternatively, you can make changes to the policy setting directly using the [Office Cloud Policy service](https://config.office.com/). Set the **Disable Publisher** policy as not configured to revert to the default behavior.
