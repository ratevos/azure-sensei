# Deploy Apache Airflow on AKS with Helm

> Source: https://learn.microsoft.com/en-us/azure/aks/airflow-overview  
> Microsoft doc last updated: 07/14/2025


In this guide, you deploy Apache Airflow on Azure Kubernetes Service (AKS) using Helm. You learn how to set up an AKS cluster, install Helm, deploy Airflow using the Helm chart, and explore the Airflow UI. This article provides a high-level overview of the architecture and components involved in deploying production-ready Airflow on AKS.

> [!IMPORTANT]
>
> Open-source software is mentioned throughout AKS documentation and samples. Software that you deploy is excluded from AKS service-level agreements, limited warranty, and Azure support. As you use open-source technology alongside AKS, consult the support options available from the respective communities and project maintainers to develop a plan.
>
> Microsoft takes responsibility for building the open-source packages that we deploy on AKS. That responsibility includes having complete ownership of the build, scan, sign, validate, and hotfix process, along with control over the binaries in container images. For more information, see [Vulnerability management for AKS](https://learn.microsoft.com/en-us/azure/aks/concepts-vulnerability-management#aks-container-images) and [AKS support coverage](https://learn.microsoft.com/en-us/azure/aks/support-policies#aks-support-coverage).

## What is Apache Airflow?

[Apache Airflow](https://airflow.apache.org/) is an open-source platform built for developing, scheduling, and monitoring batch-oriented workflows. With its flexible Python framework, Airflow allows you to design workflows that integrate seamlessly with nearly any technology. In Airflow, you must define Python workflows, represented by Directed Acyclic Graph (DAG). You can deploy Airflow anywhere, and after deploying, you can access Airflow UI and set up workflows.

## Airflow architecture

At a high level, Airflow includes:

* A metadata database that tracks the state of DAGs, task instances, XComs, and more.
* A web server providing the Airflow UI for monitoring and management.
* A scheduler responsible for triggering DAGs and task instances.
* Executors that handle the execution of task instances.
* Workers that perform the tasks.
* Other components like the Command Line Interface (CLI).

## Airflow distributed architecture for production

Airflow’s modular, distributed architecture offers several key advantages for production workloads:

* **Separation of concerns**: Each component has a distinct role, keeping the system simple and maintainable. The scheduler manages DAGs and task scheduling, while workers execute tasks, ensuring that each part stays focused on its specific function.
* **Scalability**: As workloads grow, the architecture allows for easy scaling. You can run multiple schedulers or workers concurrently and leverage a hosted database for automatic scaling to accommodate increased demand.
* **Reliability**: Because components are decoupled, the failure of a single scheduler or worker doesn’t lead to a system-wide outage. The centralized metadata database ensures consistency and continuity across the entire system.
* **Extensibility**: The architecture is flexible, allowing components like the executor or queueing service to be swapped out and customized as needed.

This design provides a robust foundation for scaling, reliability, and flexibility in managing complex data pipelines.

### Airflow executors

A very important design decision when making Airflow production-ready is choosing the correct executor. When a task is ready to run, the executor is responsible for managing its execution. Executors interact with a pool of workers that carry out the tasks. The most commonly used executors are:

* **LocalExecutor**: Runs task instances in parallel on the host system. This executor is ideal for testing, but offers limited scalability for larger workloads.
* **CeleryExecutor**: Distributes tasks across multiple machines using a Celery pool, providing horizontal scalability by running workers on different nodes.
* **KubernetesExecutor**: Tailored for Airflow deployments in Kubernetes, this executor dynamically launches worker Pods within the Kubernetes cluster. It offers excellent scalability and ensures strong resource isolation.

As we transition Airflow to production, scaling workers becomes essential, making KubernetesExecutor the best fit for our needs. For local testing, however, LocalExecutor is the simplest option.

## Next step

> [Create the infrastructure for running Apache Airflow on Azure Kubernetes Service (AKS)](https://learn.microsoft.com/en-us/azure/aks/airflow-create-infrastructure)

## Contributors

*Microsoft maintains this article. The following contributors originally wrote it:*

* Don High | Principal Customer Engineer
* Satya Chandragiri | Senior Digital Cloud Solution Architect
* Erin Schaffer | Content Developer 2
