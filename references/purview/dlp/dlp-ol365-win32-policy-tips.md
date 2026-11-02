# Data loss prevention policy tip reference for Outlook for Microsoft 365

> Source: https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips  
> Microsoft doc last updated: 2026-08-04


Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

Mailboxes must be hosted in Exchange Online. For more information, see: [Learn about data loss prevention](https://learn.microsoft.com/en-us/purview/dlp-learn-about-dlp).

Microsoft Purview Data Loss Prevention (DLP) will only process the first 4 MB on message content for policy tip in Outlook for Microsoft 365 and only classify up to 2 MB of attachments. 

Important

Policy Tips won't be displayed in the classic Outlook client for DLP policies scoped to nonmail enabled security groups but rule actions are enforced.

## Licensing

For information on licensing, see

- [Microsoft 365 Enterprise Plans](https://aka.ms/M365EnterprisePlans)
- [Microsoft 365 Service Descriptions](https://learn.microsoft.com/en-us/en-us/office365/servicedescriptions/microsoft-365-service-descriptions/microsoft-365-tenantlevel-services-licensing-guidance/microsoft-365-security-compliance-licensing-guidance)

## Conditions that support policy tips for Outlook perpetual users

| For Outlook perpetual versions and users | These conditions apply |
| --- | --- |
| -E3 users-E5 users | - For email and unencrypted Microsoft 365 files **Content contains built-in/custom sensitive information types**- **Content is shared from Microsoft 365** |

## Conditions that support policy tips for Outlook for Microsoft 365 users

| For Outlook for Microsoft versions and users | These conditions apply |
| --- | --- |
| - All E3 users - All offline E5 users - All E5 users with connected experience disabled - All online E5 users with production version builds lower than 2303 (Build 16.0.16216.10000) - All online E5 users with Semi-Annual Enterprise Channel version builds lower than 2302 (Build 16.0.16130.20478) | - Content contains built-in/custom sensitive information types - Content is shared from Microsoft 365 |
| - All online E5 users with connected experience enabled in WW commercial and GCC/GCC-H/DoD clouds - production version 2303 & Build 16.0 16216.10000 or higher - Semi-Annual Enterprise Channel version 2302 & Build 16.0.16130.20478 or higher - Users without a Microsoft 365 E5 license must be assigned a license that includes the Information Protection for Office 365 - Premium service plan to support DLP Policy Tips in Outlook Classic. | - Content contains built-in/custom sensitive information types (works for email and unencrypted Microsoft 365 and PDF files) - Message (includes email subject) contains built-in/custom sensitive information types - Attachment contains built-in/custom sensitive information types - Content contains sensitivity labels (Works for email and Office & PDF file types)- Content is shared - Sender is - Sender is member of (Only Distribution lists, Azure-based Dynamic Distribution groups, and email-enabled Security groups are supported.) - Sender domain is - Recipient is - Recipient is a member of (Only Distribution lists, Azure-based Dynamic Distribution groups, and email-enabled Security groups are supported.) - Recipient domain is - Subject contains words- Content isn't labeled - Message isn't labeled - Attachment isn't labeled - File extension is |

## Actions that support policy tips

**All Exchange actions support policy tips**

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

## Sensitive information types that support policy tips for Outlook perpetual users

**For Outlook perpetual version E3 and E5 users these built-in sensitive information types and custom sensitive information types support policy tips:**

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

## Sensitive information types that support policy tips for Outlook for Microsoft 365 users

For these Outlook versions and users

- All Microsoft 365 for Enterprise E3 users
- All Microsoft 365 for Enterprise offline E5 users
- All Microsoft 365 for Enterprise E5 users with connected experience disabled
- All Microsoft 365 for Enterprise online E5 users with production version lower than 2303 (Build 16.0.16216.10000)
- All Microsoft 365 for Enterprise online E5 users with Semi-Annual Enterprise Channel version lower than 2302 (Build 16.0.16130.20478)

These OOB sensitive information types support policy tips along with any custom and advanced sensitive information types

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
- [France national ID card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card)
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

For these Outlook versions and users:

- Online E5 users with connected experience enabled.
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2302 (Build 16.0.16130.20478) or higher.

These sensitive information types support policy tips:

- [ABA Routing Number](https://learn.microsoft.com/en-us/purview/sit-defn-aba-routing)
- [All Credential Types](https://learn.microsoft.com/en-us/purview/sit-defn-all-creds)
- [All full names](https://learn.microsoft.com/en-us/purview/sit-defn-all-full-names)
- [All medical terms and conditions](https://learn.microsoft.com/en-us/purview/sit-defn-all-medical-terms-conditions)
- [All Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-all-physical-addresses)
- [Amazon S3 Client Secret Access Key](https://learn.microsoft.com/en-us/purview/sit-defn-amazon-s3-client-secret-access-key)
- [Argentina national identity (DNI) number](https://learn.microsoft.com/en-us/purview/sit-defn-argentina-national-identity-numbers)
- [Argentina Unique Tax Identification Key (CUIT/CUIL)](https://learn.microsoft.com/en-us/purview/sit-defn-argentina-unique-tax-identification-key)
- [ASP.NET machine Key](https://learn.microsoft.com/en-us/purview/sit-defn-asp-net-machine-key)
- [Australia bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-bank-account-number)
- [Australian Business Number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-business-number)
- [Australian Company Number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-business-number)
- [Australia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-drivers-license-number)
- [Australia medical account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number)
- [Australia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-passport-number)
- [Australia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-australia-physical-addresses)
- [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number)
- [Austria Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-drivers-license-number)
- [Austria identity card](https://learn.microsoft.com/en-us/purview/sit-defn-austria-identity-card)
- [Austria passport number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-passport-number)
- [Austria physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-austria-physical-addresses)
- [Austria social security number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-social-security-number)
- [Austria tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-tax-identification-number)
- [Austria Value Added Tax (VAT) Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-value-added-tax)
- [Azure App Service deployment password](https://learn.microsoft.com/en-us/purview/sit-defn-azure-app-service-deployment-password)
- [Azure Batch shared access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-batch-shared-access-key)
- [Azure Bot Framework secret key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-bot-framework-secret-key)
- [Azure Bot service app secret](https://learn.microsoft.com/en-us/purview/sit-defn-azure-bot-service-app-secret)
- [Azure Cognitive Search API key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-cognitive-search-api-key)
- [Azure Cognitive Service key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-cognitive-service-key)
- [Azure Container Registry access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-container-registry-access-key)
- [Azure Cosmos DB account access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-cosmos-db-account-access-key)
- [Azure Databricks personal access token](https://learn.microsoft.com/en-us/purview/sit-defn-azure-databricks-personal-access-token)
- [Azure DevOps app secret](https://learn.microsoft.com/en-us/purview/sit-defn-azure-devops-app-secret)
- [Azure DevOps personal access token](https://learn.microsoft.com/en-us/purview/sit-defn-azure-devops-personal-access-token)
- [Azure DocumentDB auth key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-document-db-auth-key)
- [Azure EventGrid access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-eventgrid-access-key)
- [Azure Function Master / API key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-function-master-api-key)
- [Azure IAAS database connection string and Azure SQL connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iot-connection-string)
- [Azure IoT shared access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iot-shared-access-key)
- [Azure Logic app shared access signature](https://learn.microsoft.com/en-us/purview/sit-defn-azure-logic-app-shared-access-signature)
- [Azure Machine Learning web service API key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-machine-learning-web-service-api-key)
- [Azure Maps subscription key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-maps-subscription-key)
- [Azure publish setting password](https://learn.microsoft.com/en-us/purview/sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string)
- [Azure Redis cache connection string password](https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string-password)
- [Azure SAS](https://learn.microsoft.com/en-us/purview/sit-defn-azure-sas)
- [Azure service bus connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-connection-string)
- [Azure service bus shared access signature](https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-shared-access-signature)
- [Azure Shared Access key / Web Hook token](https://learn.microsoft.com/en-us/purview/sit-defn-azure-shared-access-key-web-hook-token)
- [Azure SignalR access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-signalr-access-key)
- [Azure SQL connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-sql-connection-string)
- [Azure storage account access key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-access-key)
- [Azure storage account key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key-generic)
- [Azure Storage account shared access signature](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-shared-access-signature)
- [Azure Storage account shared access signature for high risk resources](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-shared-access-signature-high-risk-resources)
- [Azure subscription management certificate](https://learn.microsoft.com/en-us/purview/sit-defn-azure-subscription-management-certificate)
- [Belgium driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-drivers-license-number)
- [Belgium national number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-national-number)
- [Belgium passport number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-passport-number)
- [Belgium physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-physical-addresses)
- [Belgium value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-value-added-tax-number)
- [Blood test terms](https://learn.microsoft.com/en-us/purview/sit-defn-blood-test-terms)
- [Brand medication names](https://learn.microsoft.com/en-us/purview/sit-defn-brand-medication-names)
- [Brazil CPF number](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-legal-entity-number)
- [Brazil National ID Card (RG)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-national-identification-card)
- [Brazil physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-physical-addresses)
- [Bulgaria driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-drivers-license-number)
- [Bulgaria passport number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-passport-number)
- [Bulgaria physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-physical-addresses)
- [Bulgaria uniform civil number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-uniform-civil-number)
- [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number)
- [Canada driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-drivers-license-number)
- [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number)
- [Canada passport number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number)
- [Canada physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-canada-physical-addresses)
- [Canada social insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number)
- [Chile identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](https://learn.microsoft.com/en-us/purview/sit-defn-china-resident-identity-card-number)
- [China physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-china-physical-addresses)
- [Client secret / API key](https://learn.microsoft.com/en-us/purview/sit-defn-client-secret-api-key)
- [Credit card number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number)
- [Colombia national ID](https://learn.microsoft.com/en-us/purview/sit-defn-colombia-national-id)
- [Colombia tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-colombia-tax-identification-number)
- [Croatia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-drivers-license-number)
- [Croatia identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-identity-card-number)
- [Croatia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-passport-number)
- [Croatia personal identification (OIB) number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-personal-identification-number)
- [Croatia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-physical-addresses)
- [Cyprus Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-drivers-license-number)
- [Cyprus identity card](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-identity-card)
- [Cyprus passport number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-passport-number)
- [Cyprus physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-physical-addresses)
- [Cyprus tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-tax-identification-number)
- [Czech driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-drivers-license-number)
- [Czech passport number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-passport-number)
- [Czech personal identity number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-personal-identity-number)
- [Czech Republic physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-czech-republic-physical-addresses)
- [Denmark driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-drivers-license-number)
- [Denmark passport number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-passport-number)
- [Denmark personal identification number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-personal-identification-number)
- [Denmark physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-physical-addresses)
- [Diseases](https://learn.microsoft.com/en-us/purview/sit-defn-diseases)
- [Drug Enforcement Agency (DEA) number](https://learn.microsoft.com/en-us/purview/sit-defn-drug-enforcement-agency-number)
- [Ecuador Unique Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-ecuador-unique-identification-number)
- [Estonia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-drivers-license-number)
- [Estonia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-passport-number)
- [Estonia Personal Identification Code](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-personal-identification-code)
- [Estonia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-physical-addresses)
- [EU debit card number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number)
- [EU driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-drivers-license-number)
- [EU national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-national-identification-number)
- [EU passport number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-passport-number)
- [EU Social Security Number (SSN) or Equivalent ID](https://learn.microsoft.com/en-us/purview/sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax Identification Number (TIN)](https://learn.microsoft.com/en-us/purview/sit-defn-eu-tax-identification-number)
- [Finland driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-drivers-license-number)
- [Finland European health insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-european-health-insurance-number)
- [Finland national ID](https://learn.microsoft.com/en-us/purview/sit-defn-finland-national-id)
- [Finland passport number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-passport-number)
- [Finland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-finland-physical-addresses)
- [France driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-france-drivers-license-number)
- [France health insurance number](https://learn.microsoft.com/en-us/purview/sit-defn-france-health-insurance-number)
- [France national id card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card)
- [France passport number](https://learn.microsoft.com/en-us/purview/sit-defn-france-passport-number)
- [France physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-france-physical-addresses)
- [France social security number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number)
- [France Tax Identification Number (numéro SPI.)](https://learn.microsoft.com/en-us/purview/sit-defn-france-tax-identification-number)
- [France value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-france-value-added-tax-number)
- [General password](https://learn.microsoft.com/en-us/purview/sit-defn-general-password)
- [General Symmetric key](https://learn.microsoft.com/en-us/purview/sit-defn-general-symmetric-key)
- [Generic medication names](https://learn.microsoft.com/en-us/purview/sit-defn-generic-medication-names)
- [German Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-drivers-license-number)
- [Germany identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-identity-card-number)
- [German Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-passport-number)
- [Germany physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-germany-physical-addresses)
- [Germany tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-tax-identification-number)
- [Germany value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-value-added-tax-number)
- [GitHub Personal Access Token](https://learn.microsoft.com/en-us/purview/sit-defn-github-personal-access-token)
- [Google API key](https://learn.microsoft.com/en-us/purview/sit-defn-google-api-key)
- [Greenland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-greenland-physical-addresses)
- [Greece driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-drivers-license-number)
- [Greece national ID card](https://learn.microsoft.com/en-us/purview/sit-defn-greece-national-id-card)
- [Greece passport number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-passport-number)
- [Greece physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-greece-physical-addresses)
- [Greece Social Security Number (AMKA)](https://learn.microsoft.com/en-us/purview/sit-defn-greece-social-security-number)
- [Greek Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-tax-identification-number)
- [Hong Kong identity card (HKID) number](https://learn.microsoft.com/en-us/purview/sit-defn-hong-kong-identity-card-number)
- [Http authorization header](https://learn.microsoft.com/en-us/purview/sit-defn-http-authorization-header)
- [Hungary driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-drivers-license-number)
- [Hungary passport number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-passport-number)
- [Hungary personal identification number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-personal-identification-number)
- [Hungary physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-physical-addresses)
- [Hungarian Social Security Number (TAJ)](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-social-security-number)
- [Hungary tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-tax-identification-number)
- [Hungarian Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-value-added-tax-number)
- [Iceland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-iceland-physical-addresses)
- [Impairments Listed In The U.S. Disability Evaluation Under Social Security](https://learn.microsoft.com/en-us/purview/sit-defn-impairments-us-disability-evaluation-under-social-security)
- [India driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-india-drivers-license-number)
- [India GST Number](https://learn.microsoft.com/en-us/purview/sit-defn-india-gst-number)
- [India permanent account number (PAN)](https://learn.microsoft.com/en-us/purview/sit-defn-india-permanent-account-number)
- [India unique identification (Aadhaar) number](https://learn.microsoft.com/en-us/purview/sit-defn-india-unique-identification-number)
- [India Voter Id Card](https://learn.microsoft.com/en-us/purview/sit-defn-india-voter-id-card)
- [Indonesia Drivers License Number](https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-drivers-license-number)
- [Indonesia identity card (KTP) number](https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-identity-card-number)
- [Indonesia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-passport-number)
- [International banking account number (IBAN)](https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number)
- [International classification of diseases (ICD-10-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm)
- [International classification of diseases (ICD-9-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP address](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address)
- [IP Address v4](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address-v4)
- [IP Address v6](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address-v6)
- [Ireland driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-drivers-license-number)
- [Ireland passport number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-passport-number)
- [Ireland personal public service (PPS) number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-personal-public-service-number)
- [Ireland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-physical-addresses)
- [Israel bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-bank-account-number)
- [Israel National ID](https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number)
- [Italy driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-drivers-license-number)
- [Italy fiscal code](https://learn.microsoft.com/en-us/purview/sit-defn-italy-fiscal-code)
- [Italy passport number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-passport-number)
- [Italy physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-italy-physical-addresses)
- [Italy value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-value-added-tax-number)
- [Japan bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-bank-account-number)
- [Japan driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-drivers-license-number)
- [Japanese My Number Corporate](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-corporate)
- [Japanese My Number Personal](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-personal)
- [Japan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-passport-number)
- [Japan physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-japan-physical-addresses)
- [Japanese Residence Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-residence-card-number)
- [Japan resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-resident-registration-number)
- [Japan social insurance number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number)
- [Lab test terms](https://learn.microsoft.com/en-us/purview/sit-defn-lab-test-terms)
- [Latvia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-drivers-license-number)
- [Latvia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-passport-number)
- [Latvia personal code](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-personal-code)
- [Latvia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-physical-addresses)
- [Liechtenstein physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-liechtenstein-physical-addresses)
- [Lifestyles that relate to medical conditions](https://learn.microsoft.com/en-us/purview/sit-defn-lifestyles-relate-to-medical-conditions)
- [Lithuania driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-drivers-license-number)
- [Lithuania passport number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-passport-number)
- [Lithuania personal code](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-personal-code)
- [Lithuania physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-physical-addresses)
- [Luxembourg Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-drivers-license-number)
- [Luxembourg National Identification Number (Natural persons)](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-natural-persons)
- [Luxembourg National Identification Number (Non-natural persons)](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-non-natural-persons)
- [Luxembourg Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-passport-number)
- [Luxembourg Physical Addresses](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-physical-addresses)
- [Malaysia Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-malaysia-identification-card-number)
- [Malaysia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-malaysia-passport-number)
- [Malta driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-drivers-license-number)
- [Malta identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-identity-card-number)
- [Malta passport number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-passport-number)
- [Malta physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-malta-physical-addresses)
- [Malta Tax ID Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-tax-identification-number)
- [Medical Specialities](https://learn.microsoft.com/en-us/purview/sit-defn-medical-specialities)
- [Medicare Beneficiary Identifier (MBI) card](https://learn.microsoft.com/en-us/purview/sit-defn-medicare-beneficiary-identifier-card)
- [Mexico Unique Population Registry Code (CURP)](https://learn.microsoft.com/en-us/purview/sit-defn-mexico-unique-population-registry-code)
- [Microsoft Bing maps key](https://learn.microsoft.com/en-us/purview/sit-defn-microsoft-bing-maps-key)
- [Microsoft Entra client access token](https://learn.microsoft.com/en-us/purview/sit-defn-azure-ad-client-access-token)
- [Microsoft Entra client secret](https://learn.microsoft.com/en-us/purview/sit-defn-azure-ad-client-secret)
- [Microsoft Entra user Credentials](https://learn.microsoft.com/en-us/purview/sit-defn-azure-ad-user-credentials)
- [Netherlands citizen's service (BSN) number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-citizens-service-number)
- [Netherlands driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-drivers-license-number)
- [Netherlands passport number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-passport-number)
- [Netherlands physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-physical-addresses)
- [Netherlands tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-tax-identification-number)
- [Netherlands value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-value-added-tax-number)
- [New Zealand bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-bank-account-number)
- [New Zealand Driver License Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-drivers-license-number)
- [New Zealand inland revenue number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-inland-revenue-number)
- [New Zealand ministry of health number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-ministry-of-health-number)
- [New Zealand physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-physical-addresses)
- [New Zealand social welfare number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-social-welfare-number)
- [Norway Identity Number](https://learn.microsoft.com/en-us/purview/sit-defn-norway-identification-number)
- [Norway physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-norway-physical-addresses)
- [Philippines National ID](https://learn.microsoft.com/en-us/purview/sit-defn-philippines-national-identification-number)
- [Philippines passport number](https://learn.microsoft.com/en-us/purview/sit-defn-philippines-passport-number)
- [Philippines Unified Multi-Purpose ID Number](https://learn.microsoft.com/en-us/purview/sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-drivers-license-number)
- [Poland identity card](https://learn.microsoft.com/en-us/purview/sit-defn-poland-identity-card)
- [Poland national ID (PESEL)](https://learn.microsoft.com/en-us/purview/sit-defn-poland-national-id)
- [Poland Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-passport-number)
- [Poland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-poland-physical-addresses)
- [Poland REGON number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-regon-number)
- [Poland tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-tax-identification-number)
- [Portugal citizen card number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-citizen-card-number)
- [Portugal driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-drivers-license-number)
- [Portugal passport number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-passport-number)
- [Portugal physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-physical-addresses)
- [Portugal tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-tax-identification-number)
- [Qatari ID Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-qatari-id-card-number)
- [Romania driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-drivers-license-number)
- [Romania passport number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-passport-number)
- [Romania personal numeric code (CNP)](https://learn.microsoft.com/en-us/purview/sit-defn-romania-personal-numeric-code)
- [Romania physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-romania-physical-addresses)
- [Russian Passport Number (Domestic)](https://learn.microsoft.com/en-us/purview/sit-defn-russia-passport-number-domestic)
- [Russian Passport Number (International)](https://learn.microsoft.com/en-us/purview/sit-defn-russia-passport-number-international)
- [Russia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-russia-physical-addresses)
- [Russia taxpayer identification number](https://learn.microsoft.com/en-us/purview/sit-defn-russia-taxpayer-identification-number)
- [Saudi Arabia National ID](https://learn.microsoft.com/en-us/purview/sit-defn-saudi-arabia-national-id)
- [Singapore driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-drivers-license-number)
- [Singapore passport number](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-passport-number#singapore-passport-number)
- [Singapore national registration identity card (NRIC) number](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-national-registration-identity-card-number)
- [Singapore physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-physical-addresses)
- [Slack access token](https://learn.microsoft.com/en-us/purview/sit-defn-slack-access-token)
- [Slovakia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-drivers-license-number)
- [Slovakia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-passport-number)
- [Slovakia personal number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-personal-number)
- [Slovakia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-physical-addresses)
- [Slovenia driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-drivers-license-number)
- [Slovenia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-passport-number)
- [Slovenia physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-physical-addresses)
- [Slovenia tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-tax-identification-number)
- [Slovenia Unique Master Citizen Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-unique-master-citizen-number)
- [South Africa identification number](https://learn.microsoft.com/en-us/purview/sit-defn-south-africa-identification-number)
- [South Africa physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-south-africa-physical-addresses)
- [South Korea driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-drivers-license-number)
- [South Korea passport number](https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-passport-number)
- [South Korea resident registration number](https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-resident-registration-number)
- [Spain DNI](https://learn.microsoft.com/en-us/purview/sit-defn-spain-dni)
- [Spain driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-drivers-license-number)
- [Spain passport number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-passport-number)
- [Spain physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-spain-physical-addresses)
- [Spain social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-spain-social-security-number)
- [Spain tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-tax-identification-number)
- [SQL Server connection string](https://learn.microsoft.com/en-us/purview/sit-defn-sql-server-connection-string)
- [Surgical procedures](https://learn.microsoft.com/en-us/purview/sit-defn-surgical-procedures)
- [Sweden driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-drivers-license-number)
- [Sweden national ID](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-national-id)
- [Sweden passport number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-passport-number)
- [Sweden physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-physical-addresses)
- [Sweden tax identification number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-tax-identification-number)
- [SWIFT code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code)
- [Switzerland physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-switzerland-physical-addresses)
- [Swiss Social Security Number AHV](https://learn.microsoft.com/en-us/purview/sit-defn-switzerland-ssn-ahv-number)
- [Taiwan National ID](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-national-identification-number)
- [Taiwan passport number](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-passport-number)
- [Taiwan Resident Certificate (ARC/TARC)](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-resident-certificate-number)
- [Thai population identification code](https://learn.microsoft.com/en-us/purview/sit-defn-thai-population-identification-code)
- [Turkey national identification number](https://learn.microsoft.com/en-us/purview/sit-defn-turkey-national-identification-number)
- [Turkey physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-turkey-physical-addresses)
- [Types of medication](https://learn.microsoft.com/en-us/purview/sit-defn-types-of-medication)
- [U.A.E. identity card number](https://learn.microsoft.com/en-us/purview/sit-defn-uae-identity-card-number)
- [U.A.E. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-uae-passport-number)
- [U.K. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-drivers-license-number)
- [U.K. electoral roll number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-electoral-roll-number)
- [U.K. national health service number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number)
- [U.K. national insurance number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number)
- [U.K. physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-uk-physical-addresses)
- [U.K. Unique Taxpayer Reference Number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-unique-taxpayer-reference-number)
- [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number)
- [U.S. driver's license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number)
- [U.S. physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-us-physical-addresses)
- [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number)
- [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number)
- [Ukraine Passport Number (Domestic)](https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-domestic)
- [Ukraine Passport Number (International)](https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-international)
- [Ukraine physical addresses](https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-physical-addresses)
- [User login credentials](https://learn.microsoft.com/en-us/purview/sit-defn-user-login-credentials)
- [X.509 certificate private key](https://learn.microsoft.com/en-us/purview/sit-defn-x-509-certificate-private-key)

## Exact Data Match sensitive information types that support policy tips Outlook for Microsoft 365

### Applies to

- Online E5 users with connected experience enabled
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2302 (Build 16.0.16130.20478) or higher.

For more information on exact data match based SITs, see [Learn about exact data match based sensitive information types](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits).

## Trainable classifiers support for Outlook for Microsoft 365

Important

Trainable classifiers aren't supported for the following conditions:

- For **new** conditions:
- `Message contains`
- `Attachment contains`
- For the **existing**`Content contains` condition when used in combination with `Evaluate rule per component` condition. (Preview limitation)

### Applies to:

For these Outlook versions and users:

- Online E5 users with connected experience enabled
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2302 (Build 16.0.16130.20478) or higher.

These trainable classifiers are supported:

- [Adult, racy, and gory images](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#adult-racy-and-gory-images)
- [Agreements](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#agreements)
- [Bank statement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#bank-statement)
- [Budget](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#budget)
- [Business plan](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#business-plan)
- [Completion certificates](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#completion-certificates)
- [Construction specifications](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#construction-specifications)
- [Corporate sabotage](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#corporate-sabotage)
- [Customer complaints](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#customer-complaints)
- [Discrimination](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#discrimination)
- [Employee disciplinary action](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#employee-disciplinary-action)
- [Employee insurance](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#employee-insurance)
- [Employment agreement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#employment-agreement)
- [Employee Pension Records](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#employee-pension-records)
- [Employee Stocks and Financial Bond Records](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#employee-stocks-and-financial-bond-records)
- [Enterprise Risk Management](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#enterprise-risk-management)
- [Finance](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#finance)
- [Financial audit](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#financial-audit)
- [Financial statement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#financial-statement)
- [Freight Documents](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#freight-documents)
- [Gifts & entertainment](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#gifts--entertainment)
- [Harassment](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#harassment)
- [Health/Medical forms](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#healthmedical-forms)
- [Healthcare](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#healthcare)
- [Human resources](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions)
- [Invoice](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#invoice)
- [Intellectual property](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#intellectual-property)
- [Information technology](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#information-technology)
- [Legal affairs](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#legal-affairs)
- [Legal Agreements](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#legal-agreements)
- [License agreement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#license-agreement)
- [Loan agreements and offer letters](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#loan-agreements-and-offer-letters)
- [Merger and acquisition files](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#merger-and-acquisition-files)
- [Manufacturing batch records](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#manufacturing-batch-records)
- [Meeting notes](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#meeting-notes)
- [Money laundering](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#money-laundering)
- [Network design files](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#network-design-files)
- [Non-disclosure agreement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#non-disclosure-agreement)
- [Paystub](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#paystub)
- [Personal Financial Information](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#personal-financial-information)
- [Procurement](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#procurement)
- [Project documents](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#project-documents)
- [Profanity](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#profanity)
- [Quotation](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#quotation)
- [Regulatory collusion](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#regulatory-collusion)
- [Resume](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#resume)
- [Safety records](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#safety-records)
- [Sales and revenue](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#sales-and-revenue)
- [Software product development files](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#software-product-development-files)
- [Source code](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#source-code)
- [Standard Operating Procedures and Manuals](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#standard-operating-procedures-and-manuals)
- [Statement of Accounts](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#statement-of-accounts)
- [Statement of work](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#statement-of-work)
- [Stock manipulation](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#stock-manipulation)
- [Tax documents](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#tax-documents)
- [Threat](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#threat)
- [Unauthorized disclosure](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#unauthorized-disclosure)
- [Wire Transfer](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#wire-transfer)
- [Word count requirements](https://learn.microsoft.com/en-us/purview/trainable-classifiers-definitions#word-count-requirements)

For more information on trainable classifiers, see [Learn about trainable classifiers](https://learn.microsoft.com/en-us/purview/trainable-classifiers-learn-about).

## Sensitivity label support for Outlook for Microsoft 365

### Applies to:

- Online E5 users with connected experience enabled
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2302 (Build 16.0.16130.20478) or higher.

For more information on sensitivity labels, see [Learn about sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels).

## Oversharing dialog for Outlook for Microsoft 365

The oversharing dialog is available in DLP for Outlook desktop for E5 users. When enabled in a DLP rule, this feature displays popups for warning, override, or block actions to end users who are sharing labeled or sensitive emails in Outlook desktop.

For information about legacy AIP Add-in, see [admin guide for the AIP client](https://learn.microsoft.com/en-us/en-us/azure/information-protection/rms-client/clientv2-admin-guide-customizations#implement-pop-up-messages-in-outlook-that-warn-justify-or-block-emails-being-sent).

There are multiple types of oversharing dialogs that can be presented to your users.

### Default Oversharing Dialog

#### Applies to:

- Online E5 users with connected experience enabled
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2308 (Build 16.0.16731.20716) or higher.

This dialog uses the exact same text as the policy tip (default or custom) and when applicable, a noncustomizable set of justification options to override the policy.

### Customized Oversharing Dialog

Applies to:

- Online E5 users with connected experience enabled
- Production version 2404 (Build 16.0.17531.20000) or higher.
- Semi-Annual Enterprise Channel version 2408 (Build TBD) or higher.

You can choose to tailor your oversharing dialog with a customized title, body, and dynamic variables like %%MatchedRecipientsList%%, and justification options.

For customized dialog, create a JSON file like this and ensure the following:

- The file is UTF-8 encoded.
- The content is plain text.
- No comments are included.

```json
{
    "LocalizationData": [
        {
            "Language": "en-us",
            "Title": "WARNING: A Sensitivity Label Not for External Use was Detected.",
            "Body": "The following classification(s) have been detected on this email or its attachments. <LineBreak /><LineBreak /><Bold>%%MatchedLabelName%%</Bold><LineBreak /><LineBreak />The email cannot be sent until either the following issues are corrected or a justification is provided. <LineBreak /><LineBreak />Attachment(s) needing attention (if applicable): <LineBreak />%%MatchedAttachmentName%% <LineBreak /><LineBreak />List of external recipients: <LineBreak />%%MatchedRecipientsList%% <LineBreak /><LineBreak />",
            "Options": [
                "The recipients have signed an NDA",
                "Manager has approved this email",
                "Organization required this content to be shared"
            ]
        },
{
            "Language": "es-es",
            "Title": "ADVERTENCIA: Etiqueta de sensibilidad no para uso externo detectada.",
            "Body": "Se ha detectado la(s) siguiente(s) clasificación(es) en este correo electrónico o sus archivos adjuntos. <LineBreak /><LineBreak /><Bold>%%MatchedLabelName%%</Bold><LineBreak /><LineBreak />El correo electrónico no se puede enviar hasta que se corrijan los siguientes problemas o se proporcione una justificación. <LineBreak /><LineBreak />Archivos adjuntos que necesitan atención (si corresponde): <LineBreak />%%MatchedAttachmentName%% <LineBreak /><LineBreak />Lista de destinatarios externos: <LineBreak />%%MatchedRecipientsList%% <LineBreak /><LineBreak />",
            "Options": [
                "Los destinatarios han firmado un NDA",
                "El gerente ha aprobado este correo electrónico",
                "La organización requirió que se compartiera este contenido"
            ]
        }
    ],
    "DefaultLanguage": "en-us"
}
```

The above JSON content can be uploaded in a DLP rule using below options:

##### UX instructions



##### PowerShell

```powershell
$content = Get-Content "path to the JSON file" -Encoding utf8| Out-String
```

```powershell
New-DlpComplianceRule -Name "<Rule_name>" -Policy "<Policy_name>" `-<Any_Condition> <Condition_Value> `-NotifyPolicyTipCustomDialog $content `                                                     -NotifyPolicyTipDisplayOption Dialog                                                                                                                                                                                                               
```

```powershell
  Set-DlpComplianceRule -Identity "<Rule_name>" `-NotifyPolicyTipCustomDialog $content `-NotifyPolicyTipDisplayOption Dialog                                                                                             
```

When you run the cmdlet, validation checks are run on the content. The validation checks include, the JSON character limit, formatting and, mandatory presence of one default language validation. The administrator is notified of any errors so that they can be corrected

##### Features and limitations

The dialog title, body, and override justifications options can be customized using the JSON file. You can apply bold, underline, italic formatting, and line breaks. There can be up to three justifications options plus an option for free-text input.

The text for **Acknowledgement** and **False positive overrides** isn't customizable.

Here's the required structure of the JSON files. You use this to customize the dialog for matched rules. The keys are **all case sensitive**. Formatting and dynamic tokens for matched conditions can only be used in the *Body* key.

| Keys | Mandatory? | Rules/Notes |
| --- | --- | --- |
| {} | Y | Container |
| LocalizationData | Y | Array that contains all the language options. |
| Language | Y | Specify language code, limited to 10 languages. |
| Title | Y | Specify the title for the dialog. Limited to 75 characters. |
| Body | Y | Specify the body for the dialog. Limited to 800 characters. Dynamic tokens for matched conditions can be added in the body. |
| HasFreeTextOption | N | This can be set to true or false. True will display a text box as a last option in the dialog. |
| DefaultLanguage | Y | One of the languages must be defined as DefaultLanguage within the LocalizationData key. |

##### Dynamic tokens and text formatting in custom Oversharing dialog

| Placeholder | Explanation |
| --- | --- |
| %%MatchedRecipientsList%% | Display the matched recipients for a given DLP rule for these conditions: - **Recipient is** - **Recipient domain is** - **Recipient is a member of** - **Content is shared from Microsoft 365** |
| %%MatchedLabelName%% | Display the matched labels for a given DLP rule for this condition: - **Content contains sensitivity label** |
| %%MatchedAttachmentName%% | Display the matched attachments for a given DLP rule for these conditions: - **Content contains sensitive information** - **Content contains sensitivity label** - **Attachment is not labeled** - **File extension is** |
| &lt;Bold&gt;lorem ipsum&lt;/Bold&gt; | Bold format |
| &lt;Italic&gt;lorem ipsum&lt;/Italic&gt; | Italic format |
| &lt;Underline&gt;lorem ipsum&lt;/Underline&gt; | Underline |
| &lt;Linebreak /&gt; or | Introduce a line break |

### Wait on Send dialog support for Oversharing for Outlook for Microsoft 365

After you've configured the Oversharing dialog, you can optionally enable the **Wait on send** dialog feature using the *dlpwaitonsendtimeout Registry key (DWORD value)*. Do this on all devices where you want to ensure sensitive emails are evaluated according to your DLP policies before they're sent. This registry key defines the maximum amount of time to hold an email when the user selects **Send**. It allows DLP policy evaluation to complete for labeled or sensitive content. The **Wait on send** dialog is noncustomizable.



#### Applies to:

- Online E5 users with connected experience enabled
- Production version 2303 (Build 16.0.16216.10000) or higher.
- Semi-Annual Enterprise Channel version 2302 (Build 16.0.16130.20478) or higher.

#### Configure Wait on send

To configure **Wait on send** see, [Steps to configure Wait on send](https://learn.microsoft.com/en-us/purview/dlp-osp-get-started#steps-to-configure-wait-on-send).

Important

Policy tips aren't supported for meeting invitations.
