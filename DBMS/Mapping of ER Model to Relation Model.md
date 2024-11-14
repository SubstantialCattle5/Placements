---
tags:
  - db-models-relationship
---
The process of **mapping an Entity-Relationship (ER) model to a Relational model** is an important step in database design. It involves transforming the high-level conceptual design (ER diagrams) into a practical, logical design that can be implemented in a relational database. Each component of the ER model, such as entities, attributes, and relationships, is converted into tables (also known as relations) in the relational model.

Here’s a step-by-step guide on how to map various elements of an ER model into a relational model:

---

### **1. Mapping Entities to Relations (Tables)**

Each **entity** in the ER model is mapped to a **relation (table)** in the relational model.

#### Example:
Consider the entity `Student` with attributes `studentID`, `name`, and `age`:

**ER Model**:
```
Student
---------
studentID
name
age
```

**Relational Model** (as a table):
```
Student(studentID, name, age)
```

In this case:
- The entity name becomes the table name (`Student`).
- The attributes of the entity become the columns of the table (`studentID`, `name`, `age`).
- The **primary key** (uniquely identifying the entity) in the ER model is carried over as the **primary key** in the table (e.g., `studentID`).

---

### **2. Mapping Weak Entities**

A **weak entity** is dependent on another entity (its owner or parent entity) and doesn't have a primary key of its own. When mapping weak entities, we must also include the **foreign key** from the owner entity and the **partial key** (discriminator) of the weak entity.

#### Example:
Consider a weak entity `Dependent` related to `Employee`, where `Dependent` depends on the `Employee` entity:

**ER Model**:
```
Employee(employeeID, name)
Dependent(dependentName, relationship, employeeID)  // weak entity
```

**Relational Model**:
```
Employee(employeeID, name)   // Table for owner entity
Dependent(dependentName, relationship, employeeID)   // Table for weak entity
```

Here:
- `employeeID` is the foreign key that references the `Employee` table.
- `dependentName` and `relationship` are the attributes of the weak entity.
- The combination of `dependentName` and `employeeID` will act as the composite primary key for the `Dependent` table.

---

### **3. Mapping Attributes**

- **Simple Attributes**: These are directly mapped to columns in the relational model.

- **Composite Attributes**: Composite attributes are divided into their individual components. Each component is mapped as a separate column.

  **Example**:
  If `Address` is a composite attribute with `Street`, `City`, and `ZIP`, then it will be mapped like this:
  ```
  Address(Street, City, ZIP)
  ```

- **Multivalued Attributes**: A multivalued attribute can have multiple values for a single entity. In the relational model, multivalued attributes are typically stored in a separate table, where the primary key of the original entity is used as a foreign key.

  **Example**:
  If an `Employee` has multiple `phoneNumbers`, you would create a separate table for phone numbers:
  ```
  Employee(employeeID, name)
  EmployeePhone(employeeID, phoneNumber)  // Multivalued attribute stored here
  ```

---

### **4. Mapping Relationships**

Relationships between entities in the ER model need to be translated into relations (tables) in the relational model. The way relationships are mapped depends on the **cardinality** (i.e., the number of entities that can be related to another entity).

#### **Types of Relationships:**

1. **One-to-One (1:1) Relationship**:
   - The foreign key can be placed in either of the two tables, or a separate relation can be created for the relationship.
   
   **Example**:
   If a `Person` has one `Passport`, you can place the `passportID` as a foreign key in the `Person` table:
   ```
   Person(personID, name, passportID)
   Passport(passportID, issueDate)
   ```

2. **One-to-Many (1:N) Relationship**:
   - The primary key from the "one" side is included as a foreign key in the table on the "many" side.

   **Example**:
   A `Professor` teaches many `Courses`:
   ```
   Professor(professorID, name)
   Course(courseID, title, professorID)  // Foreign key in the Course table
   ```

3. **Many-to-Many (M:N) Relationship**:
   - A new relation (table) is created to represent the relationship. This table will contain foreign keys from both participating entities.

   **Example**:
   `Students` can enroll in many `Courses`, and each course can have many students. A new table `Enrollment` is created to manage this many-to-many relationship:
   ```
   Student(studentID, name)
   Course(courseID, title)
   Enrollment(studentID, courseID)  // Join table to represent the relationship
   ```

   In the `Enrollment` table, both `studentID` and `courseID` together form the **composite primary key**.

---

### **5. Mapping Participation Constraints**

- **Total Participation**: If an entity must participate in a relationship (total participation), you might need to ensure the foreign key constraint is mandatory (i.e., it cannot be `NULL`).
  
- **Partial Participation**: If participation is optional, the foreign key can be allowed to have `NULL` values.

---

### **6. Mapping Recursive Relationships**

A **recursive relationship** occurs when an entity is related to itself. In the relational model, this can be handled by adding a foreign key to the same table.

#### Example:
An employee who manages another employee:
```
Employee(employeeID, name, managerID)  // managerID is a foreign key referencing employeeID
```

---

### **Example of Mapping ER Model to Relational Model**

Let's consider a simplified ER diagram of `Student`, `Course`, and the `Enrollment` relationship:

#### ER Model:
```
Entities:
Student(studentID, name, age)
Course(courseID, title, credits)

Relationships:
Enrollment(Student, Course)
```

#### Mapping to Relational Model:
1. **Student Table**:
   ```
   Student(studentID, name, age)
   ```

2. **Course Table**:
   ```
   Course(courseID, title, credits)
   ```

3. **Enrollment Table** (for M:N relationship):
   ```
   Enrollment(studentID, courseID)  // Composite primary key with both studentID and courseID
   ```

Here, the `Enrollment` table is created to map the many-to-many relationship between `Student` and `Course`.
