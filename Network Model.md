---
tags:
  - dbms
  - db-models-relationship
---
### **Network Model in DBMS**

1. The **Network Model** allows the representation of **many-to-many** relationships in a more flexible and complex structure compared to the **Hierarchical Model**.
2. It uses a **graph structure** consisting of **nodes (entities)** and **edges (relationships)** to organize data, enabling more efficient and direct access paths.
3. This model replaces the **hierarchical tree** with a **graph-like structure**, allowing more general connections among different nodes. It supports **many-to-many (M:N)** relationships, where a record can have more than one parent segment.
4. In the **Network Model**, a relationship is called a **set**, and each set consists of at least two types of records:
    - **Owner Record**: Equivalent to the parent in the Hierarchical Model.
    - **Member Record**: Equivalent to the child in the Hierarchical Model.
5. The model allows both **lateral** and **top-down** connections between nodes, making it more flexible than the strictly hierarchical structure.
6. It supports **1:1**, **1:M**, and **M:N** relationships, which helps avoid data redundancy issues by allowing multiple paths to the same record.

### **Key Features of the Network Model**

- **Data Relationship Representation**:  
  The network model uses a **graph structure** to represent data relationships. It allows **many-to-many** relationships, providing greater flexibility in how data is connected.
  
- **Records and Sets**:  
  Data in a network model is organized into **records** (similar to rows in a relational table) and **sets** (defining relationships between records, akin to links in a graph).
  
- **Owner-Member Relationships**:  
  The model defines relationships using **owner-member pairs**, where an owner record can be linked to multiple member records, and a member record can belong to multiple owner records. This structure supports complex relationships.
  
- **Navigational Access**:  
  The network model supports **navigational data access**, where records are accessed through predefined paths, unlike relational models which use declarative query languages like **SQL**.

- **Hierarchical and Non-Hierarchical Structures**:  
  The network model can represent both **hierarchical** (tree-like) and **non-hierarchical** (graph-like) structures, offering greater flexibility in data modeling.

### **Operations in the Network Model**

- **Insertion**:  
  Adding new records and establishing owner-member relationships.
  
- **Deletion**:  
  Removing records while maintaining data integrity by handling related records and relationships.
  
- **Update**:  
  Modifying existing records and the relationships between them.
  
- **Traversal**:  
  Navigating through the network structure to access related records using predefined paths.
  
- **Search**:  
  Retrieving specific records based on criteria by navigating the network structure.

### **Advantages of the Network Model**

1. Handles multiple types of relationships: **1:1**, **1:M**, and **M:N**.
2. Facilitates easy access to data, allowing applications to retrieve both **owner** and **member records** within the same set.
3. Enforces **data integrity** by not allowing a member to exist without an owner.
4. Supports **multi-parent relationships**, providing flexibility in data modeling.

### **Disadvantages of the Network Model**

1. **Complex Schema**:  
   The use of pointers to maintain records leads to operational complexities and potential anomalies.
   
2. **Lack of Query Optimization**:  
   The network model does not support automated query optimization, leading to inefficiencies in query processing.
   
3. **Structural Dependence**:  
   Despite being capable of achieving **data independence**, the model still fails to achieve **structural independence** due to its reliance on physical storage paths.
