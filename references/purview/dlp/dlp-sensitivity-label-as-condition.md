# Use sensitivity labels as conditions in DLP policies

> Source: https://learn.microsoft.com/en-us/purview/dlp-sensitivity-label-as-condition  
> Microsoft doc last updated: 2026-08-17


You can use [sensitivity labels](https://learn.microsoft.com/en-us/purview/sensitivity-labels) as a condition in DLP policies for these locations:

- Exchange email messages
- SharePoint
- OneDrive
- Devices
- Instances
- On-premises repositories
- Microsoft 365 Copilot
- Fabric and Power BI workspaces
- Inline web traffic (Unmanaged cloud apps and adaptive app scopes)

Sensitivity labels appear as an option in the **Content contains** condition list.



Tip

Get started with Microsoft Security Copilot to explore new ways to work smarter and faster using the power of AI. Learn more about [Microsoft Security Copilot in Microsoft Purview](https://learn.microsoft.com/en-us/purview/copilot-in-purview-overview).

## Supported items, file types, scenarios, and policy tips

You can use sensitivity labels as conditions on these items and in the following scenarios.

### Supported items

| Service | Item type | Available to policy tip | Enforceable | Notes |
| --- | --- | --- | --- | --- |
| Exchange | email message | Yes | Yes |  |
| Exchange | email attachment | Yes | Yes |  |
| SharePoint | items in SharePoint | Yes | Yes |  |
| OneDrive | items | Yes | Yes |  |
| Teams | Teams and channel messages | Not applicable | Not applicable |  |
| Teams | attachments | Yes | Yes | If SharePoint or OneDrive are included as locations in your DLP policy, you don't need to set Teams as a location. This is because attachments sent in Teams over 1:1 chat or channels are automatically uploaded to OneDrive and SharePoint and will be evaluated by DLP then. |
| Devices | items | Yes | Yes |  |
| MCAS (preview) | items | Yes | Yes |  |
| Inline web traffic | Uploaded and downloaded files | No | Yes | DLP policies don't support custom policy tips for inline web traffic. |

Note

DLP's ability to detect sensitivity labels in SharePoint and OneDrive is limited. For more information, see [Enable sensitivity labels for files in SharePoint and OneDrive](https://learn.microsoft.com/en-us/purview/sensitivity-labels-sharepoint-onedrive-files#limitations).

### Supported file types

| Workload | File types supported |
| --- | --- |
| Exchange emails | .docx, .xlsx, .pptx, .pdf, .pfile |
| SharePoint | .docx, .xlsx, .pptx, .pdf |
| OneDrive | .docx, .xlsx, .pptx, .pdf |
| endpoint devices | .docx, .xlsx, .pptx, .pdf, .pfile |
| Inline web traffic | .docx, .xlsx, .pptx, .pdf, .pfile, .eml - legacy Office file types, .doc, .xls, and .ppt, aren't supported. |

### Supported scenarios

- DLP Admin can see a list of all sensitivity labels in the tenant when they choose to include one or more sensitivity labels as a condition.
- All workloads support using sensitivity labels as a condition, as shown in the support matrix.
- DLP policy tips continue to show across workloads for DLP policies that contain one or more sensitivity labels as a condition.
- Sensitivity labels appear as part of the incident report email if a DLP policy with one or more sensitivity labels as a condition is matched.
- Sensitivity label details show in the DLP rule match audit log for DLP policy matches that contain a sensitivity label as a condition.
- For policies that apply to the Inline web traffic location, content that's encrypted can't be extracted for evaluation by DLP. The only conditions that work are metadata based ones, for example:
- **Content contains** &gt; **Sensitivity label** returns the label name
- **File size** returns the size of the encrypted file
- **File extension is** returns the extension of the encrypted file Conditions that rely on the content being evaluated don't work, for example:
- **Content contains** &gt; **Sensitive information type**
- **Content contains** &gt; **Trainable classifiers**
- **File type is**

### Support policy tips

| Workload | Policy tips supported/not supported |
| --- | --- |
| OWA | supported |
| Outlook for Windows | supported |
| SharePoint | supported |
| OneDrive | supported |
| endpoint devices | not supported |
| Inline web traffic | not supported |

Note

If you use sensitivity labels as a condition and policy tips in a DLP policy for Exchange, and, at the same time, you have mandatory labeling for sensitivity labels configured, when a user selects a label through the Mandatory Labeling prompt, the client does not re-invoke the DLP Policy Tips evaluation gate with the newly applied label. In result, the policy tip is \*\*not \*\* going to show, but the action configured in the DLP policy will be enforced.
