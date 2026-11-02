# Data Loss Prevention policy reference

> Source: https://learn.microsoft.com/en-us/purview/dlp-policy-reference  
> Microsoft doc last updated: 2026-10-16


Microsoft Purview Data Loss Prevention (DLP) policies have many components to configure. To create an effective policy, you need to understand what the purpose of each component is and how its configuration alters the behavior of the policy. This article provides a detailed anatomy of a DLP policy.

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Recommended reading

1. [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units)
2. [Learn about Microsoft Purview Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp)
3. [Plan for data loss prevention (DLP)](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#plan-for-data-loss-prevention-dlp)- by working through this article you will:
    1. [Identify stakeholders](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#identify-stakeholders)
    2. [Describe the categories of sensitive information to protect](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#describe-the-categories-of-sensitive-information-to-protect)
    3. [Set goals and strategy](https://learn.microsoft.com/en-us/purview/dlp-overview-plan-for-dlp#set-goals-and-strategy)
4. [Collection Policies solution overview](https://learn.microsoft.com/en-us/purview/collection-policies-solution-overview)
5. [Collection policy reference](https://learn.microsoft.com/en-us/purview/collection-policies-policy-reference)
6. [Data Loss Prevention policy reference](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#data-loss-prevention-policy-reference) - this article introduces all the components of a DLP policy and how each one influences the behavior of a policy
7. [Design a DLP policy](https://learn.microsoft.com/en-us/purview/dlp-policy-design) - this article walks you through creating a policy intent statement and mapping it to a specific policy configuration.
8. [Create and Deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy) - This article presents some common policy intent scenarios that you map to configuration options, then it walks you through configuring those options.
9. [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn) - This article introduces you to the lifecycle of alerts from creation, through final remediation and policy tuning. It also introduces you to the tools you use to investigate alerts.

## DLP platform considerations

Also, you need to be aware of these constraints of the platform:

- Maximum number of MIP + MIG policies in a tenant: 10,000
- Maximum size of a DLP policy (100 KB)
- Maximum number of DLP rules:
    - In a policy: Limited by the size of the policy
    - In a tenant: 600
- Maximum size of an individual DLP rule: 100 KB (102,400 characters)
- Generate Incident Report evidence limit: 100, with each SIT evidence, in proportion of occurrence
- Maximum size of text scanned from a file: The first 2 million characters (~2 MB) of extractable text. If a file exceeds this limit, first two million characters are scanned, and a “Document didn’t complete scanning” signal is emitted.
- Maximum number of nested levels of data scanned from a file: The first three levels. If a file exceeds this limit, data in the first three levels are scanned, and a *Document didn’t complete scanning* event is emitted.
- Regex size limit for all matches predicted: 20 KB
- Policy name length limit: 64 characters
- Policy rule length limit: 64 characters
- Comment length limit: 1,024 characters
- Description length limit: 1,024 characters
- Maximum size of Endpoint DLP Settings: 16,384 characters

## Default DLP policies

There are four default DLP policies that are created in every tenant. These policies are designed to help you get started with DLP and provide a baseline level of protection for your organization. You can edit or delete these policies as needed.

### Default Office 365 DLP policy

This policy detects the presence of credit card numbers in externally shared documents and emails. For more information, see [Learn about the default data loss prevention policy for Microsoft 365 Copilot location](https://learn.microsoft.com/en-us/purview/dlp-o365-default-policy)

### Default policy for Teams

The default DLP policy for Teams tracks all the credit card numbers shared internally and externally to the organization. For more information see, [Learn about the default data loss prevention policy in Microsoft Teams](https://learn.microsoft.com/en-us/purview/dlp-teams-default-policy)

### Defaul policy for devices

This policy detects the presence of credit card numbers in files on devices when users perform specific activities (such as printing a file). When detected, the activity is only audited (not blocked). Admins will receive an alert, but policy tips won't be displayed to users. You can edit these actions at any time. For more information, see [Learn about the default DLP policy for device](https://learn.microsoft.com/en-us/purview/endpoint-dlp-default-device-policy).

### Default DLP policy for Microsoft 365 Copilot location

Prevent data leakage and oversharing by restricting Microsoft 365 Copilot and agents from using sensitive info in Copilot interactions. For more information, see [Learn about the default DLP policy for Microsoft 365 Copilot location](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-default-policy).

## Policy templates

There are five types of DLP policy templates across two categories.

### Enterprise applications & devices

- enhanced policies
- policies that can detect and protect types of **Financial** information.
- policies that can detect and protect types of **Medical and health** information.
- policies that can detect and protect types of **Privacy** information.
- A **Custom** policy template that you can use to build your own policy if none of the others meet your organization's needs.

The following table lists all policy templates and the sensitive information types (SIT) that they cover.

| Category | Template | SIT |
| --- | --- | --- |
| Financial | Australia Financial Data | - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) - [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number) - [Australia bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-bank-account-number) - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) |
| Financial | Canada Financial data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number) |
| Financial | France Financial data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number) |
| Financial | Germany Financial Data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number) |
| Financial | Israel Financial Data | - [Israel bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-bank-account-number) - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) |
| Financial | Japan Financial Data | - [Japan bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-bank-account-number) - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) |
| Financial | PCI Data Security Standard (PCI DSS) | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) |
| Financial | Saudi Arabia Anti-Cyber Crime Law | - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) - [International banking account number (IBAN)](https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number) |
| Financial | Saudi Arabia Financial Data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) - [International banking account number (IBAN)](https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number) |
| Financial | UK Financial Data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number) - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) |
| Financial | US Financial Data | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [ABA Routing Number](https://learn.microsoft.com/en-us/purview/sit-defn-aba-routing) |
| Financial | U.S. Federal Trade Commission (FTC) Consumer Rules | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [ABA Routing Number](https://learn.microsoft.com/en-us/purview/sit-defn-aba-routing) |
| Financial | U.S. Gramm-Leach-Bliley Act (GLBA) Enhanced | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) -[U.S. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [U.S. Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-us-physical-addresses) |
| Financial | U.S. Gramm-Leach-Bliley Act (GLBA) | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) |
| Medical and health | Australia Health Records Act (HRIP Act) Enhanced | - [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number) - [Australia medical account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [All Medical Terms And Conditions](https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions) - [Australia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-australia-physical-addresses) |
| Medical and health | Australia Health Records Act (HRIP Act) | - [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number) - [Australia medical account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number) |
| Medical and health | Canada Health Information Act (HIA) | - [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number) - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Medical and health | Canada Personal Health Information Act (PHIA) Manitoba | - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Medical and health | Canada Personal Health Act (PHIPA) Ontario | - [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number) - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Medical and health | U.K. Access to Medical Reports Act | - [U.K. national health service number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number) - [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number) |
| Medical and health | U.S. Health Insurance Act (HIPAA) Enhanced | - [International classification of diseases (ICD-9-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm) - [International classification of diseases (ICD-10-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [All Medical Terms And Conditions](https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions) - [U.S. Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-us-physical-addresses) |
| Medical and health | U.S. Health Insurance Act (HIPAA) | - [International classification of diseases (ICD-9-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm) - [International classification of diseases (ICD-10-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm) |
| Privacy | Australia Privacy Act Enhanced | - [Australia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-drivers-license-number) - [Australia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-passport-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [All Medical Terms And Conditions](https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions) - [Australia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-australia-physical-addresses) |
| Privacy | Australia Privacy Act | - [Australia drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-drivers-license-number) - [Australia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-passport-number) |
| Privacy | Australia Personally Identifiable Information (PII) Data | - [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number) - [Australia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-drivers-license-number) |
| Privacy | Canada Personally Identifiable Information (PII) Data | - [Canada driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-drivers-license-number) - [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number) - [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number) - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Privacy | Canada Personal Information Protection Act (PIPA) | - [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number) - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Privacy | Canada Personal Information Protection Act (PIPEDA) | - [Canada driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-drivers-license-number) - [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number) - [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number) - [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number) - [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number) - [Canada Personal Health Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number) |
| Privacy | France Data Protection Act | - [France national ID card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card) - [France social security number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number) |
| Privacy | France Personally Identifiable Information (PII) Data | - [France social security number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number) - [France driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-france-drivers-license-number) - [France passport number](https://learn.microsoft.com/en-us/purview/sit-defn-france-passport-number) - [France national ID card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card) |
| Privacy | General Data Protection Regulation (GDPR) Enhanced | - [Austria Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-austria-physical-addresses) - [Belgium Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-physical-addresses) - [Bulgaria Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-physical-addresses) - [Croatia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-physical-addresses) - [Cyprus Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-physical-addresses) - [Czech Republic Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-czech-republic-physical-addresses) - [Denmark Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-physical-addresses) - [Estonia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-physical-addresses) - [Finland Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-finland-physical-addresses) - [France Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-france-physical-addresses) - [Germany Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-germany-physical-addresses) - [Greece Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-greece-physical-addresses) - [Hungary Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-physical-addresses) - [Ireland Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-physical-addresses) - [Italy Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-italy-physical-addresses) - [Latvia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-physical-addresses) - [Lithuania Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-physical-addresses) - [Luxembourg Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-physical-addresses) - [Malta Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-malta-physical-addresses) - [Netherlands Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-physical-addresses) - [Poland Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-poland-physical-addresses) - [Portuguese Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-physical-addresses) - [Romania Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-romania-physical-addresses) - [Slovakia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-physical-addresses) - [Slovenia Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-physical-addresses) - [Spain Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-spain-physical-addresses) - [Sweden Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-physical-addresses) - [Austria Social Security Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-social-security-number) - [France Social Security Number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number) - [Greece Social Security Number (AMKA)](https://learn.microsoft.com/en-us/purview/sit-defn-greece-social-security-number) - [Hungarian Social Security Number (TAJ)](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-social-security-number) - [Spain Social Security Number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-spain-social-security-number) - [Austria Identity Card](https://learn.microsoft.com/en-us/purview/sit-defn-austria-identity-card) - [Cyprus Identity Card](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-identity-card) - [Germany Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-identity-card-number) - [Malta Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-identity-card-number) - [France National ID Card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card) - [Greece National ID Card](https://learn.microsoft.com/en-us/purview/sit-defn-greece-national-id-card) - [Finland National ID](https://learn.microsoft.com/en-us/purview/sit-defn-finland-national-id) - [Poland National ID (PESEL)](https://learn.microsoft.com/en-us/purview/sit-defn-poland-national-id) - [Sweden National ID](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-national-id) - [Croatia Personal Identification (OIB) Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-personal-identification-number) - [Czech Personal Identity Number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-personal-identity-number) - [Denmark Personal Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-personal-identification-number) - [Estonia Personal Identification Code](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-personal-identification-code) - [Hungary Personal Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-personal-identification-number) - [Luxemburg National Identification Number natural persons](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-natural-persons) - [Luxemburg National Identification Number (Non-natural persons)](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-non-natural-persons) - [Italy Fiscal Code](https://learn.microsoft.com/en-us/purview/sit-defn-italy-fiscal-code) - [Latvia Personal Code](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-personal-code) - [Lithuania Personal Code](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-personal-code) - [Romania Personal Numerical Code (CNP)](https://learn.microsoft.com/en-us/purview/sit-defn-romania-personal-numeric-code) - [Netherlands Citizen's Service (BSN) Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-citizens-service-number) - [Ireland Personal Public Service (PPS) Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-personal-public-service-number) - [Bulgaria Uniform Civil Number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-uniform-civil-number) - [Belgium National Number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-national-number) - [Spain DNI](https://learn.microsoft.com/en-us/purview/sit-defn-spain-dni) - [Slovenia Unique Master Citizen Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-unique-master-citizen-number) - [Slovakia Personal Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-personal-number) - [Portugal Citizen Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-citizen-card-number) - [Malta Tax ID Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-tax-identification-number) - [Austria Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-tax-identification-number) - [Cyprus Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-tax-identification-number) -[France Tax Identification Number (numéro SPI.)](https://learn.microsoft.com/en-us/purview/sit-defn-france-tax-identification-number) - [Germany Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-tax-identification-number) - [Greek Tax identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-tax-identification-number) - [Hungary Tax identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-tax-identification-number) - [Netherlands Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-tax-identification-number) - [Poland Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-tax-identification-number) - [Portugal Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-tax-identification-number) - [Slovenia Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-tax-identification-number) - [Spain Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-tax-identification-number) - [Sweden Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-tax-identification-number) - [Austria Driver's License](https://learn.microsoft.com/en-us/purview/sit-defn-austria-drivers-license-number) - [Belgium Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-drivers-license-number) - [Bulgaria Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-drivers-license-number) - [Croatia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-drivers-license-number) - [Cyprus Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-drivers-license-number) - [Czech Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-drivers-license-number) - [Denmark Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-drivers-license-number) - [Estonia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-drivers-license-number) - [Finland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-drivers-license-number) - [France Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-drivers-license-number) - [German Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-drivers-license-number) - [Greece Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-drivers-license-number) - [Hungary Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-drivers-license-number) - [Ireland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-drivers-license-number) - [Italy Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-drivers-license-number) - [Latvia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-drivers-license-number) - [Lithuania Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-drivers-license-number) - [Luxemburg Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-drivers-license-number) - [Malta Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-drivers-license-number) - [Netherlands Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-drivers-license-number) - [Poland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-drivers-license-number) - [Portugal Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-drivers-license-number) - [Romania Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-drivers-license-number) - [Slovakia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-drivers-license-number) - [Slovenia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-drivers-license-number) - [Spain Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-drivers-license-number) - [Sweden Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-drivers-license-number) - [Austria Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-passport-number) - [Belgium Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-passport-number) - [Bulgaria Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-passport-number) - [Croatia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-passport-number) - [Cyprus Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-passport-number) - [Czech Republic Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-passport-number) - [Denmark Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-passport-number) - [Estonia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-passport-number) - [Finland Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-passport-number) - [France Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-passport-number) - [German Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-passport-number) - [Greece Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-passport-number) - [Hungary Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-passport-number) - [Ireland Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-passport-number) - [Italy Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-passport-number) - [Latvia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-passport-number) - [Lithuania Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-passport-number) - [Luxemburg Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-passport-number) - [Malta Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-passport-number) - [Netherlands Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-passport-number) - [Poland Passport](https://learn.microsoft.com/en-us/purview/sit-defn-poland-passport-number) - [Portugal Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-passport-number) - [Romania Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-passport-number) - [Slovakia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-passport-number) - [Slovenia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-passport-number) - [Spain Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-passport-number) - [Sweden Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-passport-number) - [EU Debit Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) |
| Privacy | General Data Protection Regulation (GDPR) | - [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number) - [EU driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-drivers-license-number) - [EU national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-national-identification-number) - [EU passport number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-passport-number) - [EU social security number or equivalent identification](https://learn.microsoft.com/en-us/purview/sit-defn-eu-social-security-number-equivalent-identification) - [EU Tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-tax-identification-number) |
| Privacy | Germany Personally Identifiable Information (PII) Data | - [Germany driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-drivers-license-number) - [Germany passport number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-passport-number) |
| Privacy | Israel Personally Identifiable Information (PII) Data | - [Israel national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number) |
| Privacy | Israel Protection of Privacy | - [Israel national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number) - [Israel bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-bank-account-number) |
| Privacy | Japan Personally Identifiable Information (PII) Data enhanced | - [Japan Social Insurance Number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number) - [Japan My Number - Personal](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-personal) - [Japan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-passport-number) - [Japan driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-drivers-license-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [Japan Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-all-physical-addresses) |
| Privacy | Japan Personally Identifiable Information (PII) Data | - [Japan resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-resident-registration-number) - [Japan Social Insurance Number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number) |
| Privacy | Japan Protection of Personal Information Enhanced | - [Japan Social Insurance Number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number) - [Japan My Number - Personal](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-personal) - [Japan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-passport-number) - [Japan driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-drivers-license-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [Japan Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-all-physical-addresses) |
| Privacy | Japan Protection of Personal Information | - [Japan resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-resident-registration-number) - [Japan Social Insurance Number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number) |
| Privacy | Saudi Arabia Personally Identifiable (PII) Data | - [Saudi Arabia National ID](https://learn.microsoft.com/en-us/purview/sit-defn-saudi-arabia-national-id) |
| Privacy | U.K. Data Protection Act | - [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) |
| Privacy | U.K. Privacy and Electronic Communications Regulations | - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) |
| Privacy | U.K. Personally Identifiable Information (PII) Data | - [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) |
| Privacy | U.K. Personal Information Online Code of Practice (PIOCP) | - [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number) - [U.K. national health service number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number) - [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code) |
| Privacy | U.S Patriot Act Enhanced | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [U.S. Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-us-physical-addresses) |
| Privacy | U.S. Patriot Act | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) |
| Privacy | U.S. Personally Identifiable Information (PII) Data Enhanced | - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [U.S. Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-us-physical-addresses) |
| Privacy | U.S. Personally Identifiable Information (PII) Data | - [U.S. Individual Taxpayer Identification Number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) |
| Privacy | U.S. State Breach Notification Laws Enhanced | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) -[U.S. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) - [All Full Names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names) - [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number) - [All Medical Terms And Conditions](https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions) |
| Privacy | U.S. State Breach Notification Laws | - [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number) - [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number) -[U.S. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number) - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) |
| Privacy | U.S. State Social Security Number Confidentiality Laws | - [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number) |

### Inline web traffic policies

- A **Custom** policy template that you can use to build your own policy.

## Policy scoping

See, [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units) to make sure you understand the difference between an unrestricted admin and an administrative unit restricted admin.

DLP policies are scoped at two different levels. The first level applies unrestricted admin scope policies to all of the following in your organization (depending on the locations that are selected) or to subgroups of your organization, called Administrative Unit restricted policies:

- users
- groups
- distribution groups
- accounts
- sites
- cloud app instances
- on-premises repositories
- Fabric and Power BI workspaces

At this level, an administrative unit restricted admin will only be able to pick from the administrative units that they're assigned to. DLP support admin unit scoping for some of the locations protected under Enterprise applications & devices.

The second level of DLP policy scoping is by the locations that DLP supports. At this level, both unrestricted and administrative unit restricted administrators see only the users, distribution groups, groups, and accounts that were included in the first level of policy scoping and that are available for that location.

### Support for adding SharePoint sites to Administrative Units

Microsoft Purview supports [adding SharePoint sites to existing administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units#sharepoint-site-support-for-administrative-units). When you assign a DLP policy for the SharePoint location to an administrative unit, the policy will only apply to the sites that are part of that administrative unit. The option to further edit the scope to include or exclude specific sites isn't available. The policy applies to all sites that are part of the administrative unit.

Here's an example use case:

Contoso has created an Entra ID administrative unit for the engineering department and has assigned certain administrators to manage the users and groups for that department. The engineering department has a SharePoint site that is used to store sensitive information. Contoso wants to ensure that the DLP policy for the engineering department SharePoint sites only applies to the SharePoint site that is part of the administrative unit. By assigning the DLP policy to the administrative unit, the policy will only apply to the SharePoint site that is part of that administrative unit. Also, the administrative unit restricted administrator will only be able to manage the DLP policy for that site and only see policy match result data for the administrative unit in activity explorer and the alert dashboard.

### Unrestricted policies

Unrestricted policies are created and managed by users in these role groups:

- Compliance administrator
- Compliance data administrator
- Information Protection
- Information Protection Admin
- Security administrator

See, the [Permissions](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#permissions) article for more details.

Unrestricted administrators can manage all policies and see all the alerts and events that flow from policy matches into the [Alerts dashboard](https://learn.microsoft.com/en-us/purview/dlp-alerts-dashboard-get-started) and [DLP Activity Explorer](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp#dlp-activity-explorer-and-reports).

### Administrative unit restricted policies

Administrative units are subsets of your Microsoft Entra ID directory and are created for the purposes of managing collections of users, groups, distribution groups, and accounts. These collections are typically created along business group lines or geopolitical areas. Administrative units have a delegated administrator who is associated with an administrative unit in the role group. These are called administrative unit restricted admins.

DLP supports associating policies with administrative units. See [Administrative units](https://learn.microsoft.com/en-us/purview/purview-admin-units) for implementation details in the Microsoft Purview portal. Administrative unit admins need to be assigned to one of the same roles or role groups as administrators of unrestricted DLP policies in order to create and manage DLP policies for their administrative unit.

| DLP Administrative Role Group | Can |
| --- | --- |
| Unrestricted administrator | - create and scope DLP policies to entire organization- edit all DLP policies - create and scope DLP policies to administrative units - view all alerts and events from all DLP policies |
| Administrative Unit Restricted administrator - must be a member of/[assigned to a role group/role](https://learn.microsoft.com/en-us/purview/purview-permissions#add-users-or-groups-to-a-microsoft-purview-built-in-role-group) that can administer DLP | - create and scope DLP policies only to the administrative unit that they're assigned to - edit DLP policies that are associated to their administrative unit - view alerts and events only from the DLP policies that are scoped to their administrative unit |

### Locations

A DLP policy can find and protect items that contain sensitive information across multiple locations.

| Location | Supports Administrative Units | Include/Exclude scope | Data state | Other prerequisites |
| --- | --- | --- | --- | --- |
| Exchange Online | Yes | - distribution groups assigned or dynamic  - security groups  - non email enabled security groups assigned or dynamic)  - Microsoft 365 groups assigned or dynamic | data-in-motion | No |
| SharePoint | Yes | site locations and, in preview, adaptive scopes at the policy level. If the policy is scoped to an administrative unit that includes SharePoint sites, the policy will only apply to all sites in the administrative unit, no further scoping is possible | data-at-rest  data-in-use | No |
| OneDrive | Yes | - Distribution groups  - Security groups  - Non email enabled security groups  - Microsoft 365 groups (Group members only, not the group as an entity) | data-at-rest  data-in-use | No |
| Teams chat and channel messages | Yes | - Distribution groups - Security groups  - Mail-enabled security groups  - Microsoft 365 groups (Group members only, not the group as an entity) | data-in-motion  data-in-use | See [Scope of DLP protection](https://learn.microsoft.com/en-us/purview/dlp-microsoft-teams#scope-of-dlp-protection) |
| Instances | No | Cloud app instance | data-at-rest | - [Use data loss prevention policies for non-Microsoft cloud apps](https://learn.microsoft.com/en-us/purview/dlp-use-policies-non-microsoft-cloud-apps#use-data-loss-prevention-policies-for-non-microsoft-cloud-apps) |
| Devices | Yes | - Distribution groups  - Security groups  - Non-email enabled security groups  - Microsoft 365 groups (Group members only, not the group as an entity)  - Dynamic groups (Security group: Users/Devices and Microsoft 365 group: Users) | data-in-use  data-in-motion | - [Learn about Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about)- [Get started with Endpoint data loss prevention](https://learn.microsoft.com/en-us/purview/endpoint-dlp-getting-started)- [Configure device proxy and internet connection settings for Microsoft Purview Endpoint DLP](https://learn.microsoft.com/en-us/purview/device-onboarding-configure-proxy#configure-device-proxy-and-internet-connection-settings-for-microsoft-purview-endpoint-dlp) |
| On-premises repositories (file shares and SharePoint) | No | Repository | data-at-rest | - [Learn about the data loss prevention on-premises repositories](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn) - [Get started with data loss prevention for on-premises repositories](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-get-started#get-started-with-data-loss-prevention-for-on-premises-repositories) |
| Fabric and Power BI | No | Workspaces | data-in-use | No |
| Non-Microsoft connected apps (preview) | No | Cloud app instance | data-at-rest | - [Use DLP and sensitivity label policies for non-Microsoft connected apps](https://learn.microsoft.com/en-us/purview/dlp-non-microsoft-connected-applications) - Only available in the **Custom** policy template  - Set up a [Microsoft Defender for Cloud Apps connector](https://learn.microsoft.com/en-us/en-us/defender-cloud-apps/enable-instant-visibility-protection-and-governance-actions-for-your-apps) |
| Microsoft Copilot and Chat (preview) | [Yes (rolling out)](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about#admin-units) | Account or Distribution group | data-at-rest  data-in-use | - Only available in the **Custom** policy template |
| Managed cloud apps | No | Account or Distribution group | data-in-motion | - Only available in the **Custom** policy template |
| Unmanaged cloud apps | No | Account or Distribution group | data-in-motion | - Only available in the **Custom** policy template |

Note

In the **Devices** location, the **Devices and device groups** setting supports only **Audit or restrict activities on devices**. You can't use it with **Audit or restrict activities when users access sensitive sites in the Microsoft Edge browser on Windows devices** under **Rule Actions**.

#### Exchange location scoping

If you choose to include specific distribution groups in Exchange, the DLP policy is scoped to the emails sent by members of that group or sent to members of that group. Similarly, excluding a distribution group excludes all the emails sent by the members of that distribution group or from policy evaluation.

| Group Type | Membership Type | Supported during Policy Creation | Supported during Rule Evaluation | Notes |
| --- | --- | --- | --- | --- |
| Non-Mail Enabled Security Groups | Assigned | Yes | No | Enabled for specific customers only |
| Non-Mail Enabled Security Groups | Dynamic | Yes | No |  |
| Mail-Enabled Security Groups | Assigned | Yes | Yes |  |
| Distribution Groups | Assigned | Yes | Yes |  |
| Distribution Groups | Dynamic | Yes | Yes |  |
| Microsoft 365 Groups | Assigned | Yes | Yes |  |
| Microsoft 365 Groups | Dynamic | Yes | Yes |  |
| Adaptive Scopes | Dynamic | No | No |  |

| Sender is | Recipient is | Resultant behavior |
| --- | --- | --- |
| In scope | N/A | Policy is applied |
| Out of scope | In scope | Policy isn't applied |

##### Exchange location scope calculation

Here's an example of how Exchange location scope is calculated:

Say you have four users in your org and two distribution groups that you use for defining Exchange location inclusion and exclusion scopes. Group membership is set up like this:

| Distribution Group | Membership |
| --- | --- |
| Group1 | User1, User2 |
| Group2 | User2, User3 |
| *No group* | User4 |

| Include setting | Exclude setting | Policy applies to | Policy doesn't apply to | Explanation of behavior |
| --- | --- | --- | --- | --- |
| All | None | All senders in the Exchange org (User1, User2, User3, User4) | N/A | When neither are defined, all senders are included |
| Group1 | None | Member senders of Group1 (User1, User2) | All senders who aren't members of Group1 (User3, User4) | When one setting is defined and the other isn't, the defined setting is used |
| All | Group2 | All senders in the Exchange org who aren't members of Group2 (User1, User4) | All senders who are members of Group2 (User2, User3) | When one setting is defined and the other isn't, the defined setting is used |
| Group1 | Group2 | User1 | User2, User3, User4 | Exclude overrides include |

You can choose to scope a policy to the members of distribution lists, dynamic distribution groups, and security groups. A DLP policy can contain no more than 50 such inclusions and exclusions.

#### OneDrive location scoping

When scoping a policy for OneDrive locations, in addition to applying your DLP policies to all users and groups in your organization, you can limit the scope of a policy to specific users and groups. DLP supports scoping policies to up to 100 individual users.

For instance, if you want to include more than 100 users, you must first put those users in distribution groups or security groups, as appropriate. You can then scope your policy to up to 50 groups.

In some cases, you might want to apply a policy to one or two groups, plus two or three individual users who don't belong to either of those groups. Here, the best practice is to **put those two or three individuals into a group of their own**. This is the only way to make sure that the policy is scoped to all intended users.

The reason for this is that, when you list only users, DLP adds all of the users specified to the policy scope. Similarly, when you add only groups, DLP adds all the members of all the groups to the policy scope.

Say you have the following groups and users:

| Distribution Group | Membership |
| --- | --- |
| Group1 | User1, User2 |
| Group2 | User2, User3 |

If you limit the scope of a policy to *only* users or *only* groups, the DLP applies the policy to users as illustrated in the following table:

| Specified scope | DLP Scope evaluation behavior | Users in scope |
| --- | --- | --- |
| **(Users only)** User1  User2 | DLP takes the union of the specified users | User1, User2 |
| **(Groups only)** Group1  Group2 | DLP takes the union of the specified groups | User1, User2, User3 |

However, when users and groups are mixed in the scoping configuration, things get complicated. Here's why: DLP only scopes policies to users to **the intersection** of the listed groups and users.

DLP uses the following order of operations when determining which users and groups to include in the scope:

1. Evaluate the union of group membership
2. Evaluate the union of users
3. Evaluate the intersection of group members and users, that is, where the results overlap

It then applies the scope of the policy to the intersection of group members and users.

Let's extend our example, working with the same set of groups, and let's add User4, who isn't in a group:

| Distribution Group | Membership |
| --- | --- |
| Group1 | User1, User2 |
| Group2 | User2, User3 |
| *No group* | User 4 |

The following table explains how policy scoping works in cases where users and groups are both included in the scoping instructions.

| Specified scope | DLP Scope evaluation behavior | Users in scope |
| --- | --- | --- |
| Group1  Group2  User3 User4 | **First evaluation: Union of groups:**`(Group1 + Group2) = User1, User2, User3`**Second evaluation: Union of users:**`(User3 + User4) = User3, User4`**Third evaluation: Intersection of groups and Users (the overlap):**`(Group1 + Group2) = User1, User2, User3``(User3 + User4) = User3, User4` | **User3** (User3 is the only user that appears in the results of both the first and second evaluations.) |
| Group1  Group2  User1  User3  User4 | **First evaluation: Union of groups:**`(Group1 + Group2) = User1, User2, User3`**Second evaluation: Union of users:**`(User1 + User3 + User4) = User1, User3, User4`**Third evaluation: Intersection of groups and Users (the overlap):**`(Group1 + Group2) = User1, User3``(User1 + User3, User4) = User1, User3, User4` | **User1**, **User3** (These are the only users that appear in the results of both the first and second evaluations.) |

#### SharePoint location scoping

When scoping a policy for SharePoint locations, you can limit the scope of a policy to specific SharePoint sites and adaptive scopes. DLP supports scoping policies to up to 100 sites.

### Device scoping

Microsoft Purview Data Loss Prevention (DLP) policies that include the **Devices** location can be scoped by **users** and by **devices**. A policy is enforced on an endpoint only when *both* the user and the device are included in the policy scope. If a user is in scope but the device is not, the policy isn’t applied. Similarly, if a device is in scope but the user is not, the policy isn’t applied.

Use 101.25072 or higher build for this feature support on macOS.

Device scoping does not support Microsoft Entra registered.

Here's how to configure the scope of a DLP policy for different outcomes.

| If you want to target the policy to... | Set user scope to... | Set device scope to... | Example use case |
| --- | --- | --- | --- |
| All users on all onboarded devices | **All users and groups** | **All devices and device groups** | Use this for general enforcement of DLP policies on all devices in your organization. This is the default setting for DLP policies. |
| All users on specific devices | **All users and groups** | either **All devices and device groups** with **Exclude devices and device groups** and add the devices to be excluded or **Specific devices and device groups** and add the devices to be included | Use this to apply a restrictive policy to kiosk devices that will be used by multiple users. |
| Specific users on all onboarded devices | either **All users and groups** with **Exclude users and groups** and add the users to be excluded or **Specific users and groups** and add the users to be included | **All devices and device groups** | Use this to help control data leakage by specific users on all devices in your organization. |
| Specific users on specific devices | **Specific users and groups** | **Specific devices and device groups** | Say you have special use devices in payroll that are used for printing checks and there are only a few accounts that are allowed to use those devices for printing checks. You can scope a restrictive endpoint DLP policy to those user accounts on those specific devices |

### Location support for how content can be defined

DLP policies detect sensitive items by matching them to a sensitive information type (SIT), or to a sensitivity label or a retention label. Each location supports different methods of defining sensitive content. How content can be defined when you combine locations in a policy, can change from how it can be defined when limited to a single location.

Important

When you select multiple locations for a policy, a "no" value for a content definition category takes precedence over "yes" value. For example, when you select SharePoint sites only, the policy supports detecting sensitive items by one or more of SIT, by sensitivity label or by retention label. But, when you select SharePoint sites ***and*** Teams chat and channel messages locations, the policy will only support detecting sensitive items by SIT.

| Location | Content can be defined by SIT | Content can be defined sensitivity label | Content can be defined by retention label |
| --- | --- | --- | --- |
| Exchange email online | Yes | Yes | No |
| SharePoint in Microsoft 365 sites | Yes | Yes | Yes |
| OneDrive for work or school accounts | Yes | Yes | Yes |
| Teams Chat and Channel messages | Yes | No | No |
| Devices | Yes | Yes | No |
| Instances | Yes | Yes | Yes |
| On-premises repositories | Yes | Yes | No |
| Fabric and Power BI | Yes | Yes | No |
| Microsoft 365 Copilot (preview) | No | Yes | No |
| Managed cloud apps | Yes | No | No |
| Unmanaged cloud apps | Yes | Yes | No |

DLP supports using trainable classifiers as a condition to detect sensitive information. Content can be defined by trainable classifiers in Exchange, SharePoint sites, OneDrive accounts, Teams Chat and Channels, Devices, and unmanaged cloud apps. For more information, see [Trainable Classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-learn-about).

Note

DLP supports detecting sensitivity labels on emails and attachments. For more information, see [Use sensitivity labels as conditions in DLP policies](https://learn.microsoft.com/en-us/purview/dlp-sensitivity-label-as-condition#use-sensitivity-labels-as-conditions-in-dlp-policies).

## Rules

Rules are the business logic of DLP policies. They consist of:

- **Conditions** that when matched, trigger the policy
- **Actions** that determine the activities included and outcomes of a match.
- **User notifications** to inform your users when they're doing something that triggers a policy and help educate them on how your organization wants sensitive information treated
- **User Overrides** when configured by an admin, allow users to selectively override a blocking action
- **Incident reports** that notify admins and other key stakeholders when a rule match occurs
- **Additional options** which define the priority for rule evaluation and can stop further rule and policy processing.

A policy contains one or more rules. Rules are executed sequentially, starting with the highest-priority rule in each policy.

### How DLP classification works

DLP evaluates an item for sensitive information when the item is created, read, or modified. Evaluation is also initiated by [on demand classification](https://learn.microsoft.com/en-us/purview/on-demand-classification). However, events such as **DLP Rule Matched** only appear in Audit log or activity explorer when a user attempts an activity that matches a DLP policy.

Here's a list of some of the user activities that DLP can monitor and take actions on:

- Text upload via Microsoft Edge browser using integrated capabilities
- File upload via Microsoft Edge browser using integrated capabilities
- File download via Microsoft Edge browser using integrated capabilities
- Cut/copy data via Microsoft Edge browser using integrated capabilities
- Paste data via Microsoft Edge browser using integrated capabilities
- Print data via Microsoft Edge browser using integrated capabilities
- Print data from other locations
- Copy to removable media
- Copy to network share
- Copy to clipboard
- Transfer using Bluetooth
- File accessed by unallowed app
- Paste to browsers other than Microsoft Edge
- Print data
- Transfer using remote desktop
- An item that is created, read, or modified will match a DLP rule and policy on the client if the conditions and user activity are met. This is audited as file activity, such as FileRead, or FileRenamed.
- If an activity is met, then a DLP rule match event appears in activity explorer as a 'DLP Rule Matched' event. An event describing the mode of egress will also be generated.
- Policies take actions and actions are different from conditions. A rule can match on a file even if no actions are performed.

### The priority by which rules are evaluated and applied

#### Hosted service locations

For the hosted service locations, like Exchange, SharePoint, and OneDrive, each rule is assigned a priority in the order in which it's created. This means that the rule created first has first priority, the rule created second has second priority, and so on.



When content is evaluated against rules, the rules are processed in priority order. If content matches multiple rules, the first rule evaluated that has the *most* restrictive action is enforced. For example, if content matches all of the following rules, *Rule 3* is enforced because it's the highest priority, most restrictive rule:

- Rule 1: only notifies users
- Rule 2: notifies users, restricts access, and allows user overrides
- *Rule 3: notifies users, restricts access, and doesn't allow user overrides*
- Rule 4: restricts access

Rules 1, 2, and 4 would be evaluated, but not applied. In this example, matches for all of the rules are recorded in the audit logs and shown in the DLP reports, even though only the most restrictive rule is applied.

You can use a rule to meet a specific protection requirement, and then use a DLP policy to group together common protection requirements, such as all of the rules needed to comply with a specific regulation.

For example, you might have a DLP policy that helps you detect the presence of information subject to the Health Insurance Portability and Accountability Act (HIPAA). This DLP policy could help protect HIPAA data (the "what") across all SharePoint sites and all OneDrive sites (the "where") by finding any document containing this sensitive information that's shared with people outside your organization (the conditions) and then blocking access to the document and sending a notification (the actions). These requirements are stored as individual rules and grouped together as a DLP policy to simplify management and reporting.



#### For endpoints

When an item matches multiple DLP rules, DLP goes uses through a complex algorithm to decide which actions to apply. Endpoint DLP applies the aggregate or sum of most restrictive actions. DLP uses these factors when making the calculation.

**Policy priority order** When an item matches multiple policies and those policies have identical actions, the actions from the highest priority policy are applied.

**Rule priority order** When an item matches multiple rules in a policy and those rules have identical actions, the actions from the highest priority rule are applied.

[**Mode of the policy**](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy#policy-state) When an item matches multiple policies and those policies have identical actions, the actions from all policies that are in **Turn it on** state (enforce mode) are applied preferentially over the policies in **Run the policy in simulation mode with policy tips** and **Run the policy in simulation mode** state.

##### Run the policy in simulaiton mode changes the action that's applied at runtime

When policies are matched and in the **Run the policy in simulation** state, they apply different actions than they would if they are in the **Turn it on right away** state.

| Action configured in the policy is | When policy state is**Run the policy in simulation mode**and**Show policy tips in simulation mode**is**off**, the applied action is | When policy state is**Run the policy in simulation mode**and**Show policy tips while in simulation mode**is**on**, the applied action is |
| --- | --- | --- |
| Block | Audit | Block with override |
| Block with override | Audit | Block with override |
| Audit only | Audit | Audit |
| Allow | Allow | Allow |

**Action** When an item matches multiple policies and those policies differ in actions, the aggregate or sum of the most restrictive actions are applied.

**[Authorization groups](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-manage-printer-access)** configuration When an item matches multiple policies and those policies differ in action, the aggregate, or sum, of the most restrictive actions are applied.

**override options** When an item matches multiple policies and those policies differ in the override option, actions are applied in this order:

*No override* &gt; *Allow override*

Here are scenarios that illustrate the runtime behavior. For the first three scenarios, you have three DLP policies configured like this:

| Policy name | Condition to match | Action | Policy priority |
| --- | --- | --- | --- |
| ABC | Content contains credit card number | Block print, audit all other user egress activities | 0 |
| MNO | Content contains credit card number | Block copy to USB, audit all other user egress activities | 1 |
| XYZ | Content contains U.S. social security number | Block copy to clipboard, audit all other user egress activities | 2 |

##### Item contains credit card numbers

An item on a monitored device contains credit card numbers, so it matches policy ABC and policy MNO. Both ABC and MNO are in *Turn it on* mode.

| Policy | Cloud egress action | Copy to clipboard action | Copy to USB action | Copy to network share action | Unallowed apps action | Print action | Copy via Bluetooth action | Copy to remote desktop action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC | Audit | Audit | Audit | Audit | Audit | **Block** | Audit | Audit |
| MNO | Audit | Audit | **Block** | Audit | Audit | Audit | Audit | Audit |
| Actions applied at runtime | Audit | Audit | **Block** | Audit | Audit | **Block** | Audit | Audit |

##### Item contains credit card numbers and U.S. social security numbers

An item on a monitored device contains credit card numbers and U.S. social security numbers, so this item matches policy ABC, policy MNO, and policy XYZ. All three policies are in *Turn it on* mode.

| Policy | Cloud egress action | Copy to clipboard action | Copy to USB action | Copy to network share action | Unallowed apps action | Print action | Copy via Bluetooth action | Copy to remote desktop action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC | Audit | Audit | Audit | Audit | Audit | **Block** | Audit | Audit |
| MNO | Audit | Audit | **Block** | Audit | Audit | Audit | Audit | Audit |
| XYZ | Audit | **Block** | Audit | Audit | Audit | **Block** | Audit | Audit |
| Actions applied at runtime | Audit | **Block** | **Block** | Audit | Audit | **Block** | Audit | Audit |

##### Item contains credit card numbers, different policy state

An item on a monitored device contains credit card number, so it matches policy ABC and policy MNO. Policy ABC is in *Turn it on* mode and policy *MNO* is in **Run the policy in simulation mode** state.

| Policy | Cloud egress action | Copy to clipboard action | Copy to USB action | Copy to network share action | Unallowed apps action | Print action | Copy via Bluetooth action | Copy to remote desktop action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC | Audit | Audit | Audit | Audit | Audit | **Block** | Audit | Audit |
| MNO | Audit | Audit | **Block** | Audit | Audit | Audit | Audit | Audit |
| Actions applied at runtime | Audit | Audit | Audit | Audit | Audit | **Block** | Audit | Audit |

##### Item contains credit card numbers, different override configuration

An item on a monitored device contains credit card number, so it matches policy ABC and policy MNO. Policy ABC is in *Turn it on* state and policy *MNO* is in *Turn it on* state. They have different *Override* actions configured.

| Policy | Cloud egress action | Copy to clipboard action | Copy to USB action | Copy to network share action | Unallowed apps action | Print action | Copy via Bluetooth action | Copy to remote desktop action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC | Audit | Audit | **Block with override** | Audit | Audit | **Block** | Audit | Audit |
| MNO | Audit | Audit | **Block without override** | Audit | Audit | Audit | Audit | Audit |
| Actions applied at runtime | Audit | Audit | **Block without override** | Audit | Audit | **Block** | Audit | Audit |

##### Item contains credit card numbers, different authorization groups configuration

An item on a monitored device contains credit card number, so it matches policy ABC and policy MNO. Policy ABC is in *Turn it on* state and policy *MNO* is in *Turn it on* state. They have different *authorization group* actions configured.

| Policy | Cloud egress action | Copy to clipboard action | Copy to USB action | Copy to network share action | Unallowed apps action | Print action | Copy via Bluetooth action | Copy to remote desktop action |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ABC | Audit | Audit | **Auth group A - Block** | Audit | Audit | **Auth group A - Block** | Audit | Audit |
| MNO | Audit | Audit | **Auth group A - Block with override** | Audit | Audit | **Auth group B - block** | Audit | Audit |
| Actions applied at runtime | Audit | Audit | **Auth group A - Block** | Audit | Audit | **Auth group A - Block, Auth group B - Block** | Audit | Audit |

### Conditions

Conditions are where you define what you want the rule to look for and the context in which those items are being used. They tell the rule: when you find an item that looks like *this* and is being used like *that*—it's a match and the rest of the actions in the policy should be taken on it. You can use conditions to assign different actions to different risk levels. For example, sensitive content shared internally might be lower risk and require fewer actions than sensitive content shared with people outside the organization.

Note

Users who have non guest accounts in a host organization's Active Directory or Microsoft Entra tenant are considered as people inside the organization.

#### Content contains

All locations support the **Content contains** condition. You can select multiple instances of each content type and further refine the conditions by using the **Any of these** (logical OR) or **All of these** (logical AND) operators:

- [sensitive information types](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about#learn-about-sensitive-information-types)
- [sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels)
- [retention labels](https://learn.microsoft.com/en-us/purview/retention#using-a-retention-label-as-a-condition-in-a-dlp-policy)
- [Trainable Classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-learn-about)

The rule will only look for the presence of any **sensitivity labels** and **retention labels** you pick.

SITs have a predefined [**confidence level**](https://learn-video.azurefd.net/vod/player?id=ace82ff5-4e4c-4542-b0f4-09d8d3335486) which you can alter if needed. For more information, see [More on confidence levels](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about#more-on-confidence-levels).

Important

SITs have two different ways of defining the maximum unique instance count parameters. To learn more, see [Instance count supported values for SIT](https://learn.microsoft.com/en-us/purview/sit-limits#instance-count-supported-values-for-sit).

> 
> Duplicate SIT words across different attachments in a single email are only counted once toward the unique count.

#### Adaptive Protection in Microsoft Purview

Adaptive protection integrates Microsoft Purview Insider Risk Management risk profiles into DLP policies so that DLP can help protect against dynamically identified risky behaviors. When configured in insider risk management, the **Insider risk level for Adaptive Protection is** will show up as condition for Exchange Online, Devices, Teams, and unmanaged cloud apps locations. Refer to [Learn about Adaptive Protection in Data Loss Prevention](https://learn.microsoft.com/en-us/purview/dlp-adaptive-protection-learn) for more details.

##### Conditions that Adaptive Protection supports

- Insider risk level for Adaptive Protection is supported with these values:
- Elevated risk level
- Moderate risk level
- Minor risk level

#### Condition context

The available context options change depending on which location you choose. If you select multiple locations, only the conditions that the locations have in common are available.

##### Conditions Exchange supports

Note

DLP policies for Exchange scan non system generated emails and journaling emails.

- Content contains
- Insider risk level for Adaptive Protection is
- Content isn't labeled
- Content is shared from Microsoft 365
- Content is received from
- Sender IP address is
- Header contains words or phrases
- Sender AD Attribute contains words or phrases
- Content character set contains words
- Header matches patterns
- Sender AD Attribute matches patterns
- Recipient AD Attribute contains words or phrases
- Recipient AD Attribute matches patterns
- Recipient is member of
- Document property is
- Any email attachment's content could not be scanned
- Document or attachment is password protected
- Has sender overridden the policy tip
- Sender is a member of
- Any email attachment's content didn't complete scanning
- Recipient address contains words
- File extension is
- Recipient domain is
- Recipient is
- Sender is
- Sender domain is
- Recipient address matches patterns
- Document name contains words or phrases
- Document name matches patterns
- Subject contains words or phrases
- Subject matches patterns
- Subject or body contains words or phrases
- Subject or body matches patterns
- Sender address contains words
- Sender address matches patterns
- Document size equals or is greater than
- Document content contains words or phrases
- Document content matches patterns
- Message size equals or is greater than
- Message type is
- Message importance is

Tip

For more information on the conditions that Exchange supports, including PowerShell values, see: [Data loss prevention Exchange conditions and actions reference](https://learn.microsoft.com/en-us/purview/dlp-exchange-conditions-and-actions).

##### Conditions SharePoint supports

- Content contains
- Content is shared from Microsoft 365
- Document property is
- Document could not be scanned
- Document or attachment is password protected
- Document didn't complete scanning
- File extension is
- Document name contains words or phrases
- Document size equals or is greater than
- Document created by
- Document creation date is on or after
- Document creation date is on or before
- Document modification date is on or after
- Document modification date is on or before

##### Conditions OneDrive accounts support

- Content contains
- Content is shared from Microsoft 365
- Document property is
- Document could not be scanned
- Document or attachment is password protected
- Document didn't complete scanning
- File extension is
- Document name contains words or phrases
- Document size equals or is greater than
- Document created by
- Document is shared
- Document creation date is on or after
- Document creation date is on or before
- Document modification date is on or after
- Document modification date is on or before

##### Conditions Teams chat and channel messages support

- Content contains
- Insider risk level for Adaptive Protection is
- Content is shared from Microsoft 365
- Recipient domain is
- Recipient is
- Sender is
- Sender domain is

##### Conditions managed cloud apps support

- Content contains
- File extension is
- Document size equals or is greater than
- Managed or unmanaged devices (the cut/copy data, paste data, and print data activities only support the managed or unmanaged devices condition).

##### Conditions unmanaged cloud apps support

- Content contains
- Content not fully scanned
- File cannot be scanned
- File extension is
- File is not labeled
- File is password protected
- File size is greater than
- File type is
- Insider risk level for Adaptive Protection is
- URL contains text (preview)

**(Preview)** The **URL contains text** condition detects when the URL of the unmanaged cloud app contains specified text strings. You can use it as a condition to scope DLP rules to specific URLs, or as an exception to exclude specific URLs from policy enforcement. For example, you can create a rule that blocks uploading sensitive data to any GitHub URL that doesn't contain your organization's name while allowing uploads to your organization's GitHub repositories. This condition is supported for browser and network detection and doesn't require devices to be onboarded to endpoint DLP.

Important

Encrypted files can't be inspected for sensitive info types or trainable classifiers.

##### Conditions supported for Endpoints

- **Content contains:** Specifies content to be detected. For details on supported file types, see [Files scanned for content](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#files-monitored-via-policy).
- **Content is not labeled:** Detects content that doesn't have a sensitivity label applied. To help ensure only supported file types are detected, you should use this condition with the **File extension is** or **File type is** conditions. PDF and Office files are supported:

    | File Type | Format | Monitored file extensions |
    | --- | --- | --- |
    | Word processing | Word, PDF | .doc, .docx, .docm, .dot, dotx, .dotm, .docb, .pdf |
    | Spreadsheet | Excel, CSV, TSV | .xls, .xlsx, .xlt, .xlm, .xlsm, xltx, xltm, xlsb, .xlw, .csv, .tsv |
    | Presentation | PowerPoint | .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx |
- **Document could not be scanned:** Applies to files that can't be scanned for one of the following reasons:

    - File contains one or more transient text-extraction errors
    - File is password-protected
    - File size exceeds the supported limit (Maximum file sizes: 64 MB for uncompressed files; 256 MB for compressed files)
    - Microsoft classification engine (MCE) timeout or failure
- **Document name contains words or phrases:** Detects documents with file names that contain any of the words or phrases you specify, for example: `file`, `credit card`, `patent`, etc.
- **Document name matches patterns:** Detects documents where the file name matches specific patterns. The evaluation considers the entire path of the document, not just the document’s name. The pattern is checked as a string match, meaning it can match any part of the document path. To define the patterns, use wild cards.

Note

Due to potential performance issues, this condition will gradually be phased out from Purview Endpoint DLP. We recommend using the 'Document name contains words or phrases' condition instead.

- **Document or attachment is password protected:** Detects only protected files that are open. The following files are supported:
- Archive files (ZIP, .7z, RAR)
    - Office files
    - PDFs
    - Symantec PGP encrypted files

- **Document size equals or is greater than:** Detects documents with file sizes that are equal to or greater than the specified value. DLP only supports content inspection for files less than 64 MB.

    Important

    We recommend setting this condition to detect items that are larger than 10KB
- **File type is:** Detects the following file types:

    | File type | Apps | Monitored file extensions |
    | --- | --- | --- |
    | Word processing | Word, PDF | doc, .docx, .docm, .dot, dotx, .dotm, .docb, .pdf |
    | Spreadsheet | Excel, CSV, TSV | .xls, .xlsx, .xlt, .xlm, .xlsm, xltx, xltm, xlsb, .xlw, .csv, .tsv |
    | Presentation | PowerPoint | .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx |
    | Email | Outlook | .msg |

    Important

    The **file extensions** and **file types** options *can't* be used as conditions in the same rule. If you want to use them as conditions in the same policy, they must be in separate rules.

To use the **File type is** condition, you must have one of the following versions of Windows:

- Windows Endpoints (X64):

    - Windows 10 (21H2, 22H2)
        - [Windows 10 21H2 update details](https://support.microsoft.com/topic/windows-10-update-history-857b8ccb-71e4-49e5-b3f6-7073197d98fb)
        - [Windows 10 22H2 update details](https://support.microsoft.com/topic/windows-10-update-history-8127c2c6-6edf-4fdf-8b9f-0f7be1ef3562)
- Windows Endpoints (ARM64):

    - Windows 11 (21H2, 22H2)
        - [Windows 11 21H2 update details](https://support.microsoft.com/en-us/topic/windows-11-version-21h2-update-history-a19cd327-b57f-44b9-84e0-26ced7109ba9)
        - [Windows 11 22H2 update details](https://support.microsoft.com/en-us/topic/windows-11-version-22h2-update-history-ec4229c3-9c5f-4e75-9d6d-9025ab70fcce)
- **File extension is:** In addition to detecting sensitive information in files with the same extensions as those covered by the **File type is** condition, you can use the **File extension is** condition to detect sensitive information in files with any file extension you need to monitor. To do so, add the necessary file extensions, separated by commas to a rule in your policy. The **File extension is** condition is supported only for those versions of Windows that support the **File type is** condition. **File extension is** doesn't support archive file types.

    Warning

    Including any of the following file extensions in your policy rules might significantly increase the CPU load: .dll, .exe, .mui, .ost, .pf, .pst.
- **Scanning did not complete:** Applies when the scanning of a file started, but stopped before the entire file was scanned. The primary reason for an incomplete scan is that extracted text within the file exceeds the maximum size allowed. (Maximum sizes for extracted text: Uncompressed files: The first 4 MB of extractable text; Compressed files: N=1000 / Extraction Time = 5 minutes.)
- **Document property is:** Detects documents with custom properties matching specified values. For example: `Department = 'Marketing'`, `Project = 'Secret'`. To specify multiple values for a custom property, use double quotes. For example, "Department: Marketing, Sales". Supported file types are Office and PDF:

    | File Type | Format | Monitored file extensions |
    | --- | --- | --- |
    | Word processing | Word, PDF | .doc, .docx, .docm, .dot, dotx, .dotm, .docb, .pdf |
    | Spreadsheet | Excel, CSV, TSV | .xls, .xlsx, .xlt, .xlm, .xlsm, xltx, xltm, xlsb, .xlw, .csv, .tsv |
    | Presentation | PowerPoint | .ppt, .pptx, .pos, .pps, .pptm, .potx, .potm, .ppam, .ppsx |
- **The user accessed a sensitive website from Microsoft Edge:** For more information, see [Help prevent risky user activity by monitoring or restricting access to sensitive service domains](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains).
- **Insider risk level for Adaptive Protection is:** Detects the insider risk level.

See also: [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

##### Operating system requirements for five conditions

- Document could not be scanned
- Document name contains words or phrases
- Document name matches patterns
- Document size equals or is greater than
- Scanning did not complete

To use any of these conditions, your endpoint devices must be running one of the following operating systems:

- **Windows 11 23H2:**[December 4, 2023—KB5032288 (OS Builds 22621.2792 and 22631.2792) Preview](https://support.microsoft.com/en-us/topic/december-4-2023-kb5032288-os-builds-22621-2792-and-22631-2792-preview-538fbe4a-e9de-4312-85cd-d870444341d0)
- **Windows 11 22H2:**[December 4, 2023—KB5032288 (OS Builds 22621.2792 and 22631.2792) Preview - Microsoft Support](https://support.microsoft.com/en-us/topic/december-4-2023-kb5032288-os-builds-22621-2792-and-22631-2792-preview-538fbe4a-e9de-4312-85cd-d870444341d0)
- **Windows 11 21H2:**[December 12, 2023—KB5033369 (OS Build 22000.2652) - Microsoft Support](https://support.microsoft.com/en-us/topic/december-12-2023-kb5033369-os-build-22000-2652-b69fad53-d61b-4ed6-898e-1ae6a17dfd13)
- **Windows 10 22H2:**[November 30, 2023—KB5032278 (OS Build 19045.3758) Preview - Microsoft Support](https://support.microsoft.com/en-us/topic/november-30-2023-kb5032278-os-build-19045-3758-preview-0ae14f06-577e-4eb3-8fcb-c722f3f9dc29)
- **Windows 10 21H2:**[November 30, 2023—KB5032278 (OS Build 19045.3758) Preview - Microsoft Support](https://support.microsoft.com/en-us/topic/november-30-2023-kb5032278-os-build-19045-3758-preview-0ae14f06-577e-4eb3-8fcb-c722f3f9dc29)
- **Windows Server 2022/2019:**[November 14, 2023—KB5032198 (OS Build 20348.2113) - Microsoft Support](https://support.microsoft.com/en-gb/topic/november-14-2023-kb5032198-os-build-20348-2113-e3411fed-057d-402a-86fd-814124e5f26d) (or later)

##### Operating system requirements for Condition 'Document Property is'

- **Windows 11:**[February 29, 2024—KB5034848 (OS Builds 22621.3235 and 22631.3235) Preview - Microsoft Support](https://support.microsoft.com/en-us/topic/february-29-2024-kb5034848-os-builds-22621-3235-and-22631-3235-preview-5b718126-82b1-4e14-bf01-da3500a3fc88) (or later)
- **Windows 10:**[February 29, 2024—KB5034843 (OS Build 19045.4123) Preview - Microsoft Support](https://support.microsoft.com/en-us/topic/february-29-2024-kb5034843-os-build-19045-4123-preview-c576e1b5-9b0d-4411-9be8-57328f41954d) (or later)

Important

For information about the Adobe requirements for using Microsoft Purview Data Loss Prevention (DLP) features with PDF files, see this article from Adobe: [Microsoft Purview Information Protection Support in Acrobat](https://helpx.adobe.com/enterprise/kb/mpip-support-acrobat.html).

##### Conditions Instances supports

- Content contains
- Content is shared from Microsoft 365

##### Conditions On-premises repositories support

- Content contains
- File extension is
- Document property is

##### Conditions Fabric and Power BI support

- Content contains

##### Conditions Microsoft 365 Copilot supports

This feature is in preview.

- Content contains (sensitivity labels)
- Content contains (sensitive information types)
- Email is received from (External users) (preview)

#### Condition groups

Sometimes you need a rule to identify only one thing, such as all content that contains a U.S. Social Security Number, which is defined by a single SIT. However, in many scenarios where the types of items you're trying to identify are more complex and therefore harder to define, more flexibility in defining conditions is required.

For example, to identify content subject to the U.S. Health Insurance Act (HIPAA), you need to look for:

- Content that contains specific types of sensitive information, such as a U.S. Social Security Number or Drug Enforcement Agency (DEA) Number.

    AND
- Content that's more difficult to identify, such as communications about a patient's care or descriptions of medical services provided. Identifying this content requires matching keywords from large keyword lists, such as the International Classification of Diseases (ICD-9-CM or ICD-10-CM).

You can identify this type of data by grouping conditions and using logical operators (AND, OR) between the groups.

For the **U.S. Health Insurance Act (HIPAA)**, conditions are grouped like this:



The first group contains the SITs that identify an individual and the second group contains the SITs that identify medical diagnosis.

Conditions can be grouped and joined by boolean operators (AND, OR, NOT) so that you define a rule by stating what should be included and then defining exclusions in a different group joined to the first by a NOT. To learn more about how Purview DLP implements booleans and nested groups see, [Complex rule design](https://learn.microsoft.com/en-us/purview/dlp-policy-design#complex-rule-design).

#### DLP platform limitations for conditions

| Condition | Workload | Limit | Cost of Evaluation |
| --- | --- | --- | --- |
| Content Contains | EXO/SPO/ODB | 125 SITs per rule | High |
| Content is shared from Microsoft 365 | EXO/SPO/ODB | - | High |
| Sender IP address is | EXO | Individual range length &lt;= 128; Count &lt;= 600 | Low |
| Has sender overridden the policy tip | EXO | - | Low |
| Sender is | EXO | Individual email length &lt;= 256; Count &lt;= 600 | Medium |
| Sender is a member of | EXO | Count &lt;= 600 | High |
| Sender domain is | EXO | Domain name length &lt;= 67; Count &lt;= 600 | Low |
| Sender address contains words | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Low |
| Sender address matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 600 | Low |
| Sender AD attribute contains words | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Medium |
| Sender AD attribute matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 600 | Medium |
| Content of email attachment(s) can't be scanned | EXO | [Supported file types](https://learn.microsoft.com/en-us/en-us/exchange/security-and-compliance/mail-flow-rules/inspect-message-attachments#supported-file-types-for-mail-flow-rule-content-inspection) | Low |
| Incomplete scan of email attachment content | EXO | Extracted content size &gt; 2 MB (2 million characters) | Low |
| Attachment is password-protected | EXO | File types: Office files, .PDF, .ZIP, and 7z | Low |
| Attachment's file extension is | EXO/SPO/ODB | Count &lt;= 600 per rule | High |
| Recipient is a member of | EXO | Count &lt;= 600 | High |
| Recipient domain is | EXO | Domain name length &lt;= 67; Count &lt;= 5000 | Low |
| Recipient is | EXO | Individual email length &lt;= 256; Count &lt;= 600 | Low |
| Recipient address contains words | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Low |
| Recipient address matches patterns | EXO | Count &lt;= 300 | Low |
| Document name contains words or phrases | EXO | Individual word length &lt;= 128; Count &lt;=600 | Low |
| Document Name matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 300 | Low |
| Document property is | EXO/SPO/ODB | - | Low |
| Document size equals or is greater than | EXO | - | Low |
| Subject contains words or phrases | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Low |
| Header contains words or phrases | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Low |
| Subject or body contains words or phrases | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Low |
| Content character set contains words | EXO | Count &lt;= 600 | Low |
| Header matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 300 | Low |
| Subject matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 300 | Low |
| Subject or body matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 300 | Low |
| Message type is | EXO | - | Low |
| Message size over | EXO | - | Low |
| With importance | EXO | - | Low |
| Sender AD attribute contains words | EXO | Each attribute key value pair: has Regex length &lt;= 128 char; Count &lt;= 600 | Medium |
| Sender AD attribute matches patterns | EXO | Each attribute key value pair: has Regex length &lt;= 128 char; Count &lt;= 300 | Medium |
| Document contains words | EXO | Individual word length &lt;= 128; Count &lt;= 600 | Medium |
| Document matches patterns | EXO | Regex length &lt;= 128 char; Count &lt;= 300 | Medium |

### Actions

Any item that makes it through the ***conditions*** filter has any ***actions*** that are defined in the rule applied to it. You have to configure the required options to support the action. For example, if you select Exchange with the **Restrict access or encrypt the content in Microsoft 365 locations** action, you need to choose from these options:

- Block users from accessing shared SharePoint, OneDrive, and Teams content
    - Block everyone. Only the content owner, last modifier, and site admin will continue to have access
    - Block only people from outside your organization. Users inside your organization continue to have access.
- Encrypt email messages (applies only to content in Exchange)

The actions that are available in a rule depend on the locations that have been selected. The available actions for each individual location are listed below.

Important

For SharePoint and OneDrive locations, documents will be proactively blocked right after detection of sensitive information (regardless of whether the document is shared or not) for all guests; internal users continue to have access to the document.

#### Supported actions: Exchange

When DLP policy rules are applied in Exchange, they may be **halting**, **non-halting**, or **neither**. Most of the rules that Exchange supports are non halting. Non halting actions are applied after processing the subsequent rules and policies.

DLP actions are taken on inbound encrypted emails that are in scope of a policy, such as block, *but* to maintain the confidentiality of the encryption, the event won't appear in Activity Explorer or in the Alert and the content of the message won't be accessible to anyone other than the recipient.

However, when a *halting* action is triggered by a DLP policy rule, Purview stops processing any subsequent rules. For instance, when the *Restrict access or encrypt the content in Microsoft 365 locations* action is triggered, no further rules or policies are processed.

If an action is *neither* halting nor non halting, Purview waits for the result of the action to occur before continuing. So, when an outgoing email triggers the *Forward the message for approval to sender's manager* action, Purview waits to get the manager's decision on whether or not the email may be sent. If the manager approves, the action behaves as a non halting action and the subsequent rules are processed. In contrast, if the manager rejects sending the email, *Forward the message for approval to sender's manager* behaves as a halting action and blocks sending the email; no subsequent rules or policies are processed.

The following table lists the actions that Exchange supports, and indicates whether they're halting or non halting.

| Action | Halting / Non halting |
| --- | --- |
| Restrict access or encrypt the content in Microsoft 365 locations (Block Everyone, Block only people outside your organization) | Halting |
| Restrict access or encrypt the content in Microsoft 365 locations (Encrypt Email Messages) | Non - Halting |
| Set headers | Non halting |
| Remove header | Non halting |
| Redirect the message to specific users | Non halting |
| Forward the message for approval to sender's manager | Neither |
| Forward the message for approval to specific approvers | Neither |
| Add recipient to the To box | Non halting |
| Add recipient to the Cc box | Non halting |
| Add recipient to the Bcc box | Non halting |
| Add the sender's manager as recipient | Non halting |
| Remove message encryption and rights protection | Non halting |
| Prepend Email Subject | Non halting |
| Add HTML Disclaimer | Non halting |
| Modify Email Subject | Non halting |
| Deliver the message to the hosted quarantine | Halting |
| Apply branding to encrypted messages | Non halting |

Tip

For the **Apply branding to encrypted messages** action, if you already have Microsoft Purview Message Encryption implemented, the templates automatically show up in the drop-down list. If you want to implement Microsoft Purview Message Encryption, see [Add your organization's brand to your Microsoft Purview Message Encryption encrypted messages](https://learn.microsoft.com/en-us/purview/add-your-organization-brand-to-encrypted-messages) for background on message encryption and how to create and configure your branding templates.

For more information on the actions that Exchange supports, including PowerShell values, see: [Data loss prevention Exchange conditions and actions reference](https://learn.microsoft.com/en-us/purview/dlp-exchange-conditions-and-actions).

#### Supported actions: SharePoint

- Restrict access or encrypt the content in Microsoft 365 locations
    - Block everyone
    - Block only people from outside your organization
    - Block access for specific external domains or users (in public preview)

The **Block access for specific external domains or users** sub-option lets you block external access by domain (for example, `partner.com`) or by user SMTP (for example, `user@example.com`). You can also specify allow lists by using **Domain IS NOT** or **User IS NOT**. Internal users and domains can't be blocked with this sub-option; continue to use **Block everyone** for internal users.

Note

When you use **Block access for specific external domains or users**: if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is across all matching rules — allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.

#### Supported actions: OneDrive

- Restrict access or encrypt the content in Microsoft 365 locations
    - Block everyone
    - Block only people from outside your organization
    - Block access for specific external domains or users (in public preview)

The **Block access for specific external domains or users** sub-option lets you block external access by domain (for example, `partner.com`) or by user SMTP (for example, `user@example.com`). You can also specify allow lists by using **Domain IS NOT** or **User IS NOT**. Internal users and domains can't be blocked with this sub-option; continue to use **Block everyone** for internal users.

Note

When you use **Block access for specific external domains or users**: if a user or domain appears in both allow and block lists, the block takes effect (most restrictive wins). If a file matches both an allow rule and a block rule, evaluation is per rule — allowed users and domains are permitted, blocked users and domains are denied, and users in neither list are blocked by default.

#### Supported actions: Teams Chat and Channel Messages

- Restrict access or encrypt the content in Microsoft 365 locations

#### Supported actions: Devices

The **Devices** location supports these actions:

- Restrict access or encrypt the content in Microsoft 365 locations
    - Block users from receiving email, or accessing shared SharePoint, OneDrive, Teams files, and Power BI items
- Audit or restrict activities when users access sensitive sites in Microsoft Edge browsers on Windows devices
    - Sensitive site restrictions
- Audit or restrict activities on devices
    - Upload to a restricted cloud service domain or access from an unallowed browser
    - Paste to supported browsers
- File activities for all apps
    - Copy to clipboard
    - Copy to removable USB device
    - Copy to a network share
    - Print
    - Copy or move using unallowed Bluetooth app
    - Copy or move using RDP
    - File activities for apps in restricted app groups
    - App access restrictions
        - Access by restricted apps
        - Access by apps not included in restricted apps list or any restricted app groups added to rule
        - *in preview* Restrictions in Windows Recall in Copilot+ PCs
        - Apply restrictions to only unsupported file extensions Start a Power Automate flow

Important

When you select the **Audit or restrict activities on devices** action, the **Apply restrictions to only unsupported file extensions** shows up. **Apply restrictions to only unsupported file extensions** configuration option ***DOES NOT*** support scoping by **Device and device groups** in the policy location setting.

You can tell DLP to **Allow**, **Audit only**, **Block with override**, or **Block** (the actions) these user activities for onboarded Windows devices.

You can tell DLP to **Audit only**, **Block with override**, or **Block** (the actions) these user activities for onboarded macOS devices.

- **Block**: User related activity is blocked, and auditing is enabled. Admins may optionally see alerts.
- **Block with override**: This option acts as a standard block but permits users to bypass it. By clicking the 'Allow' button on the toast notification or the 'Ok' button on the Microsoft Edge notification, users can proceed. Once allowed, Endpoint DLP will automatically resume for actions including 'Copy to a network share', 'Copy to a removable USB device', and 'Print'. For other actions, users will need to repeat the process after clicking 'Allow' to bypass the policy.
- **Audit**: No blocking of activities, but auditing is enabled, and admins may optionally see alerts.
- **Allow**: Activities are allowed without triggering alerts, but auditing is still enabled.
- **Off**: No blocking or auditing of activities.

| Enforcement mode | Block user | Alert generation | Auditing record generation |
| --- | --- | --- | --- |
| Block | Yes | Yes if alert is turned on for the DLP rule | Yes |
| Block with override | Yes | Yes if alert is turned on for the DLP rule | Yes |
| Audit | No | Yes if alert is turned on for the DLP rule | Yes |
| Allow | No | Never triggered | Yes |
| Off | No | No | No |

#### Supported actions: Managed cloud apps

You can tell DLP to **Audit only** or **Block** (the actions) for user activities in managed cloud apps on Windows and macOS devices.

#### Supported actions: Unmanaged cloud apps

You can tell DLP to **Audit only** or **Block** (the actions) for user activities in unmanaged cloud apps on Windows.

#### More information on supported actions

You can find more details here about actions:

- Restrict access or encrypt content in Microsoft 365 locations
- Audit or restrict activities when users access sensitive sites in Microsoft Edge browsers on Windows devices
- Audit or restrict activities on devices
- Service domain and browser activities
- File activities for all apps
- Restricted app activities
- File activities for apps in restricted app groups

##### Restrict access or encrypt content in Microsoft 365 locations

Use this to block users from receiving email, or accessing shared SharePoint, OneDrive, Teams files, and Power BI items. This action can block everyone or block only people who are outside your organization. For SharePoint and OneDrive locations only, you can also block access for specific external domains or user SMTPs (in public preview).

##### Audit or restrict activities when users access sensitive sites in Microsoft Edge browsers on Windows devices

Use this action to control when users attempt to:

| Activity | Description/options |
| --- | --- |
| **Print the site** | Detects when users try to print a protected site from an onboarded device. |
| **Copy data from the site** | Detects when users try to copy data from a protected site from an onboarded device. |
| **Save the site as local files (Save-As)** | Detects when users try to save a protected site as local files from an onboarded device. |

##### Audit or restrict activities on devices

Use this to restrict user activities by Service domain and browser activities, File activities for all apps, Restricted app activities. To use **Audit or restrict activities on devices**, you have to configure options in **DLP settings** and in the policy in which you want to use them. See, [Restricted apps and app groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#restricted-apps-and-app-groups) for more information.

DLP rules with the action **Audit or restrict activities on devices** can have **Block with override** configured. When this rule is applied to a file, any attempt to perform a restricted action on the file is blocked. A notification is displayed with the option to override the restriction. If the user chooses to override, the action is permitted for a period of 1 minute, during which the user can retry the action without restriction. The exception to this behavior is when a sensitive file is dragged and dropped into Microsoft Edge, which will immediately attach the file if the rule is overridden.

##### Service domain and browser activities

When you configure the **Allow/Block cloud service domains** and the **Unallowed browsers** list (see [Browser and domain restrictions to sensitive data](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#browser-and-domain-restrictions-to-sensitive-data)) and a user attempts to upload a protected file to a cloud service domain or access it from an unallowed browser, you can configure the policy action to `Audit only`, `Block with override`, or `Block` the activity.

| Activity | Description/options |
| --- | --- |
| **Upload to a restricted cloud services domain or access from an unallowed app** | Detects when protected files are blocked or allowed to be uploaded to cloud service domains. See, [Browser and domain restrictions to sensitive data](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#browser-and-domain-restrictions-to-sensitive-data) and [Help prevent risky user activity by monitoring or restricting access to sensitive service domains](https://learn.microsoft.com/en-us/purview/endpoint-dlp-create-policy-restrict-access-to-domains). |
| **Paste to supported browsers** | Detects when users paste sensitive information into a text field or web form using Microsoft Edge, Google Chrome (with Microsoft Purview extension), or Mozilla Firefox (with Microsoft Purview extension). Evaluation is independent of the classification of the source file. For more information, see: [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on). |

##### Paste to Browser limitations

Only certain rule conditions work with Paste to Browser events due to the fact that the rules are being evaluated only on the clipboard data. Paste to Browser won't evaluate based on where the text is being copied from.

Rule conditions that work with Paste to Browser:

- Content contains
- Content is not labeled

Additional notes:

- Paste to Browser supports SITs, not Sensitivity Labels.
- Paste to Browser doesn't evaluate on text smaller than 30 characters.
- Advanced Classification isn't supported.
- Contextual Summary doesn't show for Paste to Browser events.
- Paste to Browser takes 2 seconds to evaluate before allowing the paste action.
- IF JIT is configured to block on fallback, it blocks pasting.
- Paste to Browser only classifies the first 4 MB of text from the clipboard

##### File activities for all apps

With the **File activities for all apps** option, you select either **Don't restrict file activities** or **Apply restrictions to specific activities**. When you select **Apply restrictions to specific activities**, the actions that you select here are applied when a user has accessed a DLP protected item.

| Activity | Description/options |
| --- | --- |
| **Copy to clipboard** | Detects when protected files are copied to the clipboard on an onboarded device. For more information, see [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on) and [Copy to clipboard behavior](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#copy-to-clipboard-behavior) |
| **Copy to a removable device** | Detects when protected files are copied or moved from an onboarded device to a removable USB device. For more information, see [Removable USB device groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#removable-usb-device-groups). |
| **Copy to a network share** | Detects when protected files are copied or moved from an onboarded device to any network share. For more information, see [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on) and [Network share coverage and exclusions](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#network-share-coverage-and-exclusions). |
| **Print** | Detects when a protected file is printed from an onboarded device. For more information, see [Printer groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#printer-groups). |
| **Copy or move using unallowed Bluetooth app** | Detects when a protected file is copied or moved from an onboarded Windows device using an unallowed Bluetooth app. For more information, see [Unallowed Bluetooth apps](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#unallowed-bluetooth-apps). This isn't supported for macOS. |
| **Copy or move using RDP** | Detects when users copy or move protected files from an onboarded Windows device to another location using RDP. This isn't supported for macOS. |

##### Restricted app activities

Previously called Unallowed apps, *restricted app activities* are apps that you want to place restrictions on. You define these apps in a list in Endpoint DLP settings. When a user attempts to access a DLP protected file using an app that is on the list, you can either `Audit only`, `Block with override`, or `Block` the activity. DLP actions defined in **Restricted app activities** are overridden if the app is a member of restricted app group. Then the actions defined in the restricted app group are applied.

| Activity | Description/options |
| --- | --- |
| **Access by restricted apps** | Detects when unallowed apps try to access protected files on an onboarded Windows device. For more information, see [Restricted apps and app groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#restricted-apps-and-app-groups). |

##### File activities for apps in restricted app groups

You define your restricted app groups in Endpoint DLP settings and add restricted app groups to your policies. When you add a restricted app group to a policy, you must select one of these options:

- Don't restrict file activity
- Apply restrictions to all activity
- Apply restrictions to specific activity

When you select either of the *Apply restrictions* options, and a user attempts to access a DLP protected file using an app that is in the restricted app group, you can either `Audit only`, `Block with override`, or `Block` by activity. DLP actions that you define here override actions defined in **Restricted app activities** and **File activities for all apps** for the app.

For more information, see [Restricted apps and app groups](https://learn.microsoft.com/en-us/purview/dlp-configure-endpoint-settings#restricted-apps-and-app-groups).

Note

The devices location provides many subactivities (conditions) and actions. To learn more, see [Endpoint activities you can monitor and take action on](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-activities-you-can-monitor-and-take-action-on).

Important

The **Copy to clipboard** condition detects when a user copies information from a *protected file* to the clipboard. Use **Copy to clipboard** to block, block with override, or audit when users copy information from a protected file.

The **Paste to supported browsers** condition detects when a user attempts to paste sensitive text into a text field or web form using Microsoft Edge, Google Chrome with Microsoft Purview extension, or Mozilla Firefox with Microsoft Purview extension *regardless of where that information came from*. Use **Paste to supported browsers** to block, block with override, or audit when users paste sensitive information into a text field or web form.

#### Instances actions

- Restrict access or encrypt the content in Microsoft 365 locations
- Restrict Third Party Apps

#### On-premises repositories actions

- Restrict access or remove on-premises files.
    - Block people from accessing files stored in on-premises repositories
    - Set permissions on the file (permissions inherited from the parent folder)
    - Move file from where it's stored to a quarantine folder

See, [DLP On-premises repository actions](https://learn.microsoft.com/en-us/purview/dlp-on-premises-scanner-learn#dlp-on-premises-repository-actions) for full details.

#### Fabric and Power BI actions

- Notify users with email and policy tips
- Send alerts to Administrator
- Restrict access

Note

Applicable to [supported item types](https://learn.microsoft.com/en-us/en-us/purview/dlp-powerbi-get-started#supported-item-types) only.

#### Microsoft 365 Copilot actions

This feature is in preview.

- Exclude content in the location

#### Managed cloud apps actions

- Restrict browser and network activities

#### Unmanaged cloud apps actions

- Restrict browser and network activities

#### Actions available when you combine locations

If you select Exchange and any other single location for the policy to be applied to, the

- Restrict access or encrypt the content in Microsoft 365 locations and all actions for the non-Exchange location actions are available.

If you select two or more non-Exchange locations for the policy to be applied to, the

- Restrict access or encrypt the content in Microsoft 365 locations and all actions for non-Exchange locations actions are available.

For example, if you select the Exchange and Devices locations, these actions are available:

- Restrict access or encrypt the content in Microsoft 365 locations
- Audit or restrict activities on Windows devices

If you select Devices and Instances, these actions are available:

- Restrict access or encrypt the content in Microsoft 365 locations
- Audit or restrict activities on Windows devices
- Restrict Third Party Apps

Whether an action takes effect or not depends on how you configure the mode of the policy. You can choose to run the policy in simulation mode with or without showing policy tip by selecting the **Run the policy in simulation mode** option. You choose to run the policy as soon as an hour after it's created by selecting the **Turn it on right away** option, or you can choose to just save it and come back to it later by selecting the **Keep it off** option.

#### DLP platform limitations for actions

| Action Name | Workload | Limits |
| --- | --- | --- |
| Restrict access or encrypt content in Microsoft 365 | EXO/SPO/ODB | **Block access for specific external domains or users** sub-option: image files aren't protected; multiple audit records can be generated for certain actions on a blocked file by a blocked user (public preview, SPO/ODB only). |
| Set headers | EXO |  |
| Remove header | EXO |  |
| Redirect the message to specific users | EXO | Total of 100 across all DLP rules. Can't be DL/SG |
| Forward the message for approval to sender's manager | EXO | Manager should be defined in AD |
| Forward the message for approval to specific approvers | EXO | Groups aren't supported |
| Add recipient to the **To** box | EXO | Recipient count &lt;= 10; Can't be DL/SG |
| Add recipient to the **Cc** box | EXO | Recipient count &lt;= 10; Can't be DL/SG |
| Add recipient to the **Bcc** box | EXO | Recipient count &lt;= 10; Can't be DL/SG |
| Add the sender's manager as recipient | EXO | Manager attribute should be defined in AD |
| Apply HTML disclaimer | EXO |  |
| Prepend subject | EXO |  |
| Apply message encryption | EXO |  |
| Remove message encryption | EXO |  |
| (preview) Exclude content in Copilot location | Microsoft 365 Copilot (preview) | Only content in SharePoint and OneDrive for Business can be excluded from being processed by Microsoft 365 Copilot |

### User notifications and policy tips

When a user attempts an activity on a sensitive item in a context that meets the conditions of a rule (for example, content such as an Excel workbook on a OneDrive site that contains personal data (PII) and is shared with a guest), you can let them know about it through user notification emails and in-context policy tip popups. These notifications are useful because they increase awareness and help educate people about your organization's DLP policies.

An Alert email, Incident Report email, and User Notification will only be sent once per document. If a document with a 'Content is Shared' condition is shared twice, there will still be only one notification.



Important

- Notification emails are sent unprotected.
- Email notifications are only supported for the Microsoft 365 services.

#### Email notifications support by selected location

| Selected location | Email notifications supported |
| --- | --- |
| Devices | - Not supported |
| Exchange + Devices | - Supported for Exchange - Not supported for Devices |
| Exchange | - Supported |
| SharePoint + Devices | - Supported for SharePoint - Not supported for Devices |
| SharePoint | - Supported |
| Exchange + SharePoint | - Supported for Exchange - Supported for SharePoint |
| Devices + SharePoint + Exchange | - Not supported for Devices - Supported for SharePoint  Supported for Exchange |
| Teams | - Not supported |
| OneDrive | - Supported for OneDrive for work or school - Not supported for Devices |
| Fabric and Power-BI | - Not supported |
| Instances | - Not supported |
| On-premises repositories | - Not supported |
| Exchange + SharePoint + OneDrive | - Supported for Exchange - Supported for SharePoint - Supported for OneDrive |
| Microsoft 365 Copilot (preview) | - Not supported |
| Managed cloud apps | - Not supported |
| Unmanaged cloud apps | - (Preview) Supported for email notifications. See Email notifications for browser and network (preview). |

#### Email notifications for browser and network (preview)

When a DLP rule is configured for unmanaged cloud apps (browser and network), you can enable email notifications to notify end users via email when their activity is blocked. This is different from the inline pop-up notifications that appear directly in the browser, such as in Microsoft Edge for Business. Email notifications are particularly useful for integrations that don't support pop-up notifications, such as the Android Global Secure Access integration.

You can configure email notifications for:

- The person who performed the blocked activity.
- Additional recipients, such as admins or compliance officers.

##### Email notification batching

Email notifications are batched to prevent a flood of communications:

- The **first** policy match sends an email notification immediately (within seconds of the activity).
- Any additional policy matches within a rolling **10-minute window** are batched into a single email notification that lists all blocked activities.
- After 10 minutes with no further policy matches, the window resets. The next policy match sends an immediate notification and starts a new 10-minute window.

The batched email lists all blocked activities as individual entries, regardless of whether they were triggered by the same or different DLP rules for the same user.

You can also give people the option to override the policy, so that they're not blocked if they have a valid business need or if the policy is detecting a false positive.

#### Policy tips and user notifications configuration options

The user notifications and policy tips configuration options vary depending on the monitoring locations you've selected. If you selected:

- Exchange
- SharePoint
- OneDrive
- Teams Chat and Channel
- Instances

You can enable/disable user notifications for various Microsoft apps, see [Data Loss Prevention policy tips reference](https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference#data-loss-prevention-policy-tips-reference).

You can also enable/disable notifications with a policy tip.

- email notifications to the user who sent, shared, or last modified the content OR
- notify specific people

Furthermore, you can customize the email text, subject, and the policy tip text.



For detailed information on customizing end user notification emails, see [Custom email notifications](https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips#custom-email-notifications).

If you selected Devices only, you get all the same options that are available for Exchange, SharePoint, OneDrive, Teams Chat and Channel, and Instances, plus the option to customize the notification title, content, and add a hyperlink in the form of a *Get Support* button that appears on the Windows 10/11 device.

**Custom policy tip notifications character limits**

Policy tip notifications are subject to the following character limits:

| Variable | Character Limit |
| --- | --- |
| `TITLE` | 120 |
| `CONTENT` | 250 |
| `JUSTIFICATION` | 250 |

Hyperlink has no character limit but is limited to the remaining space available in the entire DLP package. The hyperlink must be a resolvable URL, and it's abstracted behind a selectable control. The more information hyperlink is available in Microsoft 365 Office apps.

You can customize the title and body of text using the following parameters.

| Common name | Parameter | Example |
| --- | --- | --- |
| file name | %%FileName%% | Contoso doc 1 |
| process name | %%ProcessName%% | Word |
| policy name | %%PolicyName%% | Contoso highly confidential |
| action | %%AppliedActions%% | pasting document content from the clipboard to another app |

**%%AppliedActions%%** substitutes these values into the message body:

| action common name | value substituted in for %%AppliedActions%% parameter |
| --- | --- |
| copy to removeable storage | *writing to removable storage* |
| copy to network share | *writing to a network share* |
| print | *printing* |
| paste from clipboard | *pasting from the clipboard* |
| copy via bluetooth | *transferring via Bluetooth* |
| open with an unallowed app | *opening with this app* |
| copy to a remote desktop (RDP) | *transferring to remote desktop* |
| uploading to an unallowed website | *uploading to this site* |
| accessing the item via an unallowed browser | *opening with this browser* |

Using this customized text

*%%AppliedActions%% File name %%FileName%% via %%ProcessName%% isn't allowed by your organization. Select 'Allow' if you want to bypass the policy %%PolicyName%%*

produces this text in the customized notification:

*pasting from the clipboard File Name: Contoso doc 1 via WINWORD.EXE isn't allowed by your organization. Select the 'Allow' button if you want to bypass the policy Contoso highly confidential*

You can localize your custom policy tips by using the [Set-DlpComplianceRule -NotifyPolicyTipCustomTextTranslations cmdlet](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/new-dlpcompliancerule#-notifypolicytipcustomtexttranslations).

Custom Policy Tips show for the most restrictive rule, not necessarily the rule that's performing the restriction.

Note

User notifications and policy tips aren't available for the On-premises location

Only the policy tip from the highest priority, most restrictive rule is shown. For example, a policy tip from a rule that blocks access to content will be shown over a policy tip from a rule that simply sends a notification. This prevents people from seeing a cascade of policy tips.

To learn more about user notification and policy tip configuration and use, including how to customize the notification and tip text, see [Send email notifications and show policy tips for DLP policies](https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips#send-email-notifications-and-show-policy-tips-for-dlp-policies).

#### Policy tip considerations

- Policy tips aren't generated if the sensitivity label is in a compressed file.
- DLP has difficulty generating policy tips for encrypted files.

#### Policy tip references

Details on support for policy tips and notifications for different apps can be found here:

- [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips)
- [Data loss prevention policy tip reference for Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips)
- [Data loss prevention policy tip reference SharePoint in Microsoft 365 and OneDrive. web client](https://learn.microsoft.com/en-us/purview/dlp-spo-odbweb-policy-tips)

#### Block users in Exchange

Note

If you have policy tips enabled when the policy is configured to **Block only users outside your organization** is met, the policy tips notification blocks you from sending a message at all if there are external recipients. Therefore, you have to remove any external recipients before you can send the message to internal recipients.

#### Blocking and notifications in SharePoint in Microsoft 365 and OneDrive

The following table shows the DLP blocking and notification behavior for policies that are scoped to SharePoint in Microsoft 365 and OneDrive. This isn't intended to be an exhaustive list, and there are more settings that aren't in scope for this article.

| Conditions | Restrict access setting | Blocking and notification behavior |
| --- | --- | --- |
| **Content is shared from Microsoft 365**- with people outside my organization | Not configured | User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is shared with a guest or when a guest accesses the file. |
| **Content is shared from Microsoft 365**- only with people inside my organization | Not configured | User notification emails, policy tips, DLP alerts, and incident reports are sent when sensitive information is detected in the document. |
| **Content is shared from Microsoft 365**- only with people inside my organization | - **Restrict access or encrypt the content in Microsoft 365 locations**- **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files**-**Block everyone** | - Access to sensitive files is blocked as soon as they're uploaded. - User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is uploaded |
| **Content is shared from Microsoft 365** - with people outside my organization | - **Restrict access or encrypt the content in Microsoft 365 locations**- **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files**- **Block only people outside your organization** | - Access to a sensitive file is blocked as soon as it's uploaded, regardless of whether the document is shared or not for all guests. Policy Tips will be sent when the sensitive information is detected.- If the sensitive information is added to a file after it's shared and accessed by a user outside the organization, then alerts and incident reports will be sent.- If the document contains sensitive information before it's uploaded, external sharing will be blocked proactively. Because external sharing in this scenario is blocked when the file is uploaded, no alerts or incident reports are sent. Suppression of the alerts and incident reports is designed to prevent a flood of alerts to the user for each blocked file. User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is uploaded or sensitive information is added to the file.- Proactive blocking will show up as event in the Audit Log and Activity Explorer. |
| - **Content is shared from Microsoft 365** - **with people outside my organization** | - **Restrict access or encrypt the content in Microsoft 365 locations**- **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files**- **Block everyone** | - When the first user outside the organization access the document, the event causes the document to be blocked. - It's expected that for a short time, the document is accessible by guests who have the link to the file.- User notification emails, policy tips, DLP alerts, and incident reports are sent when a file is shared with a guest or when a guest accesses that file. |
| **Content is shared from Microsoft 365** - with people outside my organization | - **Restrict access or encrypt the content in Microsoft 365 locations**- **Block users from receiving email or accessing shared SharePoint, OneDrive, and Teams files**- **Block access for specific external domains or users** (in public preview, SPO/ODB only) | - Access is denied when a configured external user or domain attempts to open, preview, or download the file. - An audit record is generated per blocked access attempt (subject to preview limitations). - Events can be reviewed in DLP Alerts, Activity Explorer, and Audit logs. The event contains the blocked user's email. - Internal users and domains can't be blocked with this sub-option; use **Block everyone** to block internal users. |

#### Learn more URL

Users may want to learn why their activity is being blocked. You can configure a site or a page that explains more about your policies. In the rule's user notification settings, select **Provide a compliance URL for the end user to learn more about your organization's policies**, and then enter the URL.

- For Outlook Win32, the *Learn more* link in the policy tip points to the site URL that you provide. This URL has priority over the global compliance URL configured with [Set-PolicyConfig -ComplianceURL](https://learn.microsoft.com/en-us/en-us/powershell/module/exchange/set-policyconfig?view=exchange-ps&amp;preserve-view=true).
- For Microsoft Copilot and Copilot Chat, the **Learn about access restrictions** link in the standard block message points to the URL that you provide. Only the link destination changes; the message text and enforcement action remain unchanged. For more information, see [Customize the link in Copilot policy tips](https://learn.microsoft.com/en-us/purview/dlp-microsoft365-copilot-location-learn-about#customize-the-link-in-copilot-policy-tips).

Important

You must configure the site or page that the link points to from scratch. Microsoft Purview doesn't provide this functionality out of the box.

### User overrides

The intent of **User overrides** is to give users a way to bypass, with justification, DLP policy blocking actions on sensitive items in Exchange, SharePoint, OneDrive, or Teams, so that they can continue their work. User overrides are enabled only when **Notify users in Office 365 services with a policy tip** is enabled, so user overrides go hand-in-hand with Notifications and Policy tips.



Note

User overrides aren't available for the On-premises repositories location.

Typically, user overrides are useful when your organization is first rolling out a policy. The feedback that you get from any override justifications and identifying false positives helps in tuning the policy.

- If the policy tips in the most restrictive rule allow people to override the rule, then overriding this rule also overrides any other rules that the content matched.

#### User override behavior

When a user selects the **Allow** option to override a block action for these activities:

- Print
- Copy to a removable USB device
- Copy to a network share

Within 30 seconds of the popup notification showing, the activity is allowed to continue. If the user doesn't select the **Allow** option within 30 seconds, the activity is blocked.

For all other activities, the user must repeat the activity after selecting the **Allow** option in order for it to complete

#### Business justification X-Header

When a user overrides a block with override action on an email, the override option and the text that they provide are stored in the [Audit log](https://learn.microsoft.com/en-us/purview/audit-solutions-overview) and in the email X-header. To view the business justification overrides, [search the audit log](https://learn.microsoft.com/en-us/purview/audit-search) for `ExceptionInfo` value for the details. Here's an example of the audit log values:

```xml
{
    "FalsePositive"; false,
    "Justification"; My manager approved sharing of this content",
    "Reason"; "Override",
    "Rules": [
         "<message guid>"
    ]
}
```

If you have an automated process that makes use of the business justification values, the process can access that information programmatically in the email X-header data.

Note

The `msip_justification` values are stored in the following order:

`False Positive; Recipient Entitled; Manager Approved; I Acknowledge; JustificationText_[free text]`.

Notice that the values are separated by semicolons. The maximum free text allowed is 500 characters.

### Incident reports

When a rule is matched, you can send an *Alert* email to your compliance officer (or any people you choose) with details of the event and you can view them in the Microsoft Purview Data Loss Prevention **Alerts** dashboard and in the [Microsoft Defender XDR portal](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender). An alert includes information about the item that was matched, the actual content that matched the rule, and the name of the person who last modified the content.

In preview, admin alert emails include details such as:

- The alert severity
- The time the alert occurred
- The activity.
- The sensitive data that were detected.
- The alias of the user whose activity triggered the alert.
- The policy that was matched.
- The alert ID
- The endpoint operation that was attempted if the **Devices** location is in the scope of the policy.
- The app that was being used.
- The device name, if the match occurred on an endpoint device.

DLP feeds incident information to other Microsoft Purview Information Protection services, like [insider risk management](https://learn.microsoft.com/en-us/purview/insider-risk-management). In order to get incident information to insider risk management, you must set the **Incident reports** severity level to **High**.



#### Alert types

Alerts can be sent every time an activity matches a rule, which can be noisy. To help cut down on the noise, they can be aggregated based on number of matches or volume of items over a set period of time. There are two types of alerts that can be configured in DLP policies.

- **Single-event alerts** are typically used in policies that monitor for highly sensitive events that occur in a low volume, like a single email with 10 or more customer credit card numbers being sent outside your organization. In preview [user based alert aggregation (preview)](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started#user-and-rule-based-alert-aggregation-preview) modifies the behavior of single event alerts.
- **Aggregate-event alerts** are typically used in policies that monitor for events that occur in a higher volume over a period of time. For example, an aggregate alert can be triggered when 10 individual emails each with one customer credit card number is sent outside your org over 48 hours.

Note

For rules with Alerts configured on Sharepoint, or OneDrive workloads we only send one alert per file per rule. This is true, even if the same violation has been committed by multiple users.

#### Other alert options

When you select **Use email incident reports to notify you when a policy match occurs** you can choose to include:

- The name of the person who last modified the content.
- The types of sensitive content that matched the rule.
- The rule's severity level.
- The content that matched the rule, including the surrounding text.
- The item containing the content that matched the rule.

For more information on alerts, see:

- [Alerts in DLP policies](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#incident-reports): Describes alerts in the context of a DLP policy.
- [Get started with data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alerts-get-started): Covers the necessary licensing, permissions, and prerequisites for DLP alerts and alert reference details.
- [Create and deploy data loss prevention policies](https://learn.microsoft.com/en-us/purview/dlp-create-deploy-policy): Includes guidance on alert configuration in the context of creating a DLP policy.
- [Learn about investigating data loss prevention alerts](https://learn.microsoft.com/en-us/purview/dlp-alert-investigation-learn): Covers the various methods for investigating of DLP alerts.
- [Investigate data loss incidents with Microsoft Defender XDR](https://learn.microsoft.com/en-us/en-us/defender-xdr/dlp-investigate-alerts-defender): How to investigate DLP alerts in Microsoft Defender portal.

#### Evidence collection for file activities on devices

If you've enabled **Setup evidence collection for file activities on devices** and added Azure storage accounts, you can select **Collect original file as evidence for all selected file activities on Endpoint** and the Azure storage account you want to copy the items to. You must also choose the activities you want to copy items for. For example, if you select **Print** but not **Copy to a network share**, then only items that are printed from monitored devices will be copied to the Azure storage account.

### Additional options

If you have multiple rules in a policy, you can use the **Additional options** to control further rule processing if there's a match to the rule you're editing as well as setting the priority for evaluation of the rule. This is only supported for Exchange and Teams locations
