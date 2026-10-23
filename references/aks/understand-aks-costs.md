# Understand Azure Kubernetes Service (AKS) usage and costs

> Source: https://learn.microsoft.com/en-us/azure/aks/understand-aks-costs  
> Microsoft doc last updated: 01/30/2025


This article provides resources you can use to better understand your Azure Kubernetes Service (AKS) usage and costs and identify cost optimization opportunities.

## About cost analysis

[Microsoft Cost Management](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/reporting-get-started) is a suite of FinOps tools that help you analyze, monitor, and optimize your cloud costs. It's available for Azure customers with access to a billing account, subscription, resource group, or management group. For more information, see [What is Microsoft Cost Management?](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/overview-cost-management)

[Cost analysis](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/reporting-get-started#cost-analysis) is a feature of Cost Management that helps you understand your costs and usage. It provides insights into how your resources are being used and helps you identify opportunities to reduce costs. For more information, see [Start analyzing costs in Azure](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/quick-acm-cost-analysis).

## Cost analysis resources

### Cost analysis add-on for AKS

The cost analysis add-on for AKS allows you to view comprehensive cost data scoped to Kubernetes constructs, such as clusters and namespaces, and Azure Compute, Network, and Storage resources. Enable it on your AKS cluster by following the steps in [Enable the Azure Kubernetes Service (AKS) cost analysis add-on](https://learn.microsoft.com/en-us/azure/aks/cost-analysis). To learn more about viewing the cost data, see [View Kubernetes costs](https://learn.microsoft.com/en-us/azure/cost-management-billing/costs/view-kubernetes-costs).

### Azure Cost Optimization workbook

The [Azure Cost Optimization workbook](https://learn.microsoft.com/en-us/azure/advisor/advisor-workbook-cost-optimization) provides a comprehensive view of your Azure costs and recommendations for optimizing them. For more information, see [Cost Optimization workbook](https://learn.microsoft.com/en-us/azure/advisor/advisor-workbook-cost-optimization).

### Azure Orphaned Resources workbook

The [Azure Orphaned Resources workbook](https://github.com/dolevshor/azure-orphan-resources) helps you identify and manage unused resources in your Azure environment. For more information, see [Orphaned Resources workbook](https://techcommunity.microsoft.com/blog/fasttrackforazureblog/azure-orphan-resources/3492198).

## Next steps

For more information about managing your AKS costs, see [Best practices for cost optimization in Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/best-practices-cost).
