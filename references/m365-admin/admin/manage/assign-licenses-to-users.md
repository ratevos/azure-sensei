# Assign or unassign licenses for users in the Microsoft 365 admin center

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/assign-licenses-to-users  
> Microsoft doc last updated: 02/19/2026


Check out all of our small business content on [Small business help & learning](https://go.microsoft.com/fwlink/?linkid=2224585).

You can assign or unassign licenses for users in the Microsoft 365 admin center on either the **Active users** page, or on the **Licenses** page. The method you use depends on whether you want to assign or unassign licenses for specific users, or assign or unassign users for a specific product. You can also [add a user and assign a license at the same time](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/add-users).

> [!NOTE]
>
> - As an admin, you can't assign or unassign licenses for a self-service purchase subscription bought by a user in your organization. You can [take over a purchase or trial subscription](https://learn.microsoft.com/en-us/microsoft-365/commerce/subscriptions/manage-self-service-purchases-admins#take-over-a-self-service-purchase-or-trial-subscription), and then assign or unassign licenses.
> - For some subscriptions, you can only cancel during a limited window of time after you buy or renew your subscription. If the cancellation window has passed, turn off recurring billing to cancel the subscription at the end of its term.

## Before you begin

- You must be at least a License or User Administrator to assign licenses. For more information, see [About Microsoft 365 admin roles](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/about-admin-roles).
- In addition to the steps described in this article, you can also use the Microsoft Graph PowerShell SDK to [assign Microsoft 365 licenses to user accounts with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/assign-licenses-to-user-accounts-with-microsoft-365-powershell) or [remove Microsoft 365 licenses from user accounts with PowerShell](https://learn.microsoft.com/en-us/microsoft-365/enterprise/remove-licenses-from-user-accounts-with-microsoft-365-powershell).
- To use group-based licensing, see [Assign licenses to users by group membership in Microsoft Entra ID](https://learn.microsoft.com/en-us/azure/active-directory/enterprise-users/licensing-groups-assign)
- Some services, like Sway, are automatically assigned to users, and don't need to be assigned individually.
- You can also [delete user accounts](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/delete-a-user) that were assigned a license to make their license available to other users. When you delete a user account, their license is immediately available to assign to someone else.
- If you're a Cloud Solution Provider (CSP) and you bought products on behalf of a customer, you can't use the **Your products** page to assign or unassign licenses for certain products, like perpetual software. To assign or unassign licenses for those products, [use the Licenses page](#use-the-licenses-page-to-assign-or-unassign-licenses).

## Use the Licenses page to assign or unassign licenses

1. In the admin center, go to the **Billing** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
1. Select a product.
1. On the product details page, select **Assign licenses**.
1. In the **Assign licenses** panel, begin typing the name of a user or group, and then select it from the results to add it to the list. You can add up to 20 users and/or groups at a time.
1. Select **Turn apps and services on or off** to assign or remove access to specific items.
1. When you're finished, select **Assign**, then close the right pane.

If there’s a problem completing the assignment, you see a status message when the action finishes. If some users in a group couldn’t be assigned licenses, select **View errors and issues** to see details for each affected user. After resolving the issue, you can retry the assignment.

### How license assignments appear on the Licenses page

On the **Licenses** page, assignments are displayed based on how the license was applied:

- **Direct user assignments** If a license is assigned directly to a user, the user appears individually in the list of assignments for that product.
- **Group-based assignments** If a license is assigned to a group, the group name appears in the list instead of individual users. To see which users are receiving the license through that group, go to the **Teams & groups** > <a href="https://admin.cloud.microsoft/?#/groups" target="_blank">Active teams & groups</a> page to view its members.

The **Licenses** page might show an aggregate total of licenses for all subscriptions for the same product name. For example, you might have one subscription for Microsoft 365 Business Premium that has five licenses, and another subscription that has eight licenses for the same product. The **Licenses** page shows that you have a total of 13 licenses for Microsoft 365 Business Premium across all your subscriptions. This number is different from what you see on the **Your products** page, which displays a row for each subscription you own, even if they are for the same product.

### Change the apps and services a user has access to

1. In the admin center, go to the **Billing** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
1. On the **Licenses** page, select the row for a specific user or group you want to change.
1. In the details pane, select or deselect the apps and services that you want to give access to or remove access from.
1. When you're finished, select **Save**, then select **Close**.

### Unassign licenses by using the Licenses page

1. In the admin center, go to the **Billing** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=842264" target="_blank">Licenses</a> page.
1. Select a product.
1. Select the check boxes of the users or groups for whom you want to unassign licenses.
1. Select **Unassign licenses**.

### Understand errors and issues when managing licenses

The Microsoft 365 admin center provides a list of **Errors & Issues** to help you understand what happened and take action when licenses aren’t applied as expected.

For each product, you can open the **Errors & Issues** tab to do the following:

- **View licensing errors**, which shows users who didn’t receive a license and the reason for the failure.
- **Identify users without licenses**, even if the assignment was attempted.
- **Select a user to see details**, including their current status and available options for fixing the issue.

Common reasons you might see errors or issues include the following:

- No available licenses for the selected product
- Conflicting services or license plans
- An invalid usage location

After you resolve the underlying issue&mdash;such as freeing up licenses, adjusting services, or updating user or group membership&mdash;you can retry the assignment directly from the **Errors & Issues** tab. Select the user with the error to open the details pane, then select **Reprocess**. Reprocessing attempts to apply the license again using the current configuration and available licenses.

## Use the Active users page to assign or unassign licenses

When you use the **Active users** page to assign or unassign licenses, you assign or unassign users licenses to products.

### Assign licenses to one user

1. In the admin center, go to the **Users** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834822" target="_blank">Active users</a> page.
1. Select the row of the user that you want to assign a license to.
1. In the right pane, select **Licenses and Apps**.
1. Expand the **Licenses** section, select the boxes for the licenses that you want to assign, then select **Save changes**.

### Assign licenses to multiple users

1. In the admin center, go to the **Users** > <a href="https://go.microsoft.com/fwlink/p/?linkid=834822" target="_blank">Active users</a> page.
1. Select the circles next to the names of the users that you want to assign licenses to.
1. At the top, select **Manage product licenses**.
1. In the **Manage product licenses** pane, select **Assign more: Keep the existing licenses and assign more** > **Next**.
1. Under **Licenses**, select the box for the license(s) that you want the selected users to have.

   By default, all services associated with those licenses are automatically assigned to the users. You can limit which services are available to the users. Deselect the boxes for the services that you don't want the users to have.
   
1. At the bottom of the pane, select **Save changes**.  

   You might have to buy more licenses if you don't have enough licenses for everyone.
   
> [!NOTE]
> If you want to assign licenses for a large number of users, use [Assign or unassign licenses to a group in the Microsoft 365 admin center](https://learn.microsoft.com/en-us/microsoft-365/admin/manage/manage-group-licenses).

## Use the Active users page to unassign licenses

When you use the **Active users** page to unassign licenses, you remove product licenses from users.

### Unassign licenses from one user

1. In the admin center, go to the **Users** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834822" target="_blank">Active users</a> page.
2. Select the row of the user that you want to unassign a license for.
3. In the right pane, select **Licenses and Apps**.
4. Expand the **Licenses** section, clear the boxes for the licenses that you want to unassign, then select **Save changes**.

### Unassign licenses from multiple users

1. In the admin center, go to the **Users** \> <a href="https://go.microsoft.com/fwlink/p/?linkid=834822" target="_blank">Active users</a> page.
2. Select the circles next to the names of the users who you want to unassign licenses for.
3. At the top, select **Manage product licenses**.
4. In the **Manage product licenses** pane, select **Unassign all** > **Save changes**.
5. At the bottom of the pane, select **Done**.  

## What happens to a user's data when you remove their license?

- When a license is removed from a user, Exchange Online data that is associated with that account is held for 30 days. After the 30-day grace period, the data is deleted and can't be recovered. However, it's linked to the retention policy, and the content that matches retention labels is retained for discovery.
- Files saved in OneDrive for Business aren't deleted unless the user is deleted from the Microsoft 365 admin center or is removed through Active Directory synchronization. For more information, see [OneDrive retention and deletion](https://learn.microsoft.com/en-us/onedrive/retention-and-deletion).
- When the license is removed, the user's mailbox is no longer searchable by using an eDiscovery tool such as Content Search or eDiscovery (Premium).
- If you have an Enterprise subscription, like Office 365 Enterprise E3, Exchange Online lets you preserve the mailbox data of a deleted user account by using [inactive mailboxes](https://learn.microsoft.com/en-us/microsoft-365/compliance/inactive-mailboxes-in-office-365). For more information, see [Create and manage inactive mailboxes in Exchange Online](https://learn.microsoft.com/en-us/microsoft-365/compliance/create-and-manage-inactive-mailboxes).
- To learn how to block a user's access to Microsoft 365 data after their license is removed, and how to get access to the data afterwards, see [Overview: Remove a former employee and secure data](https://learn.microsoft.com/en-us/microsoft-365/admin/add-users/remove-former-employee).
- If you remove a user's license and they still have Microsoft 365 productivity apps installed, they see [Unlicensed Product and activation errors in Office](https://support.microsoft.com/office/0d23d3c0-c19c-4b2f-9845-5344fedc4380) when they use Microsoft 365 productivity apps.

## Next steps

If you assigned licenses and your users don't have Microsoft 365 productivity apps installed, you can share the [Employee quick setup in Microsoft 365 for business](https://support.microsoft.com/office/7f34c318-e772-46a5-8c0a-ab86661542d1) with your users to set up things like [Download and install or reinstall Microsoft 365 or Office 2021 on a PC or Mac](https://support.microsoft.com/office/4414eaaf-0478-48be-9c42-23adc4716658) and [Set up Microsoft 365 apps and email on a mobile device](https://support.microsoft.com/office/7dabb6cb-0046-40b6-81fe-767e0b1f014f).

If you unassigned licenses and you don't plan to reassign the unused licenses to other users, consider [removing the licenses from your subscription](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/buy-licenses) so that you're not paying for more licenses than you need.

## Related content

[Understand subscriptions and licenses in Microsoft 365 for business](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/subscriptions-and-licenses) (article)\
[Buy or remove licenses for a Microsoft business subscription](https://learn.microsoft.com/en-us/microsoft-365/commerce/licenses/buy-licenses) (article)
