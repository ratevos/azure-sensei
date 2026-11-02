# Troubleshoot the Global Secure Access Client: Disabled by Your Organization

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/troubleshoot-global-secure-access-client-disabled  
> Microsoft doc last updated: 03/23/2026

This document provides troubleshooting guidance for the Global Secure Access client. It explores how to resolve the **Global Secure Access client - disabled by your organization** error message.   

|Icon    |Message    |Description    |
|---------|---------|---------|
|	|Global Secure Access - disabled by your organization	|Your organization disabled the client (that is, all traffic forwarding profiles are disabled).    |

The **Global Secure Access client - disabled by your organization** error message appears when the Global Secure Access client is deliberately deactivated by your organization's administrator.   

The warning message also appears when the client receives an empty policy (that is, no traffic forwarding profiles from Microsoft, Private Access, or Internet Access).
The empty policy happens in the following cases:     
1. All traffic forwarding profiles are disabled in the portal. 
1. Some traffic forwarding profiles are enabled, but the user isn't assigned to any of them (in the **User and group assignments** section of each profile). 
1. The user didn't sign in to Windows with a Microsoft Entra user. 
1. Authentication to get the policy requires user interaction (such as if multifactor authentication (MFA) or terms of use (ToU) are enabled).    

In cases **3** and **4**, only traffic profiles that are assigned to the entire tenant (**Assign to all users** in the user and group assignment section is set to **Yes**) take effect. Traffic profiles assigned to specific users and groups aren't applied since the user identity isn't used to get the policy. In these cases, only the device identity is available to the policy service.   

To view the Global Secure Access traffic profile configuration:
1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as a [Global Secure Access Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-secure-access-administrator).
1. Navigate to **Global Secure Access** > **Connect** > **Traffic forwarding**.   

## Troubleshooting steps    
1. View the available traffic forwarding profiles. At least one traffic forwarding profile must be enabled. Verify that the user is assigned to the enabled traffic forwarding profile. Users in your organization who sign in to Windows with a non-Microsoft Entra ID, such as local user or Active Directory Domain Services (AD DS) user not synced to Microsoft Entra, receive only the traffic forwarding profiles assigned to all users in the tenant.
 

1. Ensure that both the device and the user are successfully authenticated to Microsoft Entra and receive a valid token. 
    1. Check that the device is joined to Microsoft Entra and signed in to Windows with a Microsoft Entra user. 
    1. Run the command `dsregcmd /status` and check the **AzureAdPrt** field.   

1. Check if a Conditional Access policy is blocking the user. Network blocks can arise from Conditional Access settings, an unmanaged or noncompliant device, or unfulfilled MFA or ToU policies. To confirm that the Global Secure Access Client authenticated successfully to the policy service, check the list of non-interactive user sign-ins.   

> [!NOTE]
> To get the policy, the Global Secure Access client uses a non-interactive, silent authentication. 

4. If you assign the traffic forwarding profile to specific users and groups, ensure that users signed in to Windows are either assigned to the profile or are a direct member of an assigned group.   

> [!NOTE]
> Traffic profiles are fetched on behalf of the Microsoft Entra user logged into Windows, not the user logged into the client. Multiple users logging into the same device simultaneously isn't supported. Nested group memberships aren't supported. Each user must be a direct member of the group assigned to the profile. 

5. Ensure the Global Secure Access client can reach the policy service in the cloud by checking that the **Policy service hostname resolved by DNS** and the **Policy server is reachable** health check tests pass.
  

## Related content
- [How to assign users and groups to traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-manage-users-groups-assignment)   
- [Global Secure Access traffic forwarding profiles](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-traffic-forwarding)   
- [Troubleshoot the Global Secure Access client: Advanced diagnostics](https://learn.microsoft.com/en-us/entra/global-secure-access/troubleshoot-global-secure-access-client-advanced-diagnostics)
