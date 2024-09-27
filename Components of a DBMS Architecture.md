---
tags:
  - dbms
  - intro_db
---
1. Database Engine - 
	1. Core service for accessing and managing data.
	2. Responsible for processing **queries**, executing **transactions**, and managing the **storage** of data.
	3. Ensures that all operations follow the rules of **ACID properties**
	4. **Functions**:
		- Query parsing and execution.
		- Transaction processing (ensuring consistency and isolation).
		- Data storage management.
		- Backup and recovery.
2. Database Schema - 
	1. Defines the structure of the data in the database.
	2. relational databases, this is commonly represented by **Entity-Relationship Diagrams (ERDs)**
	3. **Functions**:
		- Defines data structure (tables, fields, keys, relationships).
		- Enforces data integrity rules (constraints, triggers).
3. Query Processor - 
	1. Translates high-level queries written in SQL (Structured Query Language) into low-level instructions that the database can execute.
	2. includes various stages like query parsing, optimization, and execution.
	3. **Components**:
		- **DML Compiler**: Compiles data manipulation queries (e.g., `SELECT`, `INSERT`, `UPDATE`, `DELETE`).
		- **DDL Compiler**: Compiles data definition queries (e.g., `CREATE`, `ALTER`, `DROP`).
		- **Query Optimizer**: Analyzes and determines the most efficient way to execute a query.
4. Transaction Manager - 
	1. responsible for handling transactions, ensuring that they follow **ACID properties**.
	2. ensures that multiple users can concurrently access the database without causing conflicts or data corruption.
	3. Functions: 
	    - Manages transaction execution and isolation.
	    - Ensures consistency and durability of data.
	    - Provides mechanisms for rollback in case of errors.
5. Storage Manager - 
	1. handles the physical storage of data on disk. 
6. Metadata Manager (Data Dictionary) - 
	1. metadata manager maintains the **data dictionary** or catalog, which contains information about the structure of the database, including tables, fields, relationships, indexes, and constraints.
	2. **Functions**:
	    - Stores metadata about the database objects (tables, views, indexes).
	    - Helps in query optimization by providing schema details.
	    - Assists in data integrity and security management.
7. Concurrency Control Manager
	1. component ensures that multiple users can access the database simultaneously without causing inconsistencies or conflicts in the data. 
	2. manages locking, deadlocks, and transaction isolation levels.
	3. **Functions**:
		- Provides mechanisms to handle multiple transactions concurrently.
		- Manages locks and controls access to resources.
		- Prevents data anomalies like **dirty reads** or **lost updates**.
8. Backup and Recovery Manager
	1. The backup and recovery manager ensures that data is protected and can be restored in case of failures such as system crashes, power outages, or hardware malfunctions.
	2. Functions:
	    - Manages backups (full, incremental, differential).
	    - Provides mechanisms for restoring databases to a consistent state after a failure.
	    - Ensures durability of committed transactions.