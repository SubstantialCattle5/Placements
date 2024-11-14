---
tags:
  - sql
---
## Sample Data

We will use the `airbnb_listings` sample data, which represents rental apartments on Airbnb:

| id  | city     | country | number_of_rooms | year_listed |
| --- | -------- | ------- | --------------- | ----------- |
| 1   | Paris    | France  | 5               | 2018        |
| 2   | Tokyo    | Japan   | 2               | 2017        |
| 3   | New York | USA     | 2               | 2022        |

## Querying Tables

### Select All Columns

Retrieve all columns from the table:

```sql
SELECT * 
FROM airbnb_listings;
```

### Select Specific Columns

Retrieve only the city column:

```sql
SELECT city 
FROM airbnb_listings;
```

Retrieve the city and year_listed columns:

```sql
SELECT city, year_listed
FROM airbnb_listings;
```

### Order Results

Retrieve listing id and city, ordered by the number of rooms in ascending order:

```sql
SELECT city, year_listed 
FROM airbnb_listings 
ORDER BY number_of_rooms ASC;
```

### Limit Results

Get the first 5 rows from `airbnb_listings`:

```sql
SELECT * 
FROM airbnb_listings
LIMIT 5;
```

### Unique Values

Get a unique list of cities with listings:

```sql
SELECT DISTINCT city
FROM airbnb_listings;
```

## Filtering on Numeric Columns

### Greater Than or Equal To

Retrieve listings with 3 or more rooms:

```sql
SELECT *
FROM airbnb_listings 
WHERE number_of_rooms >= 3;
```

### Less Than

Retrieve listings with fewer than 3 rooms:

```sql
SELECT *
FROM airbnb_listings 
WHERE number_of_rooms < 3;
```

### Range Filtering

Retrieve listings with 3 to 6 rooms:

```sql
SELECT *
FROM airbnb_listings 
WHERE number_of_rooms BETWEEN 3 AND 6;
```

## Filtering on Text Columns

### Specific Value

Retrieve listings in 'Paris':

```sql
SELECT * 
FROM airbnb_listings 
WHERE city = 'Paris';
```

### Multiple Conditions

Retrieve listings in the 'USA' and 'France':

```sql
SELECT *
FROM airbnb_listings 
WHERE country IN ('USA', 'France');
```

## Filtering on Multiple Columns

Retrieve listings in "Paris" with more than 3 rooms:

```sql
SELECT *
FROM airbnb_listings 
WHERE city = 'Paris' AND number_of_rooms > 3;
```

## Handling Missing Data

### Missing Values

Retrieve listings where the number of rooms is missing:

```sql
SELECT *
FROM airbnb_listings 
WHERE number_of_rooms IS NULL; 
```

### Non-Missing Values

Retrieve listings where the number of rooms is present:

```sql
SELECT *
FROM airbnb_listings 
WHERE number_of_rooms IS NOT NULL; 
```

## Simple Aggregations

### Total Rooms

Get the total number of rooms across all listings:

```sql
SELECT SUM(number_of_rooms) 
FROM airbnb_listings; 
```

### Average Rooms

Get the average number of rooms per listing:

```sql
SELECT AVG(number_of_rooms) 
FROM airbnb_listings;
```

### Maximum Rooms

Retrieve the listing with the highest number of rooms:

```sql
SELECT MAX(number_of_rooms) 
FROM airbnb_listings;
```

## Grouping, Filtering, and Sorting 

### Total Rooms by Country

Get the total number of rooms for each country:

```sql
SELECT country, SUM(number_of_rooms)
FROM airbnb_listings
GROUP BY country;
```

### Average Rooms by Country

Get the average number of rooms for each country:

```sql
SELECT country, AVG(number_of_rooms)
FROM airbnb_listings
GROUP BY country;
```

### Number of Listings per Country

Get the count of listings for each country:

```sql
SELECT country, COUNT(id) AS number_of_listings
FROM airbnb_listings
GROUP BY country;
```

---

# SQL Joins Cheat Sheet

This section provides a quick reference for joining data in SQL, allowing you to combine rows from two or more tables based on a related column.

## Sample Data

### Artist Table

| artist_id | name              |
| --------- | ----------------- |
| 1         | AC/DC             |
| 2         | Aerosmith         |
| 3         | Alanis Morissette |

### Album Table

| album_id | title                 | artist_id |
|----------|-----------------------|-----------|
| 1        | For Those Who Rock    | 1         |
| 2        | Dream On              | 2         |
| 3        | Restless and Wild     | 2         |
| 4        | Let There Be Rock     | 1         |
| 5        | Rumours               | 3         |

## Types of Joins

### 1. INNER JOIN

Returns only rows with matching values in both tables:

```sql
SELECT *
FROM ARTIST AS ART
INNER JOIN ALBUM AS ALB
ON ART.ARTIST_ID = ALB.ARTIST_ID;
```

### 2. LEFT JOIN

Returns all rows from the left table and matched rows from the right table (NULL if no match):

```sql
SELECT *
FROM ARTIST AS ART
LEFT JOIN ALBUM AS ALB
ON ART.ARTIST_ID = ALB.ARTIST_ID;
```

### 3. RIGHT JOIN

Returns all rows from the right table and matched rows from the left table (NULL if no match):

```sql
SELECT *
FROM ARTIST AS ART
RIGHT JOIN ALBUM AS ALB
ON ART.ARTIST_ID = ALB.ARTIST_ID;
```

### 4. FULL JOIN

Returns all rows from both tables, with NULL for non-matching rows:

```sql
SELECT *
FROM ARTIST AS ART
FULL OUTER JOIN ALBUM AS ALB
ON ART.ARTIST_ID = ALB.ARTIST_ID;
```

### 5. CROSS JOIN

Produces a Cartesian product of the two tables, returning all combinations:

```sql
SELECT NAME, TITLE
FROM ARTIST
CROSS JOIN ALBUM;
```

## Set Operations

### 6. UNION

Combines results of two or more SELECT statements, removing duplicates:

```sql
SELECT ARTIST_ID
FROM ARTIST
UNION
SELECT ARTIST_ID
FROM ALBUM;
```

### 7. INTERSECT

Returns rows present in both SELECT statements:

```sql
SELECT ARTIST_ID
FROM ARTIST
INTERSECT
SELECT ARTIST_ID
FROM ALBUM;
```

### 8. EXCEPT

Returns rows from the first SELECT that are not in the second:

```sql
SELECT ARTIST_ID
FROM ARTIST
EXCEPT
SELECT ARTIST_ID
FROM ALBUM;
```

## 9. SEMI JOIN

Returns rows from the first table that have matching rows in the second, without including columns from the second table:

```sql
SELECT *
FROM ALBUM
WHERE ARTIST_ID IN
(SELECT ARTIST_ID
 FROM ARTIST);
```

## 10. ANTI JOIN

Returns rows from the first table without matching rows in the second:

```sql
SELECT *
FROM ALBUM
WHERE ARTIST_ID NOT IN
(SELECT ARTIST_ID
 FROM ARTIST);
```

