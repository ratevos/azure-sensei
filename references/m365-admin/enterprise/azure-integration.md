# Azure integration with Microsoft 365

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/azure-integration  
> Microsoft doc last updated: 08/26/2025


*This article applies to both Microsoft 365 Enterprise and Office 365 Enterprise.*

Microsoft 365 uses Microsoft Entra ID to manage user identities behind the scenes. Your Microsoft 365 subscription includes a free Microsoft Entra subscription. You can integrate your on-premises Active Directory Domain Services (AD DS) to synchronize user accounts and passwords or set up single sign-on. You can also purchase advanced features to better manage your accounts.
  
Microsoft Entra ID also offers other functionality, like managing custom apps, that you can use to extend and customize your Microsoft 365 subscriptions.
  
You can use the Microsoft Entra deployment advisors for a guided setup and configuration experience in the Microsoft 365 admin center (you must be signed in to Microsoft 365):

- [Microsoft Entra Connect advisor](https://aka.ms/aadconnectpwsync)
- [AD FS deployment advisor](https://aka.ms/adfsguidance)
- [Microsoft Entra setup guide](https://aka.ms/aadpguidance)
  
> [!NOTE]
> Microsoft 365 Local – run productivity and collaboration solutions on Azure Local through a specific reference architecture validated by Microsoft and supported by a network of partners. [Learn more](https://aka.ms/MSFTSovereignCloudBlog).

<a name='azure-ad-editions-and-microsoft-365-identity-management'></a>

## Microsoft Entra editions and Microsoft 365 identity management

If you have a paid subscription to Microsoft 365, you also have a free Microsoft Entra subscription. You can use Microsoft Entra ID to create and manage user and group accounts. To activate this subscription, you have to complete a one-time registration. Afterward, you can access Microsoft Entra ID from your Microsoft 365 admin center.

For instructions to register your free Microsoft Entra subscription, see [use your free Microsoft Entra subscription](https://learn.microsoft.com/en-us/microsoft-365/compliance/use-your-free-azure-ad-subscription-in-office-365). Don't go directly to azure.microsoft.com to sign up because you'll get a trial or paid subscription to Microsoft Azure that is separate from your free Microsoft Entra subscription with Microsoft 365.
  
With the free subscription you can synchronize with on-premises directories, set up single sign-on, and synchronize with many SaaS applications, such as Salesforce, Dropbox, and many more.
  
If you want enhanced AD DS functionality, bi-directional synchronization, and other management capabilities, you can upgrade your free subscription to a paid premium subscription. For the details, see [Microsoft Entra editions](https://azure.microsoft.com/pricing/details/active-directory/).
  
For more information about Microsoft 365 and Microsoft Entra ID, see [Microsoft 365 identity models](https://learn.microsoft.com/en-us/microsoft-365/enterprise/deploy-identity-solution-identity-model).
  
## Extend the capabilities of your Microsoft 365 tenant

|**Feature**|**Description**|
|:-----|:-----|
|Custom apps  <br/> |You can grant individual apps access to your Microsoft 365 data, such as mail, calendars, contacts, users, groups, files, and folders. You can also authorize these apps at the **Microsoft Entra DC admin** level and make them available to your entire company by registering the apps in Microsoft Entra ID. For more information, see [Custom Apps and Microsoft Entra ID for Microsoft 365 administrators](https://learn.microsoft.com/en-us/microsoft-365/enterprise/integrated-apps-and-azure-ads).<br/> For more information, see [About admin roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles?). <br/> Also see [Single sign-on](https://learn.microsoft.com/en-us/azure/active-directory/manage-apps/what-is-single-sign-on).  <br/> |
|Power Apps  <br/> | Power Apps are focused apps for mobile devices that can connect to your existing data sources like SharePoint lists and other data apps. See [Create a Power App for a list in SharePoint Online](https://support.office.com/article/9338b2d2-67ac-4b81-8e67-97da27e5e9ab) and the [Power Apps page](https://powerapps.microsoft.com/) for details.  <br/> |

## See also

[Microsoft 365 Enterprise overview](https://learn.microsoft.com/en-us/microsoft-365/enterprise/microsoft-365-overview)
