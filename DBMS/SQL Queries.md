---
tags:
  - sql
---
## SELECT Statement

1. The `SELECT` statement is used to retrieve data from a database.

```sql
SELECT column1, column2, ...  
FROM table_name;
```

2. To return all columns from a table, use the `SELECT *` syntax:

```sql
SELECT *  
FROM table_name;
```

### SQL SELECT DISTINCT Statement

- Use the `DISTINCT` keyword to return only unique values for specified columns:

```sql
SELECT DISTINCT column1, column2, ...  
FROM table_name;
```

- To return the number of distinct countries from the `Customers` table:

```sql
SELECT COUNT(DISTINCT Country)  
FROM Customers;
```

**Note:** `COUNT(DISTINCT column_name)` is not supported in Microsoft Access databases. In such cases, you can use this workaround:

```sql
SELECT COUNT(*) AS DistinctCountries  
FROM (SELECT DISTINCT Country FROM Customers);
```

---

## WHERE Clause

1. The `WHERE` clause is used to filter records that meet specific conditions:

```sql
SELECT column1, column2, ...  
FROM table_name  
WHERE condition;
```

### Numeric Comparison Operators

| **Operator** | **Description**                   | **Example**                                                          |
| ------------ | --------------------------------- | -------------------------------------------------------------------- |
| =            | Equal                             | `SELECT * FROM employees WHERE age = 30;`                            |
| >            | Greater than                      | `SELECT * FROM products WHERE price > 100;`                          |
| <            | Less than                         | `SELECT * FROM products WHERE quantity < 50;`                        |
| >=           | Greater than or equal             | `SELECT * FROM orders WHERE order_date >= '2024-01-01';`             |
| <=           | Less than or equal                | `SELECT * FROM orders WHERE total_amount <= 500;`                    |
| <> or !=     | Not equal                         | `SELECT * FROM employees WHERE department <> 'HR';`                  |
| BETWEEN      | Between a certain range           | `SELECT * FROM sales WHERE amount BETWEEN 1000 AND 5000;`            |
| LIKE         | Search for a pattern              | `SELECT * FROM customers WHERE name LIKE 'A%';`                      |
| IN           | Specify multiple possible values  | `SELECT * FROM employees WHERE department IN ('Sales', 'HR', 'IT');` |

---

## ORDER BY Clause

1. The `ORDER BY` clause is used to sort the result set in either ascending (`ASC`) or descending (`DESC`) order. By default, it sorts in ascending order if `ASC` or `DESC` is not specified.

```sql
SELECT column1, column2, ...  
FROM table_name  
ORDER BY column1 [ASC|DESC], column2 [ASC|DESC], ...;
```

### Examples

- **Example 1: Sorting by a single column in ascending order**  
  Retrieve all employees and sort them by `last_name` alphabetically:

```sql
SELECT * FROM employees  
ORDER BY last_name ASC;
```

- **Example 2: Sorting by a single column in descending order**  
  Retrieve all products and sort them by `price` from highest to lowest:

```sql
SELECT * FROM products  
ORDER BY price DESC;
```

- **Example 3: Sorting by multiple columns**  
  Retrieve all employees and first sort them by `department` in ascending order, and then by `salary` in descending order within each department:

```sql
SELECT * FROM employees  
ORDER BY department ASC, salary DESC;
```

- **Example 4: Sorting using an alias or derived column**  
  You can also use an alias in your `ORDER BY` clause. For instance, if you want to calculate and sort by the total value of an order:

```sql
SELECT order_id, quantity * price_per_unit AS total_value  
FROM orders  
ORDER BY total_value DESC;
```

- **Example 5: Sorting by date**  
  Retrieve all orders and sort them by `order_date` starting from the most recent:

```sql
SELECT * FROM orders  
ORDER BY order_date DESC;
```



## Logical Operators: `AND`, `OR`, `NOT`

1. These logical operators are used in the `WHERE` clause to combine multiple conditions.

### `AND` Operator

- The `AND` operator is used to filter records only when **both** conditions are true.
```sql
SELECT column1, column2, ...   FROM table_name   WHERE condition1   AND condition2;`
```

- **Example 1:** Retrieve employees who are in the "IT" department **and** are older than 30:

```sql
SELECT * FROM employees   WHERE department = 'IT'   AND age > 30;
```
### `OR` Operator

- The `OR` operator is used to filter records when **either** of the conditions is true.

```sql
SELECT column1, column2, ...   FROM table_name   WHERE condition1   OR condition2;
```

- **Example 2:** Retrieve products that have a price greater than 100 **or** are in the "Electronics" category:

```sql
SELECT * FROM products   WHERE price > 100   OR category = 'Electronics';
```

### `NOT` Operator

- The `NOT` operator is used to filter records that **do not** meet a certain condition.

```sql
SELECT column1, column2, ...   FROM table_name   WHERE NOT condition;
```

- **Example 3:** Retrieve customers who are **not** from the country 'USA':

```sql
SELECT * FROM customers   WHERE NOT country = 'USA';
```

### Combining `AND`, `OR`, and `NOT`

- You can combine these operators to create more complex queries. Use parentheses `()` to group conditions for clarity and precedence.

- **Example 4:** Retrieve employees who are in the "HR" department **or** are younger than 25, **but not** from the "Sales" department:

```sql
SELECT * FROM employees   WHERE (department = 'HR'   OR age < 25)   AND NOT department = 'Sales';
```

- **Example 5:** Retrieve products that are either in the "Furniture" category **and** cost less than 500, **or** are in the "Home Decor" category:

```sql
SELECT * FROM products   WHERE (category = 'Furniture'   AND price < 500)   OR category = 'Home Decor';
```


## INSERT INTO Statement

The `INSERT INTO` statement is used to add new records (rows) to a table in the database.

### Syntax 1: Insert into all columns
- If you're inserting data into **all columns**, you don't need to specify the column names (as long as the values match the column order in the table).

```sql
INSERT INTO table_name  
VALUES (value1, value2, ...);
```

- **Example 1:** Inserting a new employee record into the `employees` table with values for all columns:

```sql
INSERT INTO employees  
VALUES (1, 'John', 'Doe', 'IT', 30, '2024-01-01');
```

### Syntax 2: Insert into specific columns
- If you are inserting data into **specific columns**, you must specify the column names in the `INSERT INTO` statement.

```sql
INSERT INTO table_name (column1, column2, ...)  
VALUES (value1, value2, ...);
```

- **Example 2:** Inserting a new product into the `products` table, but only specifying the `product_name` and `price` columns:

```sql
INSERT INTO products (product_name, price)  
VALUES ('Laptop', 1200);
```

### Syntax 3: Insert multiple rows at once
- You can insert multiple rows in one `INSERT INTO` statement by separating the sets of values with commas.

```sql
INSERT INTO table_name (column1, column2, ...)  
VALUES (value1, value2, ...),  
       (value1, value2, ...),  
       (value1, value2, ...);
```

- **Example 3:** Inserting three new records into the `customers` table:

```sql
INSERT INTO customers (customer_id, customer_name, country)  
VALUES (101, 'Alice', 'USA'),  
       (102, 'Bob', 'Canada'),  
       (103, 'Charlie', 'UK');
```
