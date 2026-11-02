# Global Secure Access egress IP ranges

> Source: https://learn.microsoft.com/en-us/entra/global-secure-access/reference-egress-ip-ranges  
> Microsoft doc last updated: 08/28/2025


Outbound Internet traffic that is acquired by Global Secure Access, including traffic to Microsoft services, will egress from Global Secure Access instances. If the target service uses IP restrictions and access controls, you may need to configure the target service to allow IP connections from Global Secure Access subnets:

- `128.94.0.0/19`
- `151.206.0.0/16`

## Related content

- [Global Secure Access points of presence and IP addresses](https://learn.microsoft.com/en-us/entra/global-secure-access/reference-points-of-presence)
