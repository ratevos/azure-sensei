# User management permissions for Microsoft Entra custom roles

> Source: https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-user-permissions  
> Microsoft doc last updated: 06/09/2023


User management permissions can be used in custom role definitions in Microsoft Entra ID to grant fine-grained access such as the following:

- Read or update basic properties of users
- Read identity of users
- Read or update job information of users
- Update contact information of users
- Update parental controls of users
- Update settings of users
- Read direct reports of users
- Update extension properties of users
- Read device information of users
- Read or manage licenses of users
- Update password policies of users
- Read assignments and memberships of users

This article lists the permissions you can use in your custom roles for different user management scenarios. For information about how to create custom roles, see [Create a custom role in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create).

## License requirements

Using this feature requires Microsoft Entra ID P1 licenses. To find the right license for your requirements, see [Compare generally available features of Microsoft Entra ID](https://www.microsoft.com/security/business/identity-access-management/azure-ad-pricing).

## Read or update basic properties of users

The following permissions are available to read or update basic properties of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/standard/read | Read basic properties on users |
> | microsoft.directory/users/basic/update | Update basic properties on users |

## Read identity of users

The following permissions are available to read identity of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/identities/read | Read identities of users |

## Read or update job information of users

The following permissions are available to read or update job information of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/manager/read | Read manager of users |
> | microsoft.directory/users/manager/update | Update manager for users |
> | microsoft.directory/users/jobInfo/update | Update job information of users |

## Update contact information of users

The following permissions are available to update contact information of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/contactInfo/update | Update contact properties on users |

## Update parental controls of users

The following permissions are available to update parental controls of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/parentalControls/update | Update parental controls of users |

## Update settings of users

The following permissions are available to update settings of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/usageLocation/update | Update usage location of users |

## Read direct reports of users

The following permissions are available to read direct reports of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/directReports/read | Read the direct reports for users |

## Update extension properties of users

The following permissions are available to update extension properties of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/extensionProperties/update | Update extension properties of users |

## Read device information of users

The following permissions are available to read device information of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/ownedDevices/read | Read owned devices of users |
> | microsoft.directory/users/registeredDevices/read | Read registered devices of users |
> | microsoft.directory/users/deviceForResourceAccount/read | Read deviceForResourceAccount of users |

## Read or manage licenses of users

The following permissions are available to read or manage licenses of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/licenseDetails/read | Read license details of users |
> | microsoft.directory/users/assignLicense | Manage user licenses |
> | microsoft.directory/users/reprocessLicenseAssignment | Reprocess license assignments for users |

## Update password policies of users

The following permissions are available to update password policies of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/passwordPolicies/update | Update password policies properties of users |

## Read assignments and memberships of users

The following permissions are available to read assignments and memberships of users.

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/appRoleAssignments/read | Read application role assignments for users |
> | microsoft.directory/users/scopedRoleMemberOf/read | Read user's membership of a Microsoft Entra role, that is scoped to an administrative unit |
> | microsoft.directory/users/memberOf/read | Read the dynamic membership group for users |

## Full list of permissions

> | Permission | Description |
> | ---------- | ----------- |
> | microsoft.directory/users/appRoleAssignments/read | Read application role assignments for users |
> | microsoft.directory/users/assignLicense | Manage user licenses |
> | microsoft.directory/users/basic/update | Update basic properties on users |
> | microsoft.directory/users/contactInfo/update | Update contact properties on users |
> | microsoft.directory/users/deviceForResourceAccount/read | Read deviceForResourceAccount of users |
> | microsoft.directory/users/directReports/read | Read the direct reports for users |
> | microsoft.directory/users/extensionProperties/update | Update extension properties of users |
> | microsoft.directory/users/identities/read | Read identities of users |
> | microsoft.directory/users/jobInfo/update | Update job information of users |
> | microsoft.directory/users/licenseDetails/read | Read license details of users |
> | microsoft.directory/users/manager/read | Read manager of users |
> | microsoft.directory/users/manager/update | Update manager for users |
> | microsoft.directory/users/memberOf/read | Read the dynamic membership group for users |
> | microsoft.directory/users/ownedDevices/read | Read owned devices of users |
> | microsoft.directory/users/parentalControls/update | Update parental controls of users |
> | microsoft.directory/users/passwordPolicies/update | Update password policies properties of users |
> | microsoft.directory/users/registeredDevices/read | Read registered devices of users |
> | microsoft.directory/users/reprocessLicenseAssignment | Reprocess license assignments for users |
> | microsoft.directory/users/scopedRoleMemberOf/read | Read user's membership of a Microsoft Entra role, that is scoped to an administrative unit |
> | microsoft.directory/users/standard/read | Read basic properties on users |
> | microsoft.directory/users/usageLocation/update | Update usage location of users |

## Next steps

- [Create a custom role in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/custom-create)
- [List Microsoft Entra role assignments](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/view-assignments)
