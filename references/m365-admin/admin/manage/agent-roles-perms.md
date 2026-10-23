# Agent management roles and permissions in Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/agent-roles-perms  
> Microsoft doc last updated: 04/21/2026


Access to agent management in Microsoft 365 admin center is controlled by [Microsoft Entra admin roles](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference). 

While several administrative and security roles can view agent-related information for monitoring and reporting purposes, only select roles are authorized to perform governance actions such as approving agent requests or assigning ownership.

The following table provides agent management capabilities in the Microsoft 365 admin center:

| Role | View insights and organization   data | View agent registry information | Install, modify, approve, and manage agent configurations |
|:---:|:---:|:---:|:---:|
| Global Administrator | ✔ | ✔ | ✔ |
| AI Administrator | ✔ | ✔ | ✔ |
| Global Reader | ✔ | ✔ | ✖ |
| AI Reader | ✔ | ✔ | ✖ |
| Security Administrator | ✔ | ✔ | ✖ |
| Security Reader | ✔ | ✔ | ✖ |
| Security Operator | ✔ | ✔ | ✖ |
| Reports Reader | ✔ | ✔ | ✖ |
| User Experience Success Manager | ✔ | ✔ | ✖ |
| User Account Administrator | ✔ | ✖ | ✖ |

The **AI Administrator** and **Global Administrator** roles have tenant‑wide visibility and governance authority, where-as by contrast, product-specific admin roles allow governance only within the boundaries of their products (such as Power Platform Administrator and Fabric Administrator).

> [!IMPORTANT]
>
> Use and assign roles with the fewest permissions to accomplish tasks. Accounts with lower permission roles help improve security for your organization. Global Administrator is a highly privileged role. Limit its use to emergency scenarios when you can't use an existing role. For more information, see [About admin roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).

For more information about roles and permissions related to agents, see [About administrator roles in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
