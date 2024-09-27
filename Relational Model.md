---
tags:
  - dbms
  - db-models-relationship
---
## **Relational Model Overview**

1. **Inspired by the Entity-Relationship (ER) Model**.
2. **Uses a collection of tables** to represent both data and the relationships among the data.
3. **Tables are also known as relations** in the relational model.
4. The relational model is an example of a **record-based model**, named because the database is structured into fixed-format records of various types.

---

## **Important Terms**

1. **Attribute**: Properties that define an entity (e.g., `name`, `age`, `studentID`).
   
2. **Relation Schema**: Defines the structure of a relation (or table). Example: `Student(uid, name, teacher)`, where `uid`, `name`, and `teacher` are attributes of the relation.

3. **Tuple**: Each row in a relation is known as a tuple. It represents a single record in the table.

4. **Relation Instance**: The set of tuples in a relation at a specific point in time is called a relation instance. It changes as the database updates.

5. **Degree**: The number of attributes (columns) in a relation. For example, if a table has 3 attributes (`uid`, `name`, `teacher`), its degree is 3.

6. **Cardinality**: The number of tuples (rows) in a relation, representing the total number of records.

7. **Keys**: Attributes or sets of attributes used to identify tuples in a relation.

### **Types of Keys**

1. **Primary Key**:
   - Uniquely identifies a tuple (row) in a relation.
   - Cannot be `null`.
   - Each relation can have only one primary key.
   - It is a minimal super key.

2. **Candidate Key**:
   - A set of attributes that can uniquely identify a tuple in a relation.
   - There can be multiple candidate keys in a relation.

3. **Super Key**:
   - A set of one or more attributes that can uniquely identify a tuple in a relation. It may have redundant attributes.

4. **Foreign Key**:
   - An attribute in one relation that refers to the primary key of another relation, establishing a relationship between the two tables.

5. **Alternate Key**:
   - Any candidate key that is not chosen as the primary key.

6. **Composite Key**:
   - A key consisting of two or more attributes that together uniquely identify a tuple in a relation.

---

## **Constraints in the Relational Model**

1. **Domain Constraints**:
   - Attribute-level constraints that specify valid data for attributes (e.g., `AGE > 0`).

2. **Key Integrity**:
   - The primary key must be unique and cannot be `null`.

3. **Referential Integrity**:
   - An attribute in one relation can only take values that exist in the referenced attribute of another (or the same) relation.

---

## **Anomalies in the Relational Model**

An **anomaly** refers to an irregularity or deviation from the expected or normal state. In relational databases, anomalies can arise during **Insert**, **Update**, or **Delete** operations.

### **Insertion Anomaly (in Referencing Relations)**

An insertion anomaly occurs when you cannot insert a row into a referencing relation because the referencing attribute's value is not present in the referenced relation.  
**Example**: Trying to insert a student with `BRANCH_CODE = 'ME'` in the `STUDENT` table will result in an error if 'ME' is not present in the `BRANCH` table.

### **Deletion/Update Anomaly (in Referenced Relations)**

A deletion or update anomaly occurs when you cannot delete or update a row in a referenced relation because the referenced attribute's value is being used by a referencing relation.  
**Example**: Trying to delete a row with `BRANCH_CODE = 'CS'` in the `BRANCH` table will cause an error if that `BRANCH_CODE` is referenced in the `STUDENT` table. However, if `BRANCH_CODE = 'CV'` is not referenced, it can be deleted.

### **On Delete Cascade**

This rule deletes tuples from a referencing relation if the value in the referenced relation is deleted.  
**Example**: Deleting the row with `BRANCH_CODE = 'CS'` from the `BRANCH` table will also delete rows in the `STUDENT` table with `BRANCH_CODE = 'CS'`.

### **On Update Cascade**

This rule updates the referencing relation's attribute if the value of the referenced relation is updated.  
**Example**: Updating `BRANCH_CODE = 'CS'` to `BRANCH_CODE = 'CSE'` in the `BRANCH` table will also update rows in the `STUDENT` table that had `BRANCH_CODE = 'CS'` to `CSE`.

---

## **Advantages of the Relational Model**

- **Simplicity**: Relational models are easier to understand and use compared to other models.
- **Flexibility**: They offer greater flexibility when handling data.
- **Security**: The relational model provides a higher level of data security.
- **Data Accuracy**: It helps in maintaining accurate data.
- **Data Integrity**: Integrity constraints ensure data consistency.
- **Ease of Operations**: Operations like querying and updating are relatively simple.

---

## **Disadvantages of the Relational Model**

- Not well-suited for very large databases.
- Finding relationships between tables can sometimes be challenging.
- Query response time can be slow due to complex structures.

---

## **Characteristics of the Relational Model**

- Data is stored in tables (relations), with rows and columns representing entities and attributes.
- The model supports operations such as data definition, data manipulation, and transaction management.
- Each column represents a distinct attribute, and each row represents a single entity.
