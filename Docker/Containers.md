---
tags:
  - docker
---
1. A container is a standard unit of software that packages up code and all its dependencies so the application runs quickly and reliably from one computing environment to another.
2. A Docker container image is a lightweight, standalone, executable package of software that includes everything needed to run an application: code, runtime, system tools, system libraries and settings.
3. Container images become containers at runtime and in the case of Docker containers – images become containers when they run on Docker Engine. 
4. Docker containers that run on Docker Engine:
	- **Standard:** Docker created the industry standard for containers, so they could be portable anywhere
	- **Lightweight:** Containers share the machine’s OS system kernel and therefore do not require an OS per application, driving higher server efficiencies and reducing server and licensing costs
	- **Secure:** Applications are safer in containers and Docker provides the strongest default isolation capabilities in the industry


## Comparing Containers and Virtual Machines

| **Aspect**              | **Containers**                                         | **Virtual Machines (VMs)**                  |
| ----------------------- | ------------------------------------------------------ | ------------------------------------------- |
| **Abstraction Layer**   | Application layer                                      | Hardware layer                              |
| **Isolation**           | Isolated processes in user space sharing OS kernel     | Fully isolated with a separate OS           |
| **Size**                | Lightweight (typically tens of MBs)                    | Larger (typically tens of GBs)              |
| **Boot Time**           | Fast to start                                          | Slower to boot                              |
| **Resource Efficiency** | More efficient, shares OS kernel                       | Less efficient, each VM has its own OS      |
| **Usage**               | Ideal for running multiple apps on a single OS         | Ideal for running different OS environments |
| **Overhead**            | Lower overhead (no need for separate OS per container) | Higher overhead (each VM has a full OS)     |
|                         |                                                        |                                             |


# Bare Metal vs VM vs Containers

## Bare Metal

Bare metal is a term used to describe a computer that is running directly on the hardware without any virtualization. This is the most performant way to run an application, but it is also the least flexible. You can only run one application per server, and you cannot easily move the application to another server.

## Virtual Machines

Virtual machines (VMs) are a way to run multiple applications on a single server. Each VM runs on top of a hypervisor, which is a piece of software that emulates the hardware of a computer. The hypervisor allows you to run multiple operating systems on a single server, and it also provides isolation between applications running on different VMs.

## Containers

Containers are a way to run multiple applications on a single server without the overhead of a hypervisor. Each container runs on top of a container engine, which is a piece of software that emulates the operating system of a computer.