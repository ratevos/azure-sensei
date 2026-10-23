# Identity Governance dashboard

> Source: https://learn.microsoft.com/en-us/entra/id-governance/governance-dashboard  
> Microsoft doc last updated: 04/09/2025


In this article, we provide guidance on how to use the Microsoft Identity Governance dashboard. 

## About the dashboard
Microsoft Identity Governance dashboard discovers usage information about various Identity Governance & Administration (IGA) features configured in your tenant. It then gives you at-a-glance view of your current state of Identity Governance, with actionable buttons and quickly accessible links to feature documentation. 

## Using the dashboard

We understand that implementing Identity Governance is a journey, and you may be in different stages of this journey. 
* If you are just getting started, use the dashboard to assess the complexity of your IT landscape. Identify the number of users and guests in your tenant. Discover business apps and privileged roles in your tenant and review capabilities provided by Microsoft Identity Governance to put together an implementation plan that addresses your security & compliance needs.
* If you have already deployed certain governance capabilities, use the dashboard to understand the coverage of your governance automations and find implementation gaps. For example, maybe you have automated birthright access using [entitlement management](https://go.microsoft.com/fwlink/?linkid=2210375), but you have not set up periodic [access reviews](https://go.microsoft.com/fwlink/?linkid=2211313). Use the call-to-action links in the dashboard to further improve your identity governance posture.  

## Data displayed on the dashboard 
You can access the dashboard by logging into the Microsoft Entra admin center and selecting the "Dashboard" blade under "Identity Governance". 
The dashboard experience is made up of the following main components:
* **Glanceable cards**: These cards provide high level insights into what’s happening in your tenant from the perspective of workforce users, guest users, privileged identities, and application access governance. The navigation links in the glanceable cards point to Identity Governance quick start guides and tutorials.
* **Identity Governance status**: This visual shows your identity landscape in terms of number of employees, guests, business apps, groups, and privileged roles. It then highlights the various Microsoft Identity Governance feature sets configured to better govern these entities. If a feature is not configured, you can use the "Configure Now" option to open the configuration landing blade for that feature. 
* **Tutorials**: This section contains tutorials of popular Identity governance use cases for quick access.
* **Highlights**: Use the content in this section to stay informed about the latest Identity Governance features and learn how customers are using Identity Governance to improve their security and compliance posture. 

>[!NOTE]
>The Graph APIs on the dashboard will operate in the context of the logged in user using delegated permission model. To view the dashboard with full fidelity, we recommend at minimum using the Global Reader role. 

## Troubleshooting dashboard errors

You may see two types of errors on the dashboard: 

* **Service error**: This error indicates that the dashboard was unable to retrieve data due to a backend service error. The service error could be intermittent. Try refreshing the dashboard to see if the issue resolves automatically. If the issue persists, contact Microsoft support. 
* **Permission error**: This error indicates that the dashboard was unable to retrieve data either due to insufficient permissions or data access issues or license issues. Check the role assigned to the logged in user and ensure your tenant has the right license. To view the dashboard with full fidelity, at a minimum we recommend assigning the Global reader role. 

## Next steps

- [What are Lifecycle workflows?](https://learn.microsoft.com/en-us/entra/id-governance/what-are-lifecycle-workflows)
- [What are Microsoft Entra access reviews](https://learn.microsoft.com/en-us/entra/id-governance/access-reviews-overview)
- [What is Microsoft Entra entitlement management?](https://learn.microsoft.com/en-us/entra/id-governance/entitlement-management-overview)
- [What is Microsoft Entra Privileged Identity Management?](https://learn.microsoft.com/en-us/entra/id-governance/privileged-identity-management/pim-configure)
