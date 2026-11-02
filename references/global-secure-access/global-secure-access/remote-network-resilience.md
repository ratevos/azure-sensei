# Enhance Remote Network Resilience with Global Secure Access

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/remote-network-resilience  
> Microsoft doc last updated: 09/02/2025

This article provides actionable recommendations to enhance the resilience of remote networks. To ensure optimal deployment and performance of Global Secure Access remote network connectivity, follow these best practices:
 
## Configure redundant tunnels and failovers
Configure multiple Internet Protocol Security (IPsec) tunnels from the customer premises equipment (CPE) to different Global Secure Access edges or POPs. 

### Zone redundancy 
The **Zone redundancy** option creates two IPsec tunnels in different availability zones, but within the same Azure region. 

   

### Geographic redundancy
You can also achieve redundancy by creating a new remote network in a different geographic region. You can use the same CPE configuration to set up IPsec tunnels in the secondary remote network.  

   

Use the CPE's management console to assign weights to these IPsec tunnels and decide how to route traffic through them. 

|Tunnel weighting  |Traffic routing  |
|---------|---------|
|Equal split     | active-active        |
|Primary/secondary     | active-standby        |

### Dynamic route learning
Use Border Gateway Protocol (BGP) for dynamic route learning. If BGP isn't supported on the device, set up static routes with appropriate metrics. 

## Set up CPE according to your desired security posture
Configure CPE based on whether your business prioritizes security or productivity.

### Prioritize security
If you prioritize security, prevent user traffic from going to the destination without first going through Global Secure Access. To do so, statically route traffic over the IPsec tunnel with Global Secure Access without setting up the default route.

### Prioritize productivity
If you prioritize productivity, set up a default route for traffic. This way, if a Global Secure Access VPN gateway or backend service goes down, user traffic continues directly through the default route.

> [!IMPORTANT]
> **Recommendation**: Set up a default route and configure an IP SLA Layer 7 health probe to monitor the endpoint.

To set up a default route:
1. Configure an IP SLA Layer 7 health probe to monitor the endpoint `http://m365.remote-network.edgediagnostic.globalsecureaccess.microsoft.com:6544/ping`. For guidance, see [How to create a remote network with Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-create-remote-networks).
1. Alternatively, set the probe to monitor IP address `198.18.1.101`. Statically send these IP addresses over the Global Secure Access IPsec tunnel from your CPE. We're adding this IP address to the Microsoft 365 BGP route advertisement.

> [!NOTE]
> These endpoints are accessible only through Global Secure Access remote network connectivity.

## Configure monitoring and observability
Monitor traffic logs and remote network health events by exporting them to your Log Analytics workspace. Set up Azure Monitor alert rules to track the health of your workspace. For more information, see [What are remote network health logs?](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-remote-network-health-logs).

## Related content

- [Understand remote network connectivity](https://learn.microsoft.com/en-us/entra/global-secure-access/concept-remote-network-connectivity)
- [How to create a remote network with Global Secure Access](https://learn.microsoft.com/en-us/entra/global-secure-access/how-to-create-remote-networks)
