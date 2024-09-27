---
tags:
  - dbms
  - TechPlacements
---
1. What is DBMS? 
	1. Set of applications or programs that enable users to create and maintain a database.
	2. Enables the storage of data more compactly and securely as compared to a file-based system.
	3. Overcome problems like data inconsistency, data redundancy
2. What is a Database?
	1. an organized, consistent, and logical collection of data that can easily be updated, accessed, and managed
	2. sets of tables or objects (anything created using create command is a database object) which consist of records and fields.
3. Issues with traditional file-based systems that make DBMS a better choice?
	1. absence of indexing
	2. redundancy and inconsistency
	3. lack of concurrency control
	4. Integrity check, data isolation, atomicity, security
4. Different languages present in DBMS.
	1. **DDL(Data Definition Language):**  It contains commands which are required to define the database.  E.g., CREATE, ALTER, DROP, TRUNCATE, RENAME, etc.
	2. **DML(Data Manipulation Language):** It contains commands which are required to manipulate the data present in the database.  E.g., SELECT, UPDATE, INSERT, DELETE, etc.
	3. **DCL(Data Control Language):**  It contains commands which are required to deal with the user permissions and controls of the database system. E.g., GRANT and REVOKE
	4. **TCL(Transaction Control Language):**  It contains commands which are required to deal with the transaction of the database.E.g., COMMIT, ROLLBACK, and SAVEPOINT.
5. ACID properties in DBMS?
	1. [[ACID]] stands for Atomicity, Consistency, Isolation, and Durability
6. Are NULL values in a database the same as that of blank space or zero?
	1. 