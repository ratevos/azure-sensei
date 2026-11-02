# Learn about the default DLP policy for Microsoft 365 Copilot location

> Source: https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy  
> Microsoft doc last updated: 2026-03-11


To help you get started with Microsoft Purview data loss prevention (DLP) for the Microsoft 365 Copilot location, Microsoft created a default DLP policy called **Default DLP policy - Protect sensitive M365 Copilot interactions**. The policy is referenced in the **Safeguard sensitive data in Copilot interactions** banner.

Note

See these message center announcements MC1182689 and MC1181998.

Important

The default policy detects sensitive information types (SIT) in user prompts. The **Default DLP policy - Protect sensitive M365 Copilot interactions** is initially configured to **Run the policy in simulation mode** &gt; **Show policy tips while in simulation mode**. This means that the event will only be logged. If you want to block processing of the prompt, you must change the state of the policy to enforce mode.

You can edit this policy to better suit your organization's needs. To [edit the default policy for better performance or to delete it](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy), use an account with **DLP Compliance Management** permissions. For more information, see [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions). For example, you can:

- Change the **Policy mode** to **Turn the policy on immediately** which enforces the block prompt processing action or you can **Leave the policy turned off**.
- Delete it if you don't need it.
- Add or remove sensitive information types to the policy.
- Add or remove users and groups.
- Remove sensitive information types that aren't relevant to your organization to reduce false positives and improve performance.

You can perform these actions through both the simplified experience by selecting **Get started** in the banner and through the full policy editor flow by selecting the policy in the list of policies and selecting the edit button.

Microsoft recommends that you at least edit the policy to turn on **Incident reports** and add your security team as recipients of the email notifications, so they're aware of potential sensitive information being shared in the prompts.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## What does the policy do?

The policy is in simulation mode by default, which means it doesn't block the prompt but generates an alert and sends an email to the admin (if configured). This approach helps you understand the impact of the policy and make necessary adjustments before enforcing it. It initially includes all tenant users and groups in scope and detects these SITs:

- ABA Routing Number
- Argentina National Identity (DNI) Number
- Argentina Unique Tax Identification Key (CUIT/CUIL)
- Australia Bank Account Number
- Australia Driver's License Number
- Australia Medical Account Number
- Australia Passport Number
- Australia Tax File Number
- Australian Business Number
- Australian Company Number
- Austria Tax Identification Number
- Azure SAS
- Azure Storage Account Key (Generic)
- Belgium National Number
- Brazil CPF Number
- Brazil Legal Entity Number (CNPJ)
- Brazil National ID Card (RG)
- Canada Bank Account Number
- Canada Driver's License Number
- Canada Health Service Number
- Canada Personal Health Identification Number (PHIN)
- Canada Social Insurance Number
- Chile Identity Card Number
- Colombia National ID
- Credit Card Number
- Croatia Personal Identification (OIB) Number
- Czech Personal Identity Number
- Denmark Personal Identification Number
- Drug Enforcement Agency (DEA) Number
- Estonia Personal Identification Code
- Finland National ID
- France National ID Card (CNI)
- France Social Security Number (INSEE)
- Germany Identity Card Number
- Germany Tax Identification Number
- Germany Value Added Tax Number
- Greek Tax identification Number
- Hungarian Social Security Number (TAJ)
- India GST Number
- India Permanent Account Number (PAN)
- India Unique Identification (Aadhaar) Number
- International Banking Account Number (IBAN)
- IP Address
- IP Address v4
- IP Address v6
- Ireland Passport Number
- Israel Bank Account Number
- Italy Fiscal Code
- Italy Passport Number
- Japan Bank Account Number
- Japan Passport Number
- Japanese My Number Personal
- Latvia Personal Code
- Lithuania Personal Code
- Luxembourg National Identification Number (Non-natural persons)
- Malaysia Identity Card Number
- Medicare Beneficiary Identifier (MBI) card
- Mexico Unique Population Registry Code (CURP)
- Netherlands Citizen's Service (BSN) Number
- Netherlands Tax Identification Number
- Netherlands Value Added Tax Number
- New Zealand bank account number
- New Zealand Inland Revenue number
- New Zealand Ministry of Health Number
- New Zealand Social Welfare Number
- Norway Identity Number
- Poland National ID (PESEL)
- Poland Tax Identification Number
- Polish REGON Number
- Portugal Tax Identification Number
- Saudi Arabia National ID
- Singapore National Registration Identity Card (NRIC) Number
- Slovakia Personal Number
- Slovenia Tax Identification Number
- South Africa Identification Number
- Spain DNI
- Spain Driver's License Number
- Spain Tax Identification Number
- Sweden National ID
- SWIFT Code
- Taiwan Passport Number
- Thai Population Identification Code
- Turkish National Identification number
- U.K. National Health Service Number
- U.K. National Insurance Number (NINO)
- U.K. Unique Taxpayer Reference Number
- U.S. / U.K. Passport Number
- U.S. Bank Account Number
- U.S. Driver's License Number
- U.S. Individual Taxpayer Identification Number (ITIN)
- U.S. Social Security Number (SSN)

The policy doesn't generate any policy tips for end users, but it does generate an Alert event. It also triggers a low severity email to the admin (added in the policy). Administrators can view the activities and edit the policy details by signing in to the Microsoft Purview portal.

Admins can view this policy in the Microsoft Purview portal. Go to **Data Loss prevention** &gt; **Policies**.
