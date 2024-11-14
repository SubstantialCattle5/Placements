---
tags:
  - db_normal_form
---

### Understanding First Normal Form (1NF)

In database normalization, **First Normal Form (1NF)** is the first step towards organizing a database to reduce redundancy and improve data integrity. A relation is considered to be in 1NF if it follows certain rules.

#### Key Rules of 1NF:
1. **Single-Valued Attributes**: Each column must contain atomic values, meaning no composite or multi-valued attributes are allowed.
2. **Consistent Attribute Domain**: The domain (set of possible values) of attributes must remain consistent across all rows.
3. **Unique Attribute Names**: Every attribute (or column) in the table must have a unique name.
4. **Irrelevant Data Order**: The order in which data is stored in the table does not matter.

#### Example: Non-1NF Table

Consider a table where we store details of students and their enrolled courses:

| Student_ID | Name    | Courses              |
|------------|---------|----------------------|
| 1          | John    | Math, Physics        |
| 2          | Alice   | Chemistry            |
| 3          | Bob     | Math, Chemistry      |

In this example, the `Courses` column contains multiple values (multi-valued attribute), violating the 1NF rule.

#### Converting to 1NF:

To convert the table into 1NF, each multi-valued attribute must be split into separate rows:

| Student_ID | Name    | Course    |
|------------|---------|-----------|
| 1          | John    | Math      |
| 1          | John    | Physics   |
| 2          | Alice   | Chemistry |
| 3          | Bob     | Math      |
| 3          | Bob     | Chemistry |

Now, each column contains atomic values, making the table compliant with the rules of 1NF.
