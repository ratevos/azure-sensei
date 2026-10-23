# Deploy Microsoft 365 Directory Synchronization in Microsoft Azure

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/deploy-microsoft-365-directory-synchronization-dirsync-in-microsoft-azure  
> Microsoft doc last updated: 02/12/2025


Microsoft Entra Connect (formerly known as the Directory Synchronization tool, Directory Sync tool, or the DirSync.exe tool) is an application that you install on a domain-joined server to synchronize your on-premises Active Directory Domain Services (AD DS) users to the Microsoft Entra tenant of your Microsoft 365 subscription. Microsoft 365 uses Microsoft Entra ID for its directory service. Your Microsoft 365 subscription includes a Microsoft Entra tenant. This tenant can also be used for management of your organization's identities with other cloud workloads, including other SaaS applications and apps in Azure.

You can install Microsoft Entra Connect on an on-premises server, but you can also install it on a virtual machine in Azure for these reasons:
  
- You can provision and configure cloud-based servers faster, making the services available to your users sooner.
- Azure offers better site availability with less effort.
- You can reduce the number of on-premises servers in your organization.

This solution requires connectivity between your on-premises network and your Azure virtual network. For more information, see [Connect an on-premises network to a Microsoft Azure virtual network](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-an-on-premises-network-to-a-microsoft-azure-virtual-network). 
  
> [!NOTE]
> This article describes synchronization of a single domain in a single forest. Microsoft Entra Connect synchronizes all AD DS domains in your Active Directory forest with Microsoft 365. If you have multiple Active Directory forests to synchronize with Microsoft 365, see [Multi-forest Directory Sync with Single Sign-On Scenario](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-hybrid-identity).
  
## Overview of deploying Microsoft 365 directory synchronization in Azure

The following diagram shows Microsoft Entra Connect running on a virtual machine in Azure (the directory sync server) that synchronizes an on-premises AD DS forest to a Microsoft 365 subscription.
  

  
In the diagram, there are two networks connected by a site-to-site VPN or ExpressRoute connection. There's an on-premises network where AD DS domain controllers are located, and there's an Azure virtual network with a directory sync server, which is a virtual machine running [Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594). There are two main traffic flows originating from the directory sync server:
  
- Microsoft Entra Connect queries a domain controller on the on-premises network for changes to accounts and passwords.
- Microsoft Entra Connect sends the changes to accounts and passwords to the Microsoft Entra instance of your Microsoft 365 subscription. Because the directory sync server is in an extended portion of your on-premises network, these changes are sent through the on-premises network's proxy server.

> [!NOTE]
> This solution describes synchronization of a single Active Directory domain, in a single Active Directory forest. Microsoft Entra Connect synchronizes all Active Directory domains in your Active Directory forest with Microsoft 365. If you have multiple Active Directory forests to synchronize with Microsoft 365, see [Multi-forest Directory Sync with Single Sign-On Scenario](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/whatis-hybrid-identity).
  
There are two major steps when you deploy this solution:
  
1. Create an Azure virtual network and establish a site-to-site VPN connection to your on-premises network. For more information, see [Connect an on-premises network to a Microsoft Azure virtual network](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-an-on-premises-network-to-a-microsoft-azure-virtual-network).

2. Install [Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594) on a domain-joined virtual machine in Azure, and then synchronize the on-premises AD DS to Microsoft 365. This involves:

    - Creating an Azure Virtual Machine to run Microsoft Entra Connect.

    - Installing and configuring [Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594).

    Configuring Microsoft Entra Connect requires the credentials (user name and password) of a Microsoft Entra administrator account and an AD DS enterprise administrator account. Microsoft Entra Connect runs immediately and on an ongoing basis to synchronize the on-premises AD DS forest to Microsoft 365.

Before you deploy this solution in production, you can use the instructions in [The simulated enterprise base configuration](https://learn.microsoft.com/en-us/microsoft-365/enterprise/simulated-ent-base-configuration-microsoft-365-enterprise) to set up this configuration as a proof of concept, for demonstrations, or for experimentation.
  
> [!IMPORTANT]
> When Microsoft Entra Connect configuration completes, it does not save the AD DS enterprise administrator account credentials.

> [!NOTE]
> This solution describes synchronizing a single AD DS forest to Microsoft 365. The topology discussed in this article represents only one way to implement this solution. Your organization's topology might differ based on your unique network requirements and security considerations.
  
## Plan for hosting a directory sync server for Microsoft 365 in Azure
<a name="PlanningVirtual"> </a>

### Prerequisites

Before you begin, review the following prerequisites for this solution:
  
- An Azure subscription. For information about Azure subscriptions, go to the [How To Buy Azure page](https://azure.microsoft.com/pricing/purchase-options/).

- An available private IPv4 address space to assign to the virtual network and its subnets, with sufficient room for growth to accommodate the number of virtual machines needed now and in the future.

- An available VPN device in your on-premises network to terminate the site-to-site VPN connection that supports the requirements for IPsec. For more information, see [About VPN devices for site-to-site virtual network connections](https://learn.microsoft.com/en-us/azure/vpn-gateway/vpn-gateway-about-vpn-devices).

- Changes to your routing infrastructure so that traffic routed to the address space of the Azure virtual network gets forwarded to the VPN device that hosts the site-to-site VPN connection.

- A web proxy that gives computers that are connected to the on-premises network and the Azure virtual network access to the Internet.

- Have a Microsoft 365 subscription that includes the Active Directory integration feature. For information about Microsoft 365 subscriptions, go to the [Microsoft 365 subscription page](https://products.office.com/compare-all-microsoft-office-products?tab=2).

- Provision one Azure Virtual Machine that runs Microsoft Entra Connect to synchronize your on-premises AD DS forest with Microsoft 365.

    You must have the credentials (names and passwords) for an AD DS enterprise administrator account and a Microsoft Entra Administrator account.

### Solution architecture design assumptions

The following list describes the design choices made for this solution.
  
- This solution uses a single Azure virtual network with a site-to-site VPN connection. The Azure virtual network hosts a single subnet that has one server, the directory sync server that is running Microsoft Entra Connect.

- On the on-premises network, a domain controller and DNS servers exist.

- Microsoft Entra Connect performs password hash synchronization instead of single sign-on. You don't have to deploy an Active Directory Federation Services (AD FS) infrastructure. To learn more about password hash synchronization and single sign-on options, see [Choosing the right authentication method for your Microsoft Entra hybrid identity solution](https://learn.microsoft.com/en-us/azure/active-directory/hybrid/choose-ad-authn).

There are other design choices that you might consider when you deploy this solution in your environment. These include the following:
  
- If there are existing DNS servers in an existing Azure virtual network, determine whether you want your directory sync server to use them for name resolution instead of DNS servers on the on-premises network.

- If there are domain controllers in an existing Azure virtual network, determine whether configuring Active Directory Sites and Services might be a better option for you. The directory sync server can query the domain controllers in the Azure virtual network for changes in accounts and passwords instead of domain controllers on the on-premises network.

## Deployment roadmap

Deploying Microsoft Entra Connect on a virtual machine in Azure consists of three phases:
  
- Phase 1: Create and configure the Azure virtual network

- Phase 2: Create and configure the Azure virtual machine

- Phase 3: Install and configure Microsoft Entra Connect

After deployment, you must also assign locations and licenses for the new user accounts in Microsoft 365.

### Phase 1: Create and configure the Azure virtual network

To create and configure the Azure virtual network, see [Tutorial: Create and manage a VPN gateway using the Azure portal](https://learn.microsoft.com/en-us/azure/vpn-gateway/tutorial-create-gateway-portal).
  
This is your resulting configuration.
  

  
This figure shows an on-premises network connected to an Azure virtual network through a site-to-site VPN or ExpressRoute connection.
  
### Phase 2: Create and configure the Azure virtual machine

Create the virtual machine in Azure using the instructions [Create your first Windows virtual machine in the Azure portal](https://go.microsoft.com/fwlink/p/?LinkId=393098). Use the following settings:
  
1. On the **Basics** pane, select the same subscription, location, and resource group as your virtual network. Record the user name and password in a secure location. You'll need these later to connect to the virtual machine.

1. On the **Choose a size** pane, choose the **A2 Standard** size.

1. On the **Settings** pane, in the **Storage** section, select the **Standard** storage type. In the **Network** section, select the name of your virtual network and the subnet for hosting the directory sync server (not the GatewaySubnet). Leave all other settings at their default values.

Verify that your directory sync server is using DNS correctly by checking your internal DNS to make sure that an Address (A) record was added for the virtual machine with its IP address. 
  
Use the instructions in [Connect to the virtual machine and sign on](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/connect-logon) to connect to the directory sync server with a Remote Desktop Connection. After signing in, join the virtual machine to the on-premises AD DS domain.
  
For Microsoft Entra Connect to gain access to Internet resources, you must configure the directory sync server to use the on-premises network's proxy server. You should contact your network administrator for any additional configuration steps to perform.
  
This is your resulting configuration.
  

  
This figure shows the directory sync server virtual machine in the cross-premises Azure virtual network.
  
<a name='phase-3-install-and-configure-azure-ad-connect'></a>

### Phase 3: Install and configure Microsoft Entra Connect

Complete the following procedure:
  
1. Connect to the directory sync server using a Remote Desktop Connection with an AD DS domain account that has local administrator privileges. See [Connect to the virtual machine and sign on](https://learn.microsoft.com/en-us/azure/virtual-machines/windows/connect-logon).

2. From the directory sync server, open the [Set up directory synchronization for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/set-up-directory-synchronization) article and follow the directions for directory synchronization with password hash synchronization.

> [!CAUTION]
> Setup creates the **AAD_xxxxxxxxxxxx** account in the Local Users organizational unit (OU). Do not move or remove this account or synchronization will fail.
  
This is your resulting configuration.
  

  
This figure shows the directory sync server with Microsoft Entra Connect in the cross-premises Azure virtual network.
  
### Assign locations and licenses to users in Microsoft 365

Microsoft Entra Connect adds accounts to your Microsoft 365 subscription from the on-premises AD DS, but in order for users to sign in to Microsoft 365 and use its services, the accounts must be configured with a location and licenses. Use these steps to add the location and activate licenses for the appropriate user accounts:
  
1. Sign in to the [Microsoft 365 admin center](https://admin.microsoft.com), and then click **Admin**.

2. In the left navigation, click **Users** > <a href="https://go.microsoft.com/fwlink/p/?linkid=834822" target="_blank">**Active users**</a>.
3. In the list of user accounts, select the check box next to the user you want to activate.

4. On the page for the user, click **Edit** for **Product licenses**.

5. On the **Product licenses** page, select a location for the user for **Location**, and then enable the appropriate licenses for the user.

6. When complete, click **Save**, and then click **Close** twice.

7. Go back to step 3 for additional users.

## See also

[Microsoft 365 solution and architecture center](https://learn.microsoft.com/en-us/previous-versions/microsoft-365/solutions/)
  
[Connect an on-premises network to a Microsoft Azure virtual network](https://learn.microsoft.com/en-us/microsoft-365/enterprise/connect-an-on-premises-network-to-a-microsoft-azure-virtual-network)

[Download Microsoft Entra Connect](https://www.microsoft.com/download/details.aspx?id=47594)
  
[Set up directory synchronization for Microsoft 365](https://learn.microsoft.com/en-us/microsoft-365/enterprise/set-up-directory-synchronization)
