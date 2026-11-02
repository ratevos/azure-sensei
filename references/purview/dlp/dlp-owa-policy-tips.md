# Data loss prevention policy tip reference for Outlook on the Web

> Source: https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips  
> Microsoft doc last updated: 2026-06-08


Mailboxes must be hosted in Exchange Online. For more information, see: [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp).

Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## DLP policy tips supported

Yes.

## Email notification supported for Outlook on the Web

Yes.

## Conditions that support policy tips in Outlook on the Web

- Content contains (SITs, sensitivity labels)
- Content is shared from M365
- Sender is a member of
- Recipient Domain Is
- Recipient is
- Subject Contains Words or phrases
- Sender is
- Sender domain is
- File extension is
- Subject matches patterns
- Subject or Body contains words or phrases
- Doc or Attachment is password protected
- Document name contains words or phrases
- Sender address contains words
- Document size equals or is greater than
- Subject or Body matches patterns
- Recipient address contains words
- Sender address matches patterns
- Document name matches patterns
- Recipient address matches patterns
- Message importance is
- Document property is
- Content is not labeled

## Actions that support policy tips in Outlook on the Web

- Restrict access or encrypt the content in Microsoft 365 locations
- Set headers
- Remove header
- Redirect the message to specific users
- Forward the message for approval to sender's manager
- Forward the message for approval to specific approvers
- Add recipient to the To box
- Add recipient to the Cc box
- Add recipient to the Bcc box
- Add the sender's manager as recipient
- Removed O365 Message Encryption and rights protection
- Prepend Email Subject
- Add HTML Disclaimer
- Modify Email Subject
- Deliver the message to the hosted quarantine

## Sensitive information types that support policy tips in Outlook on the Web

These preconfigured sensitive information types (SITs) support policy tips in Outlook on the Web.

- [ABA routing number](https://learn.microsoft.com/en-us/purview/sit-defn-aba-routing)
- [Argentina national identity (DNI) number](https://learn.microsoft.com/en-us/purview/sit-defn-argentina-national-identity-numbers)
- [Australia bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-bank-account-number)
- [Australia medical account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number)
- [Australia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-passport-number)
- [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number)
- [Azure DocumentDB auth key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-document-db-auth-key)
- [Azure IAAS database connection string and Azure SQL connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iot-connection-string)
- [Azure publish setting password](https://learn.microsoft.com/en-us/purview/sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string)
- [Azure SAS](https://learn.microsoft.com/en-us/purview/sit-defn-azure-sas)
- [Azure service bus connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-connection-string)
- [Azure storage account key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key-generic)
- [Belgium national number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-national-number)
- [Brazil CPF number](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-legal-entity-number)
- [Brazil national identification card (RG)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-national-identification-card)
- [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number)
- [Canada driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-drivers-license-number)
- [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number)
- [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number)
- [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number)
- [Chile identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](https://learn.microsoft.com/en-us/purview/sit-defn-china-resident-identity-card-number)
- [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number)
- [Croatia identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-identity-card-number)
- [Croatia personal identification (OIB) number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-personal-identification-number)
- [Czech personal identity number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-personal-identity-number)
- [Denmark personal identification number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-personal-identification-number)
- [Drug Enforcement Agency (DEA) number](https://learn.microsoft.com/en-us/purview/sit-defn-drug-enforcement-agency-number)
- [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number)
- [EU driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-drivers-license-number)
- [EU national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-national-identification-number)
- [EU passport number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-passport-number)
- [EU social security number or equivalent identification](https://learn.microsoft.com/en-us/purview/sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-tax-identification-number)
- [Finland national ID](https://learn.microsoft.com/en-us/purview/sit-defn-finland-national-id)
- [Finland passport number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-passport-number)
- [France driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-france-drivers-license-number)
- [France national id card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card)
- [France passport number](https://learn.microsoft.com/en-us/purview/sit-defn-france-passport-number)
- [France social security number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number)
- [Germany driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-drivers-license-number)
- [Germany passport number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-passport-number)
- [Germany identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-identity-card-number)
- [Greece national ID card](https://learn.microsoft.com/en-us/purview/sit-defn-greece-national-id-card)
- [Hong Kong identity card (HKID) number](https://learn.microsoft.com/en-us/purview/sit-defn-hong-kong-identity-card-number)
- [India permanent account number (PAN)](https://learn.microsoft.com/en-us/purview/sit-defn-india-permanent-account-number)
- [India unique identification (Aadhaar) number](https://learn.microsoft.com/en-us/purview/sit-defn-india-unique-identification-number)
- [Indonesia identity card (KTP) number](https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-identity-card-number)
- [International banking account number (IBAN)](https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number)
- [International classification of diseases (ICD-10-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm)
- [International classification of diseases (ICD-9-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP address](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address)
- [IP Address v4](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address-v4#ip-address-v4)
- [IP Address v6](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address-v6#ip-address-v6)
- [Ireland personal public service (PPS) number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-personal-public-service-number)
- [Israel bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-bank-account-number)
- [Israel national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number)
- [Italy driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-drivers-license-number)
- [Japan bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-bank-account-number)
- [Japan driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-drivers-license-number)
- [Japan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-passport-number)
- [Japan resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-resident-registration-number)
- [Japan social insurance number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number)
- [Japan residence card number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-residence-card-number)
- [Malaysia identification card number](https://learn.microsoft.com/en-us/purview/sit-defn-malaysia-identification-card-number)
- [Netherlands citizens service (BSN) number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-citizens-service-number)
- [New Zealand ministry of health number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-ministry-of-health-number)
- [Norway identification number](https://learn.microsoft.com/en-us/purview/sit-defn-norway-identification-number)
- [Philippines unified multi-purpose identification number](https://learn.microsoft.com/en-us/purview/sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland identity card](https://learn.microsoft.com/en-us/purview/sit-defn-poland-identity-card)
- [Poland national ID (PESEL)](https://learn.microsoft.com/en-us/purview/sit-defn-poland-national-id)
- [Poland passport number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-passport-number)
- [Portugal citizen card number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-citizen-card-number)
- [Saudi Arabia National ID](https://learn.microsoft.com/en-us/purview/sit-defn-saudi-arabia-national-id)
- [Singapore national registration identity card (NRIC) number](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-national-registration-identity-card-number)
- [South Africa identification number](https://learn.microsoft.com/en-us/purview/sit-defn-south-africa-identification-number)
- [South Korea resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-resident-registration-number)
- [Spain social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-spain-social-security-number)
- [SQL Server connection string](https://learn.microsoft.com/en-us/purview/sit-defn-sql-server-connection-string)
- [Sweden national ID](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-national-id)
- [Sweden passport number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-passport-number)
- [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code)
- [Taiwan national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-national-identification-number)
- [Taiwan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-passport-number)
- [Taiwan-resident certificate (ARC/TARC) number](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-resident-certificate-number)
- [Thai population identification code](https://learn.microsoft.com/en-us/purview/sit-defn-thai-population-identification-code)
- [Turkey national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-turkey-national-identification-number)
- [U.K. drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-drivers-license-number)
- [U.K. electoral roll number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-electoral-roll-number)
- [U.K. national health service number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number)
- [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number)
- [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number)
- [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number)
- [U.S. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number)
- [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number)

## Exact data match sensitive information types support for policy tips in Outlook on the Web

Yes.

All exact data match sensitive information types are custom created. For more information, see [Learn about exact data match based sensitive information types](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits).

## Custom sensitive information types support for policy tips in Outlook on the Web

Yes.

Custom sensitive information types that use REGEX, functions, keyword lists, and keyword dictionaries support policy tips in Outlook on the Web. For more information, see [Create custom sensitive information types](https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type) and [Create a custom sensitive information type using PowerShell](https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type-in-scc-powershell).

## Sensitivity labels support for policy tips in Outlook on the Web

Yes.

## Retention labels support for policy tips in Outlook on the Web

No.

## Trainable classifiers support for policy tips in Outlook on the Web

No.

## Important information

- When emails are encrypted with Microsoft Purview Message Encryption and the policy used to detect them uses the *detect encryption* condition, policy tips will not appear.
- Administrators can use the DlpViaDcsEnabled parameter to enable exact same features and conditions that New Outlook does, see: [Learn about Organisation configuration](https://learn.microsoft.com/en-us/en-us/powershell/module/exchangepowershell/set-organizationconfig?view=exchange-ps&amp;source=docs).
