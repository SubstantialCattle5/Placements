---
tags:
  - usaco
  - prefixsum
Date: 2024-08-17T15:49
Solved: true
Difficulty:
  - very easy
---
## Problem Statement
Farmer John has **N** cows, each assigned a breed ID: 1 for Holsteins, 2 for Guernseys, and 3 for Jerseys. The cows are standing in a row, and Farmer John wants to know the count of each breed within certain intervals. Given **N** and **Q** queries, where each query asks for the counts of each breed in a specific range, provide the counts for each query.

- **Input:** The first line contains two integers **N** (number of cows) and **Q** (number of queries). The next **N** lines contain a single integer representing the breed ID of a cow. The following **Q** lines each contain two integers **a** and **b** representing the range [a, b].

- **Output:** For each query, output three integers representing the counts of Holsteins (breed 1), Guernseys (breed 2), and Jerseys (breed 3) within the interval [a, b].

## Example
- **Input:**
  ```
  7 3
  1
  2
  1
  3
  2
  1
  3
  1 3
  2 4
  5 7
  ```
- **Output:**
  ```
  2 1 0
  1 1 1
  1 0 2
  ```

## Constraints
- $1 <= N <= 100,000$
- $1 <= Q <= 100,000$
- $1 <= a <= b <= N$
- Each cow's breed ID is either 1, 2, or 3.

## Approach

### 1. Brute Force
- **Description:** For each query, iterate through the cows in the given range and count the number of Holsteins, Guernseys, and Jerseys.
- **Time Complexity:** \(O(N \times Q)\)
- **Space Complexity:** \(O(1)\)

### 2. Optimized
- **Description:** Use prefix sums to precompute the counts of each breed up to each cow in the line. For each query, calculate the breed counts using the difference between the prefix sums at the endpoints of the interval.
- **Time Complexity:** \(O(N + Q)\)
- **Space Complexity:** \(O(N)\)

## Pseudocode

### Optimized Approach

```
Input: N, Q
Initialize prefix arrays for Holsteins, Guernseys, Jerseys of size N+1

For i from 1 to N:
    Read breed ID
    Update prefix sums for Holsteins, Guernseys, Jerseys

For each query (a, b):
    holsteins_count = prefix_holsteins[b] - prefix_holsteins[a-1]
    guernseys_count = prefix_guernseys[b] - prefix_guernseys[a-1]
    jerseys_count = prefix_jerseys[b] - prefix_jerseys[a-1]
    Output holsteins_count, guernseys_count, jerseys_count
```

## Implementation

### Language: Python
```python
# Open input and output files
with open('bcount.in', 'r') as fin:
    with open('bcount.out', 'w') as fout:
        # Read input values for the number of cows and number of queries
        number_of_cows, number_of_queries = map(int, fin.readline().split())

        # Initialize prefix sum arrays for each breed
        prefix_holsteins = [0] * (number_of_cows + 1)
        prefix_guernseys = [0] * (number_of_cows + 1)
        prefix_jerseys = [0] * (number_of_cows + 1)

        # Fill the prefix sum arrays
        for i in range(1, number_of_cows + 1):
            cow = int(fin.readline().strip())
            prefix_holsteins[i] = prefix_holsteins[i - 1] + (1 if cow == 1 else 0)
            prefix_guernseys[i] = prefix_guernseys[i - 1] + (1 if cow == 2 else 0)
            prefix_jerseys[i] = prefix_jerseys[i - 1] + (1 if cow == 3 else 0)

        # Process each query
        for _ in range(number_of_queries):
            query_i, query_j = map(int, fin.readline().split())
            
            # Calculate the number of cows of each breed in the range [query_i, query_j]
            holsteins_count = prefix_holsteins[query_j] - prefix_holsteins[query_i - 1]
            guernseys_count = prefix_guernseys[query_j] - prefix_guernseys[query_i - 1]
            jerseys_count = prefix_jerseys[query_j] - prefix_jerseys[query_i - 1]
            
            # Write the result for this query to the output file
            fout.write(f"{holsteins_count} {guernseys_count} {jerseys_count}\n")
```

## Explanation
This solution precomputes the counts of each breed up to every cow using prefix sums. This allows us to answer each query in constant time by subtracting the prefix sums of the interval's endpoints. This method efficiently handles large inputs.

## Additional Notes
- Handle edge cases where the interval is the entire range, or where there's only one cow in the interval.
- The prefix sum approach reduces the complexity significantly, making it feasible to handle the maximum constraints.

## References
- [Usaco org](https://usaco.org/index.php?page=viewproblem2&cpid=572)
- [[1D Prefix Sum]]

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA  #TechPlacements