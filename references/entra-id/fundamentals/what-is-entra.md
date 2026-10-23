# What is Microsoft Entra?

> Source: https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra  
> Microsoft doc last updated: 06/18/2026


Microsoft Entra is a family of identity and network access products that helps organizations implement a [Zero Trust](https://learn.microsoft.com/en-us/security/zero-trust/zero-trust-overview) security strategy. Use Microsoft Entra to verify identities, validate access conditions, check permissions, encrypt connection channels, and monitor for compromise across your environment. Microsoft Entra also integrates with [Security Copilot](https://learn.microsoft.com/en-us/entra/security-copilot/security-copilot-in-entra) to help investigate identity risks and troubleshoot access issues using AI.

## Microsoft Entra product family

The Microsoft Entra product family spans identity, access, governance, and security. It covers secure end-to-end access for employees, customers, partners, workloads, and AI agents across any cloud environment.

### Establish Zero Trust access controls

#### Microsoft Entra ID

[Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/what-is-entra) is the foundational product of Microsoft Entra. It's a cloud-based identity and access management service that provides authentication, policy enforcement, and protection for users, devices, apps, and resources. Every new Microsoft Entra directory includes an initial domain name, like `contoso.onmicrosoft.com`. You can also add your organization's custom domain names.

If you're a **Microsoft 365, Azure, or Dynamics CRM Online subscriber**, you're already using Microsoft Entra ID — every tenant is automatically a Microsoft Entra tenant. You can start managing access to your integrated cloud apps right away.

#### Microsoft Entra Domain Services

[Microsoft Entra Domain Services](https://learn.microsoft.com/en-us/entra/identity/domain-services/overview) provides managed domain services like group policy, LDAP, and Kerberos/NTLM authentication. It's designed for legacy applications in the cloud that can't use modern authentication methods.

> **Scenario:** An organization with services that need Kerberos authentication can create a managed domain where Microsoft deploys and maintains the core service components.

### Secure access for employees

#### Microsoft Entra Private Access

[Microsoft Entra Private Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access#microsoft-entra-private-access) secures access to all private apps and resources, including corporate networks and multicloud environments. Remote users can connect to internal resources from any device and network without a VPN.

**For example**, an employee can securely access a corporate network printer while working from home or a cafe.

#### Microsoft Entra Internet Access

[Microsoft Entra Internet Access](https://learn.microsoft.com/en-us/entra/global-secure-access/overview-what-is-global-secure-access#microsoft-entra-internet-access) secures access to all internet resources, including SaaS apps and Microsoft 365 apps and resources.

> **Scenario:** Enable web content filtering to regulate access to websites based on content categories and domain names.

#### Microsoft Entra ID Governance

[Microsoft Entra ID Governance](https://learn.microsoft.com/en-us/entra/id-governance/identity-governance-overview) simplifies identity and permissions management by automating access requests, assignments, and reviews. It also helps protect critical assets through identity lifecycle management.

**For example**, administrators can automatically assign user accounts, groups, and licenses to new employees and remove those assignments when employees leave the company.

#### Microsoft Entra ID Protection

[Microsoft Entra ID Protection](https://learn.microsoft.com/en-us/entra/id-protection/overview-identity-protection) detects and reports identity-based risks. Administrators can investigate and automatically remediate risks using tools like [risk-based Conditional Access policies](https://learn.microsoft.com/en-us/entra/id-protection/concept-identity-protection-policies).

> **Scenario:** Create risk-based Conditional Access policies that require multifactor authentication when the sign-in risk level is medium or high.

#### Microsoft Entra Verified ID

[Microsoft Entra Verified ID](https://learn.microsoft.com/en-us/entra/verified-id/decentralized-identifier-overview) is a credential verification service based on open [decentralized identity (DID) standards](https://learn.microsoft.com/en-us/entra/verified-id/verifiable-credentials-standards). Organizations can issue verifiable credentials — digital signatures that prove the validity of information — to users, who store the credentials on their personal devices and present them when needed.

**For example**, a recent college graduate can ask the university to issue a digital diploma to their DID, then present it to a potential employer who can independently verify the issuer, issuance time, and status.

### Secure access for customers and partners

#### Microsoft Entra External ID

[Microsoft Entra External ID](https://learn.microsoft.com/en-us/entra/external-id/external-identities-overview) lets external identities safely access business resources and consumer apps. It provides secure methods for collaborating with business partners and guests on internal apps, and for managing customer identity and access management (CIAM) in consumer-facing applications.

> **Scenario:** Set up self-service registration for customers to sign in to a web application using one-time passcodes or social accounts from Google or Facebook.

### Secure access in any cloud

#### Microsoft Entra Workload ID

[Microsoft Entra Workload ID](https://learn.microsoft.com/en-us/entra/workload-id/workload-identities-overview) is the identity and access management solution for workload identities — applications, services, and containers that require authentication and authorization policies. It lets organizations secure access to resources using adaptive policies and custom security attributes.

**For example**, GitHub Actions needs a workload identity to access Azure subscriptions to automate, customize, and execute software development workflows.

### Secure access for AI agents

#### Microsoft Entra Agent ID

[Microsoft Entra Agent ID](https://learn.microsoft.com/en-us/entra/agent-id/what-is-microsoft-entra-agent-id) is an identity and security framework that extends Microsoft Entra capabilities to AI agents. As organizations deploy assistive, autonomous, and user-like agents, Entra Agent ID provides purpose-built identity constructs to authenticate, authorize, govern, and protect these nonhuman identities at enterprise scale.

> **Scenario:** An organization deploys AI agents that access corporate data on behalf of users. Entra Agent ID provides each agent with a governed identity, enforces least-privilege access, and maintains an audit trail of the agent's actions.

## Prepare your environment

Before deploying Microsoft Entra, configure your infrastructure and processes according to security best practices and standards. The following articles provide architectural, deployment, and operational guidance:

- [Architecture](https://learn.microsoft.com/en-us/entra/architecture/architecture)
- [Deployment plans](https://learn.microsoft.com/en-us/entra/architecture/deployment-plans)
- [Operations reference](https://learn.microsoft.com/en-us/entra/architecture/ops-guide-intro)
- [Operations guide](https://learn.microsoft.com/en-us/entra/architecture/security-operations-introduction)
- [Recommended security configurations](https://learn.microsoft.com/en-us/entra/fundamentals/configure-security)

### License Microsoft Entra features

The features of Microsoft Entra are licensed in multiple ways. These licenses include Microsoft Entra ID Free, Microsoft Entra ID P1, Microsoft Entra ID P2, Microsoft Entra Suite, Microsoft Entra External ID, Microsoft Entra Workload ID, Microsoft Entra ID Governance, and other standalone products. Microsoft Entra is also part of licenses like [Microsoft 365](https://www.microsoft.com/microsoft-365/enterprise/microsoft365-plans-and-pricing) and [Enterprise Mobility + Security](https://www.microsoft.com/microsoft-365/enterprise-mobility-security/compare-plans-and-pricing). For more information about licensing and available options, see the article [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) or the [Microsoft Entra pricing page](https://www.microsoft.com/security/business/microsoft-entra-pricing).

## Manage and develop with Microsoft Entra

Administrators can use the [Microsoft Entra admin center](#microsoft-entra-admin-center) and [Microsoft Graph API](#microsoft-graph-api) to manage identity and network access resources. Developers can use the [Microsoft identity platform](#microsoft-identity-platform) to build identity-aware applications.

### Microsoft Entra admin center

The [Microsoft Entra admin center](https://entra.microsoft.com/) is a web-based portal for configuring and managing Microsoft Entra products from a single interface.

To learn more, see [Overview of Microsoft Entra admin center](https://learn.microsoft.com/en-us/entra/fundamentals/entra-admin-center).

### Microsoft Graph API

The [Microsoft Graph API](https://learn.microsoft.com/en-us/graph/api/overview) automates administrative tasks like license deployments and user lifecycle management.

To learn more, see [Manage Microsoft Entra using Microsoft Graph](https://learn.microsoft.com/en-us/graph/api/resources/identity-network-access-overview).

### Microsoft identity platform

The [Microsoft identity platform](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview) enables developers to build authentication experiences for web, desktop, and mobile applications using open-source libraries and standard-compliant authentication services.

To start developing, see [Getting started](https://learn.microsoft.com/en-us/entra/identity-platform/v2-overview#getting-started).

## Next steps

- [Microsoft Entra licensing](https://learn.microsoft.com/en-us/entra/fundamentals/licensing) — Detailed licensing information for all Microsoft Entra products.
- [Identity and access fundamentals](https://learn.microsoft.com/en-us/entra/fundamentals/identity-fundamental-concepts) — Understand core identity concepts.
- Sign up for a [free 30-day Microsoft Entra ID P1 or P2 trial](https://azure.microsoft.com/trial/get-started-active-directory/).
- [Compare Active Directory and Microsoft Entra ID](https://learn.microsoft.com/en-us/entra/fundamentals/compare).
- Get started with [Microsoft Entra ID for developers](https://learn.microsoft.com/en-us/entra/identity-platform/index.yml).
- Find definitions in the [Microsoft identity platform glossary](https://learn.microsoft.com/en-us/entra/identity-platform/developer-glossary#tenant).
