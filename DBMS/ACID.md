---
tags:
  - dbms
---
ACID stands for Atomicity, Consistency, Isolation and Durability. 

1. Atomicity - This property reflects the concept of either executing the whole query or executing nothing at all, which implies that if an update occurs in a database then that update should either be reflected in the whole database or should not be reflected at all.
2. **Consistency** - This property ensures that the data remains onsistent before and after a transaction in a database.
3. **Isolation** - This property ensures that each transaction is occurring independently of the others. This implies that the state of an ongoing transaction doesn’t affect the state of another ongoing transaction. 
4. **Durability** - This property ensures that the data is not lost in cases of a system failure or restart and is present in the same state as it was before the system failure or restart.