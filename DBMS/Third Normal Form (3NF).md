---
tags:
  - db_normal_form
---
**Third Normal Form (3NF)** is the next step in database normalization after 2NF. A relation is in 3NF if:

1. **It is in Second Normal Form (2NF)**.
2. **No transitive dependency exists**: A non-key attribute should not depend on another non-key attribute. In other words, all non-key attributes must depend only on the primary key.

#### Example: Non-3NF Table

Consider a table that stores information about students, their courses, and the department where the course is offered:

| Student_ID | Student_Name | Course    | Instructor | Department |
|------------|--------------|-----------|------------|------------|
| 1          | John         | Math      | Dr. Smith  | Science    |
| 2          | Alice        | Chemistry | Dr. Green  | Science    |
| 3          | Bob          | History   | Dr. White  | Humanities |
| 4          | Carol        | Math      | Dr. Smith  | Science    |

**Primary Key**: `Student_ID`  
In this table, `Department` depends on `Course`, not directly on `Student_ID`, which is a **transitive dependency**. This violates 3NF because `Department` should depend only on the primary key (i.e., `Student_ID`), but it depends on another non-key attribute (`Course`).

#### Converting to 3NF:

To remove transitive dependencies, we split the table into two separate tables so that every non-key attribute depends only on the primary key.

1. **Student Enrollment Table**:
   Store student-specific information and the courses they are enrolled in, ensuring all attributes depend only on `Student_ID`.

   | Student_ID | Student_Name | Course    |
   |------------|--------------|-----------|
   | 1          | John         | Math      |
   | 2          | Alice        | Chemistry |
   | 3          | Bob          | History   |
   | 4          | Carol        | Math      |

2. **Course Details Table**:
   Store the course-specific information (including the department), which now only depends on `Course`.

   | Course    | Instructor | Department |
   |-----------|------------|------------|
   | Math      | Dr. Smith  | Science    |
   | Chemistry | Dr. Green  | Science    |
   | History   | Dr. White  | Humanities |

Now, each table is in 3NF:
- **Student Enrollment Table**: All non-key attributes (`Student_Name` and `Course`) depend only on the primary key (`Student_ID`).
- **Course Details Table**: All non-key attributes (`Instructor` and `Department`) depend only on the primary key (`Course`).

---

By converting the table into 3NF, we eliminate transitive dependencies, further reducing redundancy and making the database structure more efficient for updates and maintenance.
