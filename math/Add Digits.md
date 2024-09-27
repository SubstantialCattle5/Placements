---
tags:
  - math
Difficulty:
  - Easy
Date: 2024-08-14T16:53
Solved: true
---

## Problem Statement

Given an integer `num`, repeatedly add all its digits until the result has only one digit, and return it.

## Example

**Input:** num = 38
**Output:** 2
**Explanation:** The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
## Constraints

$0 <= num <= 2^31 - 1$

## Approach
### 1. Brute Force
- **Description:** Run a recursive operation on add digits and keep on adding the last digit and removing it from the number.Till it reaches the length of one where we check if the response if greater than 10 or not if yes then we again check through it.
- **Time Complexity:** $O(log(n))$
- **Space Complexity:** 

### 2. Optimized
- **Description:** Explain the optimized approach.
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
Provide the pseudocode for the solution here.

## Implementation
### Language: Python/Java/C++/Other
```python
# Add your code here
```


## Explanation
Explain how your code works here. Discuss any edge cases and how your code handles them.

## Additional Notes
Add any additional notes or comments here.

## References
- [Add Digits](https://leetcode.com/problems/add-digits/)
- [Digital Root](https://en.wikipedia.org/wiki/Digital_root)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms 