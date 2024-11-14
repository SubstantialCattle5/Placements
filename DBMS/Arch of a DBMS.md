---
tags:
  - intro_db
---
1. The **architecture of a Database Management System (DBMS)** refers to its structure and the way it is designed to manage, store, and retrieve data efficiently. 
2. DBMS architectures can vary based on how they interact with users, how data is processed, and the environment in which they are deployed. 
3. In general, a DBMS follows a multi-layered architecture, consisting of different components and layers that work together to manage data effectively.

### **Types of DBMS Architecture**

DBMS architectures can be classified into the following types:

1. **1-Tier Architecture** ([[#Monolithic]])
2. **2-Tier Architecture** ([[#Client-Server]])
3. **3-Tier Architecture** ([[#Client-Application-Database]])


## Monolithic

In this architecture, the **database** and the **application** both reside on the same system. The user interacts directly with the database through the DBMS. This type of architecture is common in simple, desktop-based database systems like **Microsoft Access**.
- **Characteristics**:   
    - The entire DBMS resides on a single machine.
    - Suitable for standalone applications.
    - Not scalable beyond one machine.
    - Limited in terms of security and concurrency handling.
- **Example**: A single user running a database on a local machine.
## Client-Server

In this architecture, the system is divided into two layers: the **client** and the **server**. The client runs the user interface and application logic, while the server holds the database. Clients send requests to the server, and the server processes these requests and sends back the required data.
- **Characteristics**:
    - The **client** handles the presentation and business logic, while the **server** manages the database.
    - Suitable for environments where multiple users need to interact with a central database.
    - Provides better **security** and **concurrency** compared to 1-tier architecture.
    - More scalable, but limited when compared to 3-tier architecture.
- **Example**: Web applications where the client (browser) communicates with the database server through queries.

## Client-Application-Database

This is the most widely used architecture, especially for enterprise-level applications. It introduces an additional **middle layer** (also called the **application or business logic layer**) between the client and the database server. This architecture separates the database from the application logic and user interface.

- **Components**: 
    - **Client Layer (Presentation Layer)**: The user interface, which can be a web browser, mobile app, or desktop application. It communicates with the application layer.
    - **Application Layer (Middle Layer)**: Handles business logic, application-specific rules, and data processing. It receives requests from the client, processes them, and interacts with the database.
    - **Database Layer**: This layer contains the DBMS and the actual database. It manages storage, retrieval, and modification of data.
- **Characteristics**:
    - Enhances **scalability** and **performance** by distributing workloads between layers.
    - Improves **security** by restricting direct access to the database from the client.
    - Easier to maintain and update each layer independently (modular design).
    - Widely used in web-based applications (e.g., **LAMP stack** – Linux, Apache, MySQL, PHP).
- **Examples**:
    - Web applications like **e-commerce platforms**, where a user interacts through a browser (client), and the application server processes business logic and interacts with the database server.
