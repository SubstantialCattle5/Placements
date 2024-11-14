---
tags:
  - db-models-relationship
---

## **Need for Object-Oriented Data Model**

To represent complex real-world problems, there was a need for a data model that closely mirrors reality. The **Object-Oriented Data Model** (OODM) simplifies the representation of real-world scenarios by organizing data as objects. These objects encapsulate both data and behavior, making it easier to represent complex systems.

---

## **Object-Oriented Data Model**

In the **Object-Oriented Data Model**, data and their relationships are encapsulated in a single structure called an **object**. This model represents real-world problems as objects with various attributes, and these objects interact with each other through relationships. Essentially, the OODM combines the principles of **Object-Oriented Programming (OOP)** and the **Relational Database Model**, as illustrated below:

**Object-Oriented Data Model**  
= **Object-Oriented Programming** + **Relational Database Model**

---

## **Components of the Object-Oriented Data Model**

### **1. Objects**

An **object** is an abstraction of a real-world entity, or in other words, an instance of a class. Objects encapsulate both **data** (attributes) and **code** (methods) into a single unit, providing **data abstraction** by hiding the implementation details from the user.  
**Example**: Instances such as Student, Doctor, and Engineer are objects.

### **2. Attributes**

Attributes describe the properties of an object.  
**Example**: For the object `STUDENT`, the attributes could be `Roll no`, `Branch`, and the method `Setmarks()` in the `Student` class.

### **3. Methods**

Methods represent the behavior or actions of an object. In real-world terms, methods define what an object can do.  
**Example**: A method like `Setmarks()` in the `STUDENT` class could represent setting a student’s marks.

### **4. Class**

A **class** is a blueprint for objects, containing shared attributes and methods. An object is an instance of a class.  
**Example**: `Person`, `Student`, `Doctor`, and `Engineer` are classes. All objects of a class share the same structure (attributes) and behavior (methods).

Here’s an example of a class definition:

```cpp
class Student {
    char Name[20];
    int roll_no;
    // Other attributes

public:
    void search();  // Method to search student records
    void update();  // Method to update student details
};
```

In this example, `Student` refers to the class, and `S1`, `S2` can be objects (instances) of the `Student` class created in the main function.

### **5. Inheritance**

**Inheritance** allows a new class to inherit attributes and methods from an existing class (the base class). This promotes reusability and reduces redundancy.  
**Example**: Classes like `Student`, `Doctor`, and `Engineer` can inherit from the base class `Person`.

---

## **Advantages of the Object-Oriented Data Model**

1. **Reusability**: Code can be reused through inheritance, reducing redundancy.
2. **Understandable Structure**: The model is intuitive, as it represents real-world entities and their behaviors.
3. **Lower Maintenance Costs**: Inheritance allows for reusability of attributes and functions, reducing the cost of maintaining code.

---

## **Disadvantages of the Object-Oriented Data Model**

1. **Lack of Development**: The model is not fully developed and standardized, making it less widely adopted by users.
2. **Complexity**: While it simplifies real-world representations, it can be more complex to implement and manage than simpler data models like the relational model.
