# Data Loss Prevention policy tips reference

> Source: https://learn.microsoft.com/en-us/purview/dlp-policy-tips-reference  
> Microsoft doc last updated: 2025-09-03


Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## DLP Policy Tips support matrix for Outlook clients highlights

This short table highlights some common DLP support for policy tips across Outlook clients. For complete information, see:

- [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips)
- [Data loss prevention policy tip reference for Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips)
- [Data loss prevention policy tip reference for new Outlook for Windows](https://learn.microsoft.com/en-us/purview/dlp-policy-reference-new-outlook)

| Feature | [Outlook for Microsoft 365 (ver. 2105 build 14026.20000 and semi-annual channel ver. 2102 build 13801.20862)](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | [Outlook On the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips) | [new Outlook for Windows](https://learn.microsoft.com/en-us/purview/dlp-policy-reference-new-outlook) |
| --- | --- | --- | --- |
| Policy tips supported | Yes | Yes | Yes |
| Top 10 conditions - Content is shared from M365- Content contains SITs- Content contains sensitivity label- Subject or Body contains words or phrases- Sender is - Sender is a member of- Sender domain is- Recipient is- Recipient domain is- Recipient is a member of | Yes | Yes | Yes |
| [Default Oversharing Dialog](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips#default-oversharing-dialog) | Yes | No | Yes |
| [Customized Oversharing Dialog](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips#customized-oversharing-dialog) | Yes | No | Yes |
| [Wait on Send dialog support for Oversharing for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips#wait-on-send-dialog-support-for-oversharing-for-outlook-for-microsoft-365) | Yes | No | Yes |
| [Microsoft provided sensitive information types (SIT)](https://learn.microsoft.com/en-us/purview/sit-sensitive-information-type-learn-about) | Yes | Yes | Yes |
| [Custom SITs](https://learn.microsoft.com/en-us/purview/sit-create-a-custom-sensitive-information-type) | Yes | Yes | Yes |
| [Exact data match SITs](https://learn.microsoft.com/en-us/purview/sit-learn-about-exact-data-match-based-sits) | Yes | Yes | Yes |
| [Custom compliance URL to further educate end users](https://learn.microsoft.com/en-us/purview/dlp-policy-reference#policy-tips-and-user-notifications-configuration-options) | Yes | No | No |

## Support Matrix for DLP policy tips across Microsoft apps

| **App and platform** | **DLP policy tip support** | **Sensitive information types supported** | **Conditions and actions supported** | **Comments** |
| --- | --- | --- | --- | --- |
| **Outlook On the Web** |  | Subset. See [Sensitive information types that support policy tips in Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips#sensitive-information-types-that-support-policy-tips-in-outlook-on-the-web) | Subset. See [Conditions that support policy tips in Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips#conditions-that-support-policy-tips-in-outlook-on-the-web) and [Actions that support policy tips in Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips#actions-that-support-policy-tips-in-outlook-on-the-web) | For full details, see [Data loss prevention policy tip reference for Outlook on the Web](https://learn.microsoft.com/en-us/purview/dlp-owa-policy-tips) |
| **Outlook for Microsoft 365 (ver. 2105 build 14026.20000 and semi-annual channel ver. 2102 build 13801.20862)** |  | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) |
| **Outlook Mobile (iOS, Android)** |  | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS](https://learn.microsoft.com/en-us/purview/dlp-outlook-mobile-policy-tip-ref) |
| **Outlook Mac** |  | Varies by version and license. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | Subset. See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips) | For full details, see [Data loss prevention policy tip reference for Outlook for Android, iOS, and macOS](https://learn.microsoft.com/en-us/purview/dlp-outlook-mobile-policy-tip-ref) |
| **SharePoint/OneDrive Web client** |  | All. | All. | See [Data loss prevention policy tip reference for SharePoint and OneDrive web client](https://learn.microsoft.com/en-us/purview/dlp-spo-odbweb-policy-tips) |
| **SharePoint Win32/ OneDrive Win32 client** |  | None | None | DLP policy tips aren't supported on SharePoint or OneDrive desktop client apps |
| **Word, Excel, PowerPoint Web Client** |  | All | All SPO/ODB predicates and actions in DLP | DLP policy tip s are supported if the document is hosted on SharePoint or the OneDrive web app and the DLP policy is already stamped. |
| **Word, Excel, PowerPoint Mobile Client** |  | None | None | DLP policy tips aren't supported in mobile apps for Office. |
| **Teams Web/ Teams Desktop/ Teams Mobile/ Teams Mac** |  | All | All Teams predicates in DLP policy | Policy tips will show when a message is flagged as “This message has been flagged. What can I do?” When clicking the link, the user can review the sensitive info types detected and override or report an issue if allowed by the admin. No policy tips are shown for files. When the recipient tries to access the document, they might get access denied if not allowed. |
| **Win32 Endpoint Devices** |  | Subset | All Endpoint DLP predicates and actions in DLP policy | For more information, see Data Loss Prevention on Endpoint supports policy tips for only some sensitive information types |
| **macOS devices** |  | All | DLP policy tips are supported for all actions that are supported for macOS. | For more information, see [Endpoint DLP Windows 10/11 and macOS support](https://learn.microsoft.com/en-us/purview/endpoint-dlp-learn-about#endpoint-dlp-windows-1011-and-macos-support) |
| **3rd party cloud apps** |  | None | None | DLP policy tips aren't supported on third party cloud apps |
| **On-prem** |  | None | None |  |
| **Word, Excel, PowerPoint Win32 Client** |  | Subset | Subset | See [Data loss prevention policy tip reference for Outlook for Microsoft 365](https://learn.microsoft.com/en-us/purview/dlp-ol365-win32-policy-tips#data-loss-prevention-policy-tip-reference-for-outlook-for-microsoft-365) for the list of sensitive information types supportedPolicy tips for WXP client apps will work for documents stored on SharePoint or OneDrive Sites for all DLP policies that have exactly the below or a subset of conditions or actions in the DLP policy:<br>- Content contains sensitive information types<br>- Access Scope (Content is shared internally/externally)<br>- Notify User (policy tips/user notifications)<br>- Block everyone<br>- Incident reports<br><br> If any other condition or action is present, the DLP policy tip for that policy won't appear in the desktop apps of Word, Excel or PowerPoint.See [Policy tips in Excel, PowerPoint, and Word](https://learn.microsoft.com/en-us/purview/dlp-use-notifications-and-policy-tips#policy-tips-in-excel-powerpoint-and-word) for more details |
| **Fabric and Power BI** |  | - Sensitivity labels - Sensitive information types (excluding exact data match sensitive information types) | Subset | Data loss prevention policies in Power BI and Fabric are generally available.  Policy tips and admin alerts are supported. |

## Data loss prevention on endpoint devices supports policy tips for only some sensitive information types

These sensitive information types (SIT)s can be detected on endpoint devices:

- [ABA routing number](https://learn.microsoft.com/en-us/purview/sit-defn-aba-routing)
- [Argentina national identity (DNI) number](https://learn.microsoft.com/en-us/purview/sit-defn-argentina-national-identity-numbers)
- [Australia bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-bank-account-number)
- [Australia medical account number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-medical-account-number)
- [Australia passport number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-passport-number)
- [Australia tax file number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-tax-file-number)
- [Australia business number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-business-number)
- [Australia Company Number](https://learn.microsoft.com/en-us/purview/sit-defn-australia-company-number)
- [Austria Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-drivers-license-number)
- [Austria Identity Card](https://learn.microsoft.com/en-us/purview/sit-defn-austria-identity-card)
- [Austria Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-passport-number)
- [Austria Social Security Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-social-security-number)
- [Austria Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-austria-tax-identification-number)
- [Austria value added tax](https://learn.microsoft.com/en-us/purview/sit-defn-austria-value-added-tax)
- [Azure DocumentDB auth key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-document-db-auth-key)
- [Azure IAAS database connection string and Azure SQL connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iaas-database-connection-string-azure-sql-connection-string)
- [Azure IoT connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-iot-connection-string)
- [Azure publish setting password](https://learn.microsoft.com/en-us/purview/sit-defn-azure-publish-setting-password)
- [Azure Redis cache connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-redis-cache-connection-string)
- [Azure SAS](https://learn.microsoft.com/en-us/purview/sit-defn-azure-sas)
- [Azure service bus connection string](https://learn.microsoft.com/en-us/purview/sit-defn-azure-service-bus-connection-string)
- [Azure storage account key](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key)
- [Azure Storage account key (generic)](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-key-generic)
- [Azure Storage account Shared Access Signature](https://learn.microsoft.com/en-us/purview/sit-defn-azure-storage-account-shared-access-signature)
- [Belgium drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-drivers-license-number)
- [Belgium National Number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-national-number)
- [Belgium passport number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-passport-number)
- [Belgium value added tax number](https://learn.microsoft.com/en-us/purview/sit-defn-belgium-value-added-tax-number)
- [Brazil CPF number](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-cpf-number)
- [Brazil legal entity number (CNPJ)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-legal-entity-number)
- [Brazil national identification card (RG)](https://learn.microsoft.com/en-us/purview/sit-defn-brazil-national-identification-card)
- [Bulgaria drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-drivers-license-number)
- [Bulgaria passport number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-passport-number)
- [Bulgaria Uniform Civil Number](https://learn.microsoft.com/en-us/purview/sit-defn-bulgaria-uniform-civil-number)
- [Canada bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-bank-account-number)
- [Canada drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-drivers-license-number)
- [Canada health service number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-health-service-number)
- [Canada Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-passport-number)
- [Canada personal health identification number (PHIN)](https://learn.microsoft.com/en-us/purview/sit-defn-canada-personal-health-identification-number)
- [Canada Social Insurance Number](https://learn.microsoft.com/en-us/purview/sit-defn-canada-social-insurance-number)
- [Chile Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-chile-identity-card-number)
- [China resident identity card (PRC) number](https://learn.microsoft.com/en-us/purview/sit-defn-china-resident-identity-card-number)
- [Credit Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-credit-card-number)
- [Croatia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-drivers-license-number)
- [Croatia Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-identity-card-number)
- [Croatia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-passport-number)
- [Croatia Personal Identification (OIB) Number](https://learn.microsoft.com/en-us/purview/sit-defn-croatia-personal-identification-number)
- [General Symmetric Key](https://learn.microsoft.com/en-us/purview/sit-defn-general-symmetric-key)
- [Cyprus Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-drivers-license-number)
- [Cyprus Identity Card](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-identity-card)
- [Cyprus Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-passport-number)
- [Cyprus Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-cyprus-tax-identification-number)
- [Czech drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-drivers-license-number)
- [Czech Personal Identity Number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-personal-identity-number)
- [Czech passport number](https://learn.microsoft.com/en-us/purview/sit-defn-czech-passport-number)
- [Denmark Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-drivers-license-number)
- [Denmark Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-passport-number)
- [Denmark Personal Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-denmark-personal-identification-number)
- [Drug Enforcement Agency (DEA) number](https://learn.microsoft.com/en-us/purview/sit-defn-drug-enforcement-agency-number)
- [Estonia drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-drivers-license-number#estonia-drivers-license-number)
- [Estonia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-passport-number)
- [Estonia Personal Identification Code](https://learn.microsoft.com/en-us/purview/sit-defn-estonia-personal-identification-code)
- [EU Debit Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-debit-card-number)
- [EU Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-drivers-license-number)
- [EU National Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-national-identification-number)
- [EU Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-eu-passport-number)
- [EU Social Security Number (SSN) or Equivalent ID](https://learn.microsoft.com/en-us/purview/sit-defn-eu-social-security-number-equivalent-identification)
- [EU Tax Identification Number (TIN)](https://learn.microsoft.com/en-us/purview/sit-defn-eu-tax-identification-number)
- [Finland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-drivers-license-number)
- [Finland European Health Insurance Number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-european-health-insurance-number)
- [Finland National ID](https://learn.microsoft.com/en-us/purview/sit-defn-finland-national-id)
- [Finland Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-finland-passport-number)
- [France Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-drivers-license-number)
- [France Health Insurance Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-health-insurance-number)
- [France National ID Card (CNI)](https://learn.microsoft.com/en-us/purview/sit-defn-france-national-id-card)
- [France Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-passport-number)
- [France Social Security Number (INSEE)](https://learn.microsoft.com/en-us/purview/sit-defn-france-social-security-number)
- [France Tax Identification Number (numéro SPI.)](https://learn.microsoft.com/en-us/purview/sit-defn-france-tax-identification-number)
- [France Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-france-value-added-tax-number)
- [German Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-drivers-license-number)
- [German Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-passport-number)
- [German Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-identity-card-number)
- [German Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-tax-identification-number)
- [German Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-germany-value-added-tax-number)
- [Greece Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-drivers-license-number)
- [Greece National ID Card](https://learn.microsoft.com/en-us/purview/sit-defn-greece-national-id-card)
- [Greece Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-passport-number)
- [Greece Social Security Number (AMKA)](https://learn.microsoft.com/en-us/purview/sit-defn-greece-social-security-number)
- [Greek Tax identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-greece-tax-identification-number)
- [Hong Kong Identity Card (HKID) Number](https://learn.microsoft.com/en-us/purview/sit-defn-hong-kong-identity-card-number)
- [Hungary Social Security Number (TAJ)](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-social-security-number)
- [Hungary Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-value-added-tax-number)
- [Hungary Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-drivers-license-number)
- [Hungary Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-passport-number)
- [Hungary Personal Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-personal-identification-number)
- [Hungary Tax identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-hungary-tax-identification-number)
- [India Permanent Account Number (PAN)](https://learn.microsoft.com/en-us/purview/sit-defn-india-permanent-account-number)
- [India Unique Identification (Aadhaar) Number](https://learn.microsoft.com/en-us/purview/sit-defn-india-unique-identification-number)
- [Indonesia Identity Card (KTP) Number](https://learn.microsoft.com/en-us/purview/sit-defn-indonesia-identity-card-number)
- [International Banking Account Number (IBAN)](https://learn.microsoft.com/en-us/purview/sit-defn-international-banking-account-number)
- [International Classification of Diseases (ICD-10-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-10-cm)
- [International Classification of Diseases (ICD-9-CM)](https://learn.microsoft.com/en-us/purview/sit-defn-international-classification-of-diseases-icd-9-cm)
- [IP Address](https://learn.microsoft.com/en-us/purview/sit-defn-ip-address)
- [Ireland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-drivers-license-number)
- [Ireland Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-passport-number)
- [Ireland Personal Public Service (PPS) Number](https://learn.microsoft.com/en-us/purview/sit-defn-ireland-personal-public-service-number)
- [Israel Bank Account Number](https://learn.microsoft.com/en-us/purview/sit-defn-israel-bank-account-number)
- [Israel National ID](https://learn.microsoft.com/en-us/purview/sit-defn-israel-national-identification-number)
- [Italy Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-drivers-license-number)
- [Italy Fiscal Code](https://learn.microsoft.com/en-us/purview/sit-defn-italy-fiscal-code)
- [Italy Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-passport-number)
- [Italy Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-italy-value-added-tax-number)
- [Japan Bank Account Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-bank-account-number)
- [Japan Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-drivers-license-number)
- [Japan Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-passport-number)
- [Japan Resident Registration Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-resident-registration-number)
- [Japan Social Insurance Number (SIN)](https://learn.microsoft.com/en-us/purview/sit-defn-japan-social-insurance-number)
- [Japan My Number Corporate](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-corporate)
- [Japan My Number Personal](https://learn.microsoft.com/en-us/purview/sit-defn-japan-my-number-personal)
- [Japan Residence Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-japan-residence-card-number)
- [Latvia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-drivers-license-number)
- [Latvia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-passport-number)
- [Latvia Personal Code](https://learn.microsoft.com/en-us/purview/sit-defn-latvia-personal-code)
- [Lithuania Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-drivers-license-number)
- [Lithuania Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-passport-number)
- [Lithuania Personal Code](https://learn.microsoft.com/en-us/purview/sit-defn-lithuania-personal-code)
- [Luxemburg drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-drivers-license-number)
- [Luxemburg national identification number (natural persons)](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-natural-persons)
- [Luxemburg national identification number (non-natural persons)](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-national-identification-number-non-natural-persons)
- [Luxemburg passport number](https://learn.microsoft.com/en-us/purview/sit-defn-luxemburg-passport-number)
- [Malaysia Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-malaysia-identification-card-number)
- [Malta Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-drivers-license-number)
- [Malta Identity Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-identity-card-number)
- [Malta Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-passport-number)
- [Malta Tax ID Number](https://learn.microsoft.com/en-us/purview/sit-defn-malta-tax-identification-number)
- [Netherlands Citizen's Service (BSN) Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-citizens-service-number)
- [Netherlands Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-drivers-license-number)
- [Netherlands Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-passport-number)
- [Netherlands Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-tax-identification-number)
- [Netherlands Value Added Tax Number](https://learn.microsoft.com/en-us/purview/sit-defn-netherlands-value-added-tax-number)
- [New Zealand bank account Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-bank-account-number)
- [New Zealand Driver License Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-drivers-license-number)
- [New Zealand Inland Revenue Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-inland-revenue-number)
- [New Zealand Ministry of Health Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-ministry-of-health-number)
- [New Zealand Social Welfare Number](https://learn.microsoft.com/en-us/purview/sit-defn-new-zealand-social-welfare-number)
- [Norway Identity Number](https://learn.microsoft.com/en-us/purview/sit-defn-norway-identification-number)
- [Philippines Unified Multi-Purpose ID Number](https://learn.microsoft.com/en-us/purview/sit-defn-philippines-unified-multi-purpose-identification-number)
- [Poland Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-drivers-license-number)
- [Poland Identity Card](https://learn.microsoft.com/en-us/purview/sit-defn-poland-identity-card)
- [Poland National ID (PESEL)](https://learn.microsoft.com/en-us/purview/sit-defn-poland-national-id)
- [Poland Passport](https://learn.microsoft.com/en-us/purview/sit-defn-poland-passport-number)
- [Poland Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-tax-identification-number)
- [Polish REGON Number](https://learn.microsoft.com/en-us/purview/sit-defn-poland-regon-number)
- [Portugal Citizen Card Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-citizen-card-number)
- [Portugal Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-drivers-license-number)
- [Portugal Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-passport-number)
- [Portugal Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-portugal-tax-identification-number)
- [Romania Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-drivers-license-number)
- [Romania Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-romania-passport-number)
- [Romania Personal Numerical Code (CNP)](https://learn.microsoft.com/en-us/purview/sit-defn-romania-personal-numeric-code)
- [Russian Passport Number (Domestic)](https://learn.microsoft.com/en-us/purview/sit-defn-russia-passport-number-domestic)
- [Russian Passport Number (International)](https://learn.microsoft.com/en-us/purview/sit-defn-russia-passport-number-international)
- [Saudi Arabia National ID](https://learn.microsoft.com/en-us/purview/sit-defn-saudi-arabia-national-id)
- [Singapore national registration identity card (NRIC) number](https://learn.microsoft.com/en-us/purview/sit-defn-singapore-national-registration-identity-card-number)
- [Slovakia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-drivers-license-number)
- [Slovakia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-passport-number)
- [Slovakia Personal Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovakia-personal-number)
- [Slovenia Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-drivers-license-number)
- [Slovenia Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-passport-number)
- [Slovenia Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-tax-identification-number)
- [Slovenia Unique Master Citizen Number](https://learn.microsoft.com/en-us/purview/sit-defn-slovenia-unique-master-citizen-number)
- [South Africa Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-south-africa-identification-number)
- [South Korea Resident Registration Number](https://learn.microsoft.com/en-us/purview/sit-defn-south-korea-resident-registration-number)
- [Spain DNI](https://learn.microsoft.com/en-us/purview/sit-defn-spain-dni)
- [Spain Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-drivers-license-number)
- [Spain Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-passport-number)
- [Spain Social Security Number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-spain-social-security-number)
- [Spain Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-spain-tax-identification-number)
- [SQL Server Connection String](https://learn.microsoft.com/en-us/purview/sit-defn-sql-server-connection-string)
- [Sweden Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-drivers-license-number)
- [Sweden National ID](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-national-id)
- [Sweden Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-passport-number)
- [Sweden Tax Identification Number](https://learn.microsoft.com/en-us/purview/sit-defn-sweden-tax-identification-number)
- [SWIFT Code](https://learn.microsoft.com/en-us/purview/sit-defn-swift-code)
- [Swiss Social Security Number AHV](https://learn.microsoft.com/en-us/purview/sit-defn-switzerland-ssn-ahv-number)
- [Taiwan National ID](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-national-identification-number)
- [Taiwan Passport Number](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-passport-number)
- [Taiwan Resident Certificate (ARC/TARC)](https://learn.microsoft.com/en-us/purview/sit-defn-taiwan-resident-certificate-number)
- [Thai Population Identification Code](https://learn.microsoft.com/en-us/purview/sit-defn-thai-population-identification-code)
- [Turkish National Identification number](https://learn.microsoft.com/en-us/purview/sit-defn-turkey-national-identification-number)
- [U.K. Driver's License Number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-drivers-license-number)
- [U.K. Electoral Roll Number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-electoral-roll-number)
- [U.K. National Health Service Number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-health-service-number)
- [U.K. National Insurance Number (NINO)](https://learn.microsoft.com/en-us/purview/sit-defn-uk-national-insurance-number)
- [U.K. Unique Taxpayer Reference Number](https://learn.microsoft.com/en-us/purview/sit-defn-uk-unique-taxpayer-reference-number)
- [U.S./U.K. passport number](https://learn.microsoft.com/en-us/purview/sit-defn-us-uk-passport-number)
- [U.S. bank account number](https://learn.microsoft.com/en-us/purview/sit-defn-us-bank-account-number)
- [U.S. drivers license number](https://learn.microsoft.com/en-us/purview/sit-defn-us-drivers-license-number)
- [U.S. individual taxpayer identification number (ITIN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-individual-taxpayer-identification-number)
- [U.S. social security number (SSN)](https://learn.microsoft.com/en-us/purview/sit-defn-us-social-security-number)
- [Ukraine passport domestic](https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-domestic)
- [Ukraine passport international](https://learn.microsoft.com/en-us/purview/sit-defn-ukraine-passport-international)

Custom sensitive information types will also be detected in addition to the above out-of-the-box sensitive information types.
