# Integrate Microsoft 365 with ServiceNow Virtual Agent

> Source: https://learn.microsoft.com/en-us/microsoft-365/admin/manage/servicenow-virtual-agent-integration  
> Microsoft doc last updated: 04/28/2025


> [!IMPORTANT]
> Microsoft 365 support integration with ServiceNow is retired, and the service will be completely shut down on May 30, 2025. If you installed the integration, take necessary steps to remove it before May 30, 2025.

When you configure the Microsoft 365 support integration app to work with ServiceNow Virtual Agent, you access the self-help created by Microsoft 365 product teams through two different user experiences:

- Microsoft 365 step-by-step and walk-through solutions.

    
    

- Top web search results from Microsoft 365 knowledge base articles.

    

## Before you begin

- Enable Virtual Agent in ServiceNow. For details, see [Activate Virtual Agent](https://docs.servicenow.com/bundle/quebec-now-intelligence/page/administer/virtual-agent/task/activate-virtual-agent.html).

- Install and complete the setup of the Microsoft 365 support integration app from the ServiceNow Store.

- Minimum version of ServiceNow: Rome.

- Role required: ServiceNow admin or virtual_agent_admin.

## Configure Microsoft 365 support integration to work with ServiceNow Virtual Agent

### Standalone fallback topic

Set Microsoft 365 Support as your fallback topic. For details, see [Configure a Virtual Agent chat experience](https://docs.servicenow.com/bundle/quebec-now-intelligence/page/administer/virtual-agent/task/configure-default-chat-experience.html).

### Topic blocks

If you don’t have any topic created, you can use the standalone fallback topic as above or [create your own virtual agent topic](https://docs.servicenow.com/bundle/rome-now-intelligence/page/administer/virtual-agent/task/create-virtual-agent-topic.html).

Follow these steps to add the Microsoft 365 Support topic block:

1. Under **Utilities**, select **Topic Block**, and add it to your flow.

    

1. Under **Topic Block Properties**, choose **Microsoft 365 Support Topic Block**.

    

1. A Microsoft 365 Support Topic Block accesses input text in this order:

    a. Checks for input variable. If the input variable is not empty, fetches the results for the input variable.

    

    b. If the input variable is empty, checks for text entered by the user in the chat window and fetches results for the text.

    

    c. If the user didn't enter text, asks the user to enter text to fetch results.

    

1. Microsoft 365 Support Topic Block provides an output variable, which is the user’s feedback for the results.

    a. Output variable name: m365_success
    b. Possible output variable values: YES/NO
