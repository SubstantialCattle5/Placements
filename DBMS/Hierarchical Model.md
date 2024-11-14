---
tags:
  - db-models-relationship
---
1. one of the oldest models in a data model which was developed by IBM, in the 1950s
2. data are viewed as a collection of tables, or we can say segments that form a hierarchical relation
3. data is organized into a tree-like structure where each record consists of one parent record and many children
4. Even if the segments are connected as a chain-like structure by logical associations, then the instant structure can be a fan structure with multiple branches. 
5. We call the illogical associations as directional associations
6. Structure 
	1. segments pointed to by the logical association are called the **child segment**
	2. and other segment is called parent segment
	3. segment without parent is called a root 
	4. segment with no children is called a leaf. 
7. The main disadvantage of the hierarchical model is that it can have one-to-one and one-to-many relationships between the nodes.

**Applications of hierarchical model :**

- Hierarchical models are generally used as semantic models in practice as many real-world occurrences of events are hierarchical in nature like biological structures, political, or social structures.
- Hierarchical models are also commonly used as physical models because of the inherent hierarchical structure of the disk storage system like tracks, cylinders, etc. There are various examples such as Information Management System (IMS) by IBM, NOMAD by NCSS, etc.

**Advantages of the hierarchical model :**

- As the database is based on this architecture the relationships between various layers are logically simple so, it has a very simple hierarchical database structure.
- It has data sharing as all data are held in a common database data and therefore sharing of data becomes practical.
- It offers data security and this model was the first database model that offered data security.
- There’s also data integrity as it is based on the parent-child relationship and also there’s always a link between the parents and the child segments.

**Disadvantages of the hierarchical model :**

- Even though this model is conceptually simple and easy to design at the same time it is quite complex to implement.
- This model also lacks flexibility as the changes in the new tables or segments often yield very complex system management tasks. Here, a deletion of one segment can lead to the involuntary deletion of all segments under it.
- It has no standards as the implementation of this model does not provide any specific standard.
- It is also limited as many of the common relationships do not conform to the 1 to N format as required by the hierarchical model.