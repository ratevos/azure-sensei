# What are custom security attributes in Microsoft Entra ID?

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-overview  
> Microsoft doc last updated: 10/28/2024


Custom security attributes in Microsoft Entra ID are business-specific attributes (key-value pairs) that you can define and assign to Microsoft Entra objects. These attributes can be used to store information, categorize objects, or enforce fine-grained access control over specific Azure resources. Custom security attributes can be used with [Azure attribute-based access control (ABAC)](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-overview).

## Why use custom security attributes?

Here are some scenarios where you could use custom security attributes:

- Extend user profiles, such as add Hourly Salary to all my employees.
- Ensure only administrators can see the Hourly Salary attribute in my employees' profiles.
- Categorize hundreds or thousands of applications to easily create a filterable inventory for auditing.
- Grant users access to the Azure Storage blobs belonging to a project.

## What can I do with custom security attributes?

Custom security attributes include these capabilities:

- Define business-specific information (attributes) for your tenant.
- Add a set of custom security attributes on users and applications.
- Manage Microsoft Entra objects using custom security attributes with queries and filters.
- Provide attribute governance so attributes determine who can get access.

Custom security attributes **aren't** supported in the following areas:

- [Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview)
- [Security Assertion Markup Language (SAML) token claims](https://learn.microsoft.com/en-us/entra/identity-platform/saml-claims-customization)
- [JSON Web Token claims](https://learn.microsoft.com/en-us/entra/identity-platform/security-tokens)

## Features of custom security attributes

Custom security attributes include these features:

- Available tenant-wide
- Include a description
- Support different data types: Boolean, integer, string
- Support single value or multiple values
- Support user-defined free-form values or predefined values
- Assign custom security attributes to directory synced users from an on-premises Active Directory

The following example shows several custom security attributes assigned to a user. The custom security attributes are different data types and have values that are single, multiple, free-form, or predefined.

## Objects that support custom security attributes

You can add custom security attributes for the following Microsoft Entra objects:

- Microsoft Entra users
- Microsoft Entra enterprise applications (service principals)

## How do custom security attributes compare with extensions?

While both extensions and custom security attributes can be used to extend objects in Microsoft Entra ID and Microsoft 365, they are suitable for fundamentally different custom data scenarios. Here are some ways that custom security attributes compare with [extensions](https://learn.microsoft.com/en-us/graph/extensibility-overview):

| Capability | Extensions | Custom security attributes |
|--|--|--|
| Extend Microsoft Entra ID and Microsoft 365 objects | Yes | Yes |
| Supported objects | Depends on the extension type | Users and service principals |
| Restricted access | No. Anyone with permissions to read the object can read the extension data. | Yes. Read and write access is restricted through a separate set of permissions and role-based access control (RBAC). |
| When to use | Store data to be used by an application <br/> Store non-sensitive data | Store sensitive data <br/> Use for authorization scenarios |
| License requirements | Available in all editions of Microsoft Entra ID | Available in all editions of Microsoft Entra ID |

For more information about working with extensions, see [Add custom data to resources using extensions](https://learn.microsoft.com/en-us/graph/extensibility-overview).

## Steps to use custom security attributes

1. **Check permissions**

    Check that you are assigned the [Attribute Definition Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-administrator) or [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-administrator) roles. If necessary, someone with at least the [Privileged Role Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#privileged-role-administrator) role can assign these roles.

    

1. **Add attribute sets**

    Add attribute sets to group and manage related custom security attributes. [Learn more](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-add)

    

1. **Manage attribute sets**

    Specify who can read, define, or assign custom security attributes in an attribute set. [Learn more](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-manage)

    

1. **Define attributes**

    Add your custom security attributes to your directory. You can specify the date type (Boolean, integer, or string) and whether values are predefined, free-form, single, or multiple. [Learn more](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-add)

    

1. **Assign attributes**

    Assign custom security attributes to Microsoft Entra objects for your business scenarios. [Learn more](https://learn.microsoft.com/en-us/entra/identity/users/users-custom-security-attributes)

    

1. **Use attributes**

    Filter users and applications that use custom security attributes. [Learn more](https://learn.microsoft.com/en-us/entra/identity/users/users-custom-security-attributes)

    Add conditions that use custom security attributes to Azure role assignments for fine-grained access control. [Learn more](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-custom-security-attributes)

## Terminology

To better understand custom security attributes, you can refer back to the following list of terms.

| Term | Definition |
| --- | --- |
| attribute definition | The schema of a custom security attribute or key-value pair. For example, the custom security attribute name, description, data type, and predefined values. |
| attribute set | A collection of related custom security attributes. Attribute sets can be delegated to other users for defining and assigning custom security attributes. |
| attribute name | A unique name of a custom security attribute within an attribute set. The combination of attribute set and attribute name forms a unique attribute for your tenant. |
| attribute assignment | The assignment of a custom security attribute to a Microsoft Entra object, such as users and enterprise applications (service principals). |
| predefined value | A value that is allowed for a custom security attribute. |

## Custom security attribute properties

The following table lists the properties you can specify for attribute sets and custom security attributes. Some properties are immutable and cannot be changed later.

| Property | Required | Can be changed later | Description |
| --- | :---: | :---: | --- |
| Attribute set name  | :white_check_mark: |  | Name of the attribute set. Must be unique within a tenant. Cannot include spaces or special characters. |
| Attribute set description |  | :white_check_mark: | Description of the attribute set. |
| Maximum number of attributes |  | :white_check_mark: | Maximum number of custom security attributes that can be defined in an attribute set. Default value is `null`. If not specified, the administrator can add up to the maximum of 500 active attributes per tenant. |
| Attribute set | :white_check_mark: |  | A collection of related custom security attributes. Every custom security attribute must be part of an attribute set. |
| Attribute name  | :white_check_mark: |  | Name of the custom security attribute. Must be unique within an attribute set. Cannot include spaces or special characters. |
| Attribute description |  | :white_check_mark: | Description of the custom security attribute. |
| Data type | :white_check_mark: |  | Data type for the custom security attribute values. Supported types are `Boolean`, `Integer`, and `String`. |
| Allow multiple values to be assigned | :white_check_mark: |  | Indicates whether multiple values can be assigned to the custom security attribute. If data type is set to `Boolean`, cannot be set to Yes. |
| Only allow predefined values to be assigned | :white_check_mark: |  | Indicates whether only predefined values can be assigned to the custom security attribute. If set to No, free-form values are allowed. Can later be changed from Yes to No, but cannot be changed from No to Yes. If data type is set to `Boolean`, cannot be set to Yes.|
| Predefined values |  |  | Predefined values for the custom security attribute of the selected data type. More predefined values can be added later. Values can include spaces, but some special characters are not allowed. |
| Predefined value is active |  | :white_check_mark: | Specifies whether the predefined value is active or deactivated. If set to false, the predefined value cannot be assigned to any additional supported directory objects. |
| Attribute is active |  | :white_check_mark: | Specifies whether the custom security attribute is active or deactivated. |

## Limits and constraints

Here are some of the limits and constraints for custom security attributes.

> | Resource | Limit | Notes |
> | --- | :---: | --- |
> | Attribute definitions per tenant | 500 | Applies only to active attributes in the tenant |
> | Attribute sets per tenant | 500 |  |
> | Attribute set name length | 32 | Unicode characters and case sensitive |
> | Attribute set description length | 128 | Unicode characters |
> | Attribute name length | 32 | Unicode characters and case sensitive |
> | Attribute description length | 128 | Unicode characters |
> | Predefined values |  | Unicode characters and case sensitive |
> | Predefined values per attribute definition | 100 |  |
> | Attribute value length | 64 | Unicode characters |
> | Attribute values assigned per object | 50 | Values can be distributed across single and multivalued attributes.<br/>Example: 5 attributes with 10 values each or 50 attributes with 1 value each |
> | Special characters **not** allowed for:<br/>Attribute set name<br/>Attribute name | ``<space> ` ~ ! @ # $ % ^ & * ( ) _ - + = { [ } ] \| \ : ; " ' < , > . ? /`` | Attribute set name and attribute name cannot start with a number |
> | Special characters allowed for attribute values | All special characters |  |
> | Special characters allowed for attribute values when used with blob index tags | `<space> + - . : = _ /` | If you plan to use [attribute values with blob index tags](https://learn.microsoft.com/en-us/azure/role-based-access-control/conditions-custom-security-attributes), these are the only special characters allowed for blob index tags. For more information, see [Setting blob index tags](https://learn.microsoft.com/en-us/azure/storage/blobs/storage-manage-find-blobs#setting-blob-index-tags). |

## Custom security attribute roles

Microsoft Entra ID provides built-in roles to work with custom security attributes. The Attribute Definition Administrator role is the minimum role you need to manage custom security attributes. The Attribute Assignment Administrator role is the minimum role you need to assign custom security attribute values for Microsoft Entra objects like users and applications. You can assign these roles at tenant scope or at attribute set scope.

> | Role | Permissions |
> | --- | --- |
> | [Attribute Definition Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-reader) | Read attribute sets<br/>Read custom security attribute definitions |
> | [Attribute Definition Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-definition-administrator) | Manage all aspects of attribute sets<br/>Manage all aspects of custom security attribute definitions |
> | [Attribute Assignment Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-reader) | Read attribute sets<br/>Read custom security attribute definitions<br/>Read custom security attribute keys and values for users and service principals |
> | [Attribute Assignment Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-assignment-administrator) | Read attribute sets<br/>Read custom security attribute definitions<br/>Read and update custom security attribute keys and values for users and service principals |
> | [Attribute Log Reader](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-log-reader) | Read audit logs for custom security attributes |
> | [Attribute Log Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#attribute-log-administrator) | Read audit logs for custom security attributes<br/>Configure diagnostic settings for custom security attributes |

> [!IMPORTANT]
> By default, [Global Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#global-administrator) and other administrator roles do not have permissions to read, define, or assign custom security attributes.

<a name='microsoft-graph-apis'></a>

## Microsoft Graph API

You can manage custom security attributes programmatically using Microsoft Graph API. For more information, see [Overview of custom security attributes using the Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/resources/custom-security-attributes-overview).

You can use an API client such as [Graph Explorer](https://learn.microsoft.com/en-us/graph/graph-explorer/graph-explorer-overview) to more easily try the Microsoft Graph API for custom security attributes.

## License requirements

Using this feature is free and included in your Azure subscription.

## Next steps

- [Add or deactivate custom security attribute definitions in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-add)
- [Manage access to custom security attributes in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/custom-security-attributes-manage)
- [Assign, update, list, or remove custom security attributes for a user](https://learn.microsoft.com/en-us/entra/identity/users/users-custom-security-attributes)
- [Provision custom security attributes from HR sources (preview)](https://learn.microsoft.com/en-us/entra/identity/app-provisioning/provision-custom-security-attributes)
