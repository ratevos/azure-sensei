# Connect to Microsoft 365 Government Community Cloud (GCC) data with Usage Analytics

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/connect-to-gcc-data-with-usage-analytics  
> Microsoft doc last updated: 07/26/2021


Use the following procedures to connect to your data with the Microsoft 365 Usage Analytics report in a Microsoft 365 Government Community Cloud (GCC) tenant.

> [!NOTE]
> These instructions are specifically for Microsoft 365 GCC tenants and aren't applicate to GCC High and DOD.

## Before you begin

To initially configure Microsoft 365 Usage Analytics:

- You must be a Microsoft 365 Global Administrator to enable data collection.
  
> [!IMPORTANT]
>
> Microsoft recommends that you use roles with the fewest permissions. Using roles with the fewest permissions helps improve security for your organization. Global Administrator is a highly privileged role that should be limited to emergency scenarios when you can't use an existing role. For more information, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

- You must have the [Power BI Desktop](https://powerbi.microsoft.com/desktop/) application to use the template file.
- You must have a [Power BI Pro license](https://go.microsoft.com/fwlink/p/?linkid=845347) or Premium capacity to publish and view the report.

## Step 1: Make your organization’s data available for the Microsoft 365 Usage Analytics report

1. In the Microsoft 365 admin center, expand the navigation menu, select **Reports**, then select **Usage**.
2. On the **Usage Reports** page, in the Microsoft 365 Usage Analytics section, select **Get Started**.
3. Under **Enable Power BI for usage analytics**, select **Make organizational usage data available to Microsoft usage analytics for Power BI**, and then select **Save**.

    

    This starts a process to make your organizations data accessible for this report, and you might see a message that states **We’re getting your data ready for Microsoft 365 usage analytics**. This process can take 24 hours to complete.

4. When your organizations data is ready, refreshing the page shows a message stating that your data is now available, and provides your **tenant ID** number. You must use the tenant ID in a later step when you attempt to connect to your tenant data.

    

    > [!IMPORTANT]
    > When your data is available, don't select **Go to Power BI**, which takes you to the Power BI Marketplace. The template app for this report required by GCC tenants isn't available in the Power BI Marketplace.  

## Step 2: Download the Power BI template, connect to your data, and publish the report

Microsoft 365 GCC users can download and use the Microsoft 365 Usage Analytics report template file to connect to their data. You would need Power BI Desktop to open and use the template file.

 > [!NOTE]
 > Currently, a template app for the Microsoft 365 Usage Analytics report isn't available for GCC tenants in the Power BI Marketplace.  

1. After downloading the [Power BI template](https://download.microsoft.com/download/7/8/2/782ba8a7-8d89-4958-a315-dab04c3b620c/Microsoft%20365%20Usage%20Analytics.pbit), open it using Power BI Desktop.
2. When prompted for a **TenantID**, enter the tenant ID you received when you prepared your organization’s data for this report in step 1. Then select **Load**. It can take several minutes for your data to load.

    

3. When loading completes, your report is displayed, and you see an executive summary of your data.

    

4. Save your changes to the report. 
5. Select **Publish** in the Power BI Desktop menu to publish the report to the Power BI Online service where it can be viewed. This requires either a Power BI Pro license or Power BI Premium capacity. As part of the [publish process](https://learn.microsoft.com/en-us/power-bi/create-reports/desktop-upload-desktop-files#to-publish-a-power-bi-desktop-dataset-and-reports), you must select a destination to publish to an available workspace in the Power BI Online Service.

## Related content

[About usage analytics](https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/usage-analytics) </br>
[Get the latest version of usage analytics](https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/get-the-latest-version-of-usage-analytics) </br>
[Navigate and utilize the reports in Microsoft 365 usage analytics](https://learn.microsoft.com/en-us/microsoft-365/admin/usage-analytics/navigate-and-utilize-reports) </br>
