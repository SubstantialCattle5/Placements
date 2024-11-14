---
tags:
  - db_normal_form
---
**Second Normal Form (2NF)** is the next step in database normalization after 1NF. A relation is said to be in 2NF if:

1. **It is in First Normal Form (1NF)**.
2. **No partial dependency exists**: All non-key attributes must depend on the entire primary key, not just a part of it. This rule applies only to tables where the primary key is composite (i.e., consists of multiple columns).

#### Example: Non-2NF Table

Consider a table that stores information about students, their courses, and their instructors:

| Student_ID | Course    | Instructor | Student_Name |
|------------|-----------|------------|--------------|
| 1          | Math      | Dr. Smith  | John         |
| 1          | Physics   | Dr. Brown  | John         |
| 2          | Chemistry | Dr. Green  | Alice        |
| 3          | Math      | Dr. Smith  | Bob          |
| 3          | Chemistry | Dr. Green  | Bob          |

**Primary Key**: `(Student_ID, Course)`  
In this table, `Student_Name` depends only on `Student_ID` (part of the primary key), and `Instructor` depends only on `Course` (another part of the primary key). These are **partial dependencies**, which violate the rules of 2NF.

#### Converting to 2NF:

To remove partial dependencies, we need to split the table into two or more tables so that non-key attributes depend on the entire primary key.

1. **Student Details Table**:
   Store the student information separately, which depends only on `Student_ID`.

   | Student_ID | Student_Name |
   |------------|--------------|
   | 1          | John         |
   | 2          | Alice        |
   | 3          | Bob          |

2. **Course Details Table**:
   Store the course and instructor details separately, which depend only on `Course`.

   | Course    | Instructor |
   |-----------|------------|
   | Math      | Dr. Smith  |
   | Physics   | Dr. Brown  |
   | Chemistry | Dr. Green  |

3. **Enrollment Table**:
   Store the relationships between students and courses, where the composite primary key is now fully utilized.

   | Student_ID | Course    |
   |------------|-----------|
   | 1          | Math      |
   | 1          | Physics   |
   | 2          | Chemistry |
   | 3          | Math      |
   | 3          | Chemistry |

Now, the table structure adheres to 2NF, as all non-key attributes depend on the whole primary key, and there are no partial dependencies.

