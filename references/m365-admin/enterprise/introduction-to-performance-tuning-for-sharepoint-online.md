# Introduction to performance tuning for SharePoint

> Source: https://learn.microsoft.com/en-us/microsoft-365/enterprise/introduction-to-performance-tuning-for-sharepoint-online  
> Microsoft doc last updated: 05/17/2024


This article explains what specific aspects you need to consider when designing pages for best performance in SharePoint.
     
## SharePoint performance metrics

The following broad metrics for SharePoint provide real-world data about performance:
  
- The speed at which pages load
    
- The number of round-trips required per page
    
- Issues with the SharePoint service
    
- Other factors that cause performance degradation
    
### Conclusions reached from the data

General benchmarking data tells us:
  
- Most of the pages perform well on SharePoint.
    
- Noncustomized pages load more quickly.
    
- OneDrive, team sites and system pages, such as _layouts, etc., are all quick to load.
    
- The slowest 1% of SharePoint pages take more than 5,000 milliseconds to load.
    
One simple benchmark test you can use would be to measure performance by comparing the load time of your own portal against the load time of the OneDrive home page as it uses few customized features. This step is often the first step Support asks you to complete when troubleshooting network performance issues.
  
## Use a standard user account when checking performance

A site admin, Site Owner, Editor, or Contributor belong to another security groups, have more permissions, and therefore have extra elements that SharePoint loads on a page.
  
This scenario is applicable to SharePoint on-premises and SharePoint in Microsoft 365, but in an on-premises scenario the differences can't be as easily noticed as in SharePoint in Microsoft 365.
  
In order to correctly evaluate how a page performs for users, you should use a standard user account to avoid loading the authoring controls and extra traffic related to security groups.
  
## Connection categories for performance tuning

You can categorize the connections between the server and the user into three main components. Consider these components when designing SharePoint pages for insight into load times.
  
- **Server** The servers that Microsoft hosts in datacenters.
    
- **Network** The Microsoft network, the Internet, and your on-premises network between the datacenter and your users.
    
- **Browser** Where the page is loaded.
    
Within these three connections, there are typically five reasons that cause 95% of slow pages. Each of these reasons is discussed in this article:
  
- Navigation issues
    
- Content roll-up
    
- Large files
    
- Many requests to the server
    
- Web Part processing
    
### Server connection

Many of the issues that affect performance with SharePoint on-premises also apply to SharePoint in Microsoft 365.
  
As you would expect, you have far more control over how servers perform with on-premises SharePoint. With SharePoint in Microsoft 365, things are a little different. The more work you make a server do, the longer it takes to render a page. The biggest culprits in this respect are complex pages with multiple web parts.
  
SharePoint Server on-premises
  

  
SharePoint in Microsoft 365
  

  
With SharePoint on-premises, certain page requests might actually end up calling multiple servers. You could end up with a matrix of requests between servers for an individual request. These interactions are expensive from a page load perspective and make things slow.
  
Examples of these server-to-server interactions are:
  
- Web to SQL Servers
    
- Web to application servers
    
The other thing that can slow down server interactions is cache misses. Unlike on-premises SharePoint, there's a slim chance that you would hit the same server for a page that you visited previously; this makes object caching obsolete.
  
### Network connection

With on-premises SharePoint that doesn't make use of a WAN, you can use a high-speed connection between datacenter and end users. Generally, things are easy to manage from a network perspective.
  
With SharePoint in Microsoft 365, there are a few more factors to consider; for example:
  
- The Microsoft network
    
- The Internet
    
- The Internet Service Provider (ISP)
    
Regardless of which version of SharePoint (and which network) you're using, things that typically cause the network to be busy include:
  
- Large payload
    
- Many files
    
- Large physical distance to the server
    
One feature that you can use in SharePoint in Microsoft 365 is the Microsoft 365 CDN (Content Delivery Network). A CDN is basically a distributed collection of servers deployed across multiple datacenters. With a CDN, content on pages can be hosted on a server close to the client even if the client is far away from the originating SharePoint server. Microsoft will be using this feature more in the future to store local instances of pages that can't be customized, for example the SharePoint admin home page. For more information about CDNs, see [Content delivery networks](https://learn.microsoft.com/en-us/microsoft-365/enterprise/content-delivery-networks).
  
Something that you need to be aware of but have no control over is the connection speed of your ISP. A simple speed test tool tells you the connection speed.
  
### Browser connection

There are a few factors to consider with web browsers from a performance perspective.
  
Visiting complex pages affects performance. Most browsers only have a small default cache size (around 90 MB), while the average web page is typically around 1.6 MB, which doesn't take long to get used up.
  
Bandwidth can also be an issue. For example, if a user is watching videos in another session, it can affect the performance of your SharePoint page. While you can't prevent users from streaming media, you can control the way a page loads for users.
  
Check out the following articles for different SharePoint page customization techniques and other best practices to help you achieve optimal performance.
  
- [Navigation options for SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/navigation-options-for-sharepoint-online)
    
- [Use the Page Diagnostics tool for SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/page-diagnostics-for-spo)
    
- [Image optimization for SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/image-optimization-for-sharepoint-online)
    
- [Delay loading images and JavaScript in SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/delay-loading-images-and-javascript-in-sharepoint-online)
    
- [Minification and bundling in SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/minification-and-bundling-in-sharepoint-online)
    
- [Use the Office 365 Content Delivery Network (CDN) with SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/use-microsoft-365-cdn-with-spo)
    
- [Using Content Search Web Part instead of Content Query Web Part to improve performance in SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/using-content-search-web-part-instead-of-content-query-web-part-to-improve-perfo)
    
- [Capacity planning and load testing SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/capacity-planning-and-load-testing-sharepoint-online)
    
- [Diagnosing performance issues with SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/diagnosing-performance-issues-with-sharepoint-online)
    
- [Using the object cache with SharePoint](https://learn.microsoft.com/en-us/microsoft-365/enterprise/using-the-object-cache-with-sharepoint-online)
    
- [How to: Avoid getting throttled or blocked in SharePoint](https://learn.microsoft.com/en-us/sharepoint/dev/general-development/how-to-avoid-getting-throttled-or-blocked-in-sharepoint-online)
