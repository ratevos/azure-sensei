# Automatic Service Health Incident Creation

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-incidents  
> Microsoft doc last updated: 04/28/2025


> [!IMPORTANT]
> Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

The Microsoft 365 support integration app enables you to create ServiceNow incidents when a Microsoft Service Health Incident is published for your tenant. To use this feature, you must use version 2.1.0 or later. This feature helps IT teams by automatically creating incidents in ServiceNow when Microsoft publishes new service health incidents.

> [!NOTE]
> This article was partially generated using Azure OpenAI Service. Before publishing, an author reviewed and revised the content as needed. See [Our principles for using AI-generated content in Microsoft Learn](https://aka.ms/ai-content-principles).

When a Microsoft Service Health Incident is updated, the app posts the same updates to the ServiceNow incident. You can choose to have the app automatically close the ServiceNow incident when the Microsoft service health incident is resolved, or you can close it manually.

The properties on the Microsoft service health incident map to properties on the ServiceNow incident.

| Microsoft Service Health | ServiceNow Incident |
| --- | --- |
| Title | Short Description |
| Issue type | Impact |
| Status | Urgency |
| All other fields | Description |

## Configuration

To enable automatic creation of ServiceNow incidents, navigate to **Microsoft 365 Support** > **Service Health** in your ServiceNow instance.

Select **Enable the Microsoft 365 support integration app to create ServiceNow incidents for each Microsoft 365 service health incident**.

To automatically close ServiceNow incidents, select **Automatically resolve ServiceNow incident when the Microsoft service health is resolved**.

If the ServiceNow incident is manually closed and this setting is enabled, the app stops posting updates to that incident.

If the ServiceNow incident is automatically resolved, the app stops posting updates to that incident. The ServiceNow incident is resolved with the following settings:

- Resolution code: **Closed/Resolved by Caller**
- Resolution note: **The Microsoft service health incident was resolved on <date_time>. Please refer to the incident details in the Microsoft 365 Support tab for more information.**

To automatically create ServiceNow incidents, configure the **Assignment group** and **Category** for the app. The **Assigned to** and **Subcategory** aren't required. Setting those values improves routing and reporting.
