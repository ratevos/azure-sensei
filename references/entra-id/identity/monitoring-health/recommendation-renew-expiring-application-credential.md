# Recommendation to renew expiring application credentials

> Source: https://learn.microsoft.com/en-us/entra/identity/monitoring-health/recommendation-renew-expiring-application-credential  
> Microsoft doc last updated: 04/09/2025


[Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations) is a feature that provides you with personalized insights and actionable guidance to align your tenant with recommended best practices.

This article covers the recommendation to renew expiring application credentials. This recommendation is called `applicationCredentialExpiry` in the recommendations API in Microsoft Graph. 

## Prerequisites

There are different role requirements for viewing or updating a recommendation. Use the least-privileged role for the type of access needed. For a full list of roles, see [Least privileged roles by task](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/delegate-by-task#monitoring-and-health---recommendations-least-privileged-roles).

| Microsoft Entra role | Access type |
|---- |---- |
| Reports Reader | Read-only |
| Security Reader | Read-only |
| Global Reader | Read-only |
| Authentication Policy Administrator | Update and read |
| Exchange Administrator | Update and read |
| Security Administrator | Update and read |
| `DirectoryRecommendations.Read.All` | Read-only in Microsoft Graph |
| `DirectoryRecommendations.ReadWrite.All` | Update and read in Microsoft Graph |

Some recommendations might require a P2 or other license. For more information, see the [Recommendations overview table](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations#recommendations-overview-table).

## Description

Application credentials can include certificates and other types of secrets that need to be registered with that application. These credentials are used to prove the identity of the application.

This recommendation shows up if your tenant has application credentials that will expire soon.

An application credential is expiring if:

- It's on an application registration AND is expiring within the next 30 days.

The following credentials are exempted from this recommendation:

- Credentials that were identified as expiring but have since been removed from the app registration
- Credentials whose expiration date has lapsed show as **completed** in the list of **Impacted resources**.

## Value

Renewing an application’s credentials prior to their expiry date is crucial for maintaining uninterrupted operations and minimizing the risk of any downtime resulting from outdated credentials.

## Action plan

This recommendation is available in the Microsoft Entra admin center and using the Microsoft Graph API.

### [Microsoft Entra admin center](#tab/microsoft-entra-admin-center)

1. Sign in to the [Microsoft Entra admin center](https://entra.microsoft.com) as at least a [Security Administrator](https://learn.microsoft.com/en-us/entra/identity/role-based-access-control/permissions-reference#search-administrator).

1. Browse to **Entra ID** > **Overview**.

1. Select the **Recommendations** tab and select the **Renew expiring application credentials** recommendation.

1. Take note of the following details from the **Impacted resources** table.
    - The **Resource** column displays the application name
    - The **ID** column displays the application ID

        

1. Select **More Details** from the **Actions** column.

1. From the panel that opens, select **Update Credential** to navigate directly to the **Certificates & secrets** area of the app registration to renew the expiring credential.
    1. Alternatively, browse to **Entra ID** > **App registrations** and locate the application for which the credential needs to be rotated.

      

    1. Navigate to the **Certificates & Secrets** section of the app registration.

1. Pick the credential type that you want to rotate and navigate to either **Certificates** or **Client Secret** tab and follow the prompts.

    

1. Once the certificate or secret is successfully added, update the service code to ensure it works with the new credential and doesn't negatively affect customers.

1. Use the Microsoft Entra sign-in logs to validate that the Key ID of the credential matches the one that was recently added.

1. After validating the new credential, navigate back to **App registrations** > **Certificates and Secrets** for the app and remove the old credential.

### [Microsoft Graph API](#tab/microsoft-graph-api)

The following requests can be used to retrieve the recommendation and the impacted resources using the Microsoft Graph API. To use the Microsoft Graph API, you need the `DirectoryRecommendations.Read.All` and `DirectoryRecommendations.ReadWrite.All` permissions. For more information, see [How to use Identity Recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations).

1. Sign in to [Graph Explorer](https://developer.microsoft.com/graph/graph-explorer).
1. Select **GET** as the HTTP method from the dropdown.

To retrieve all recommendations for your tenant:

```http
GET https://graph.microsoft.com/beta/directory/recommendations
```

From the response, find the ID of the recommendation that matches the following pattern: `{tenantId}_ApplicationCredentialExpiry`.

To identify impacted resources:

```http
GET https://graph.microsoft.com/beta/directory/recommendations/{tenantId}_ApplicationCredentialExpiry
```

To filter the resources based on their status (for example, *active* resources):

```http
GET https://graph.microsoft.com/beta/directory/recommendations/536279f6-15cc-45f2-be2d-61e352b51eef_ ApplicationCredentialExpiry’/impactedResources?$filter=status eq Microsoft.Graph.recommendationStatus'active'
```

Take note of the `AppId`, `CredentialId`, and `Origin` of the credential you want to remove. To remove the credential, use the following Microsoft Graph guidance:

- [addPassword](https://learn.microsoft.com/en-us/graph/api/application-addpassword?view=graph-rest-1.0&preserve-view=true)
- [addKey](https://learn.microsoft.com/en-us/graph/api/application-addkey?view=graph-rest-1.0&preserve-view=true)
- [removePassword](https://learn.microsoft.com/en-us/graph/api/application-removepassword?view=graph-rest-1.0&preserve-view=true)
- [removeKey](https://learn.microsoft.com/en-us/graph/api/application-removekey?view=graph-rest-1.0&preserve-view=true)

#### Sample response

```json
 {
  "id": "aaaabbbb-6666-cccc-7777-dddd8888eeee_ApplicationCredentialExpiry",
  "recommendationType": "applicationCredentialExpiry",
  "createdDateTime": "2022-06-08T00:08:01Z",
  "impactStartDateTime": "2022-06-08T00:08:01Z",
  "postponeUntilDateTime": null,
  "lastModifiedDateTime": "2024-07-29T12:03:16Z",
  "lastModifiedBy": "System",
  "displayName": "Renew expiring application credentials",
  "featureAreas": [
    "applications"
  ],
  "insights": "Your tenant has applications with credentials that will expire soon.",
  "benefits": "Renewing the app credential(s) before its expiration ensures the application continues to function and reduces the possibility of downtime due to an expired credential.",
  "category": "identityBestPractice",
  "status": "active",
  "priority": "high",
  "requiredLicenses": "microsoftEntraWorkloadId",
  "impactType": "apps",
  "actionSteps": [
    {
      "stepNumber": 1,
      "text": "1. Navigate to the App registration section and locate the application for which the credential needs to be rotated."
    },
    {
      "stepNumber": 2,
      "text": "2. Navigate to the “Certificates & Secrets” blade of the app registration."
    },
    {
      "stepNumber": 3,
      "text": "3. Pick the credential type that you want to rotate and navigate to either “Certificates” or “Client Secret” tab and follow the prompts.",
      "actionUrl": null
    },
    {
      "stepNumber": 4,
      "text": "4. Once the certificate or secret is successfully added, update the service code to ensure it works with the new credential and has no negative customer impact. You should use Microsoft Entra ID’s sign-in logs to validate that the thumbprint of the certificate matches the one that was just uploaded.",
      "actionUrl": null
    },
    {
      "stepNumber": 5,
      "text": "5. After validating the new credential, navigate back to the Certificates and Secrets blade for the app and remove the old credential.",
      "actionUrl": null
    }
  ]
}
```

---

## Related content

- [Review the Microsoft Entra recommendations overview](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/overview-recommendations)
- [Learn how to use Microsoft Entra recommendations](https://learn.microsoft.com/en-us/entra/identity/monitoring-health/howto-use-recommendations)
- [Explore the Microsoft Graph API properties for recommendations](https://learn.microsoft.com/en-us/graph/api/resources/recommendation)
- [Learn about app and service principal objects in Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/identity-platform/app-objects-and-service-principals)
