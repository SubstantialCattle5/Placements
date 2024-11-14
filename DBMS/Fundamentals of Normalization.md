---
tags:
  - db_normal_form
---
1. Process of organizing data in a database so that it is consistent, efficient, and easy to manage. 
2. Redundant fields should be refactored into smaller pieces.
3. The normalizing procedure depends on the functional dependencies among the attributes inside a table and uses several normal forms to guide the design process.

### The Normalization Process Begins With the Following:
1. **First Normal Form (1NF):** Ensures that each column contains only atomic values that cannot be divided, and each record is unique.
2. **Second Normal Form (2NF):** Includes 1NF and removes subsets of data that would apply for more than one row and places that data in a separate table. It deals with a partial dependency example when a non-key attribute depends on part of a composite primary key.
3. **Third Normal Form(3NF):** This applies further normalization to the schema by removing transitive dependencies, which are where the non-key attributes depend on other non-key attributes.
4. 