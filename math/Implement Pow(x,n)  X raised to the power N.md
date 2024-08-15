---
tags:
  - math
Date: 2024-08-11T01:57
Difficulty:
  - Medium
Solved: true
---

## Problem Statement
Given a double x and integer n, calculate x raised to power n. Basically Implement pow(x, n).

## Example
- **Input:** 4.
- **Output:** 16.

## Constraints
- $1 <= n <= 10^{15}$
## Approach
### 1. Brute Force
- **Description:** Loop through it and multiply n till you reach output.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$

### 2. Optimized
- **Description:** Use [[Binary Exponentiation]] to get $O(log(n))$
- **Time Complexity:** $O(log(n))$
- **Space Complexity:** $O(1)$

## Pseudocode

We just need to replicate the [[Binary Exponentiation]] .
```
def fn(x-> number, n-> power) : 
	if n == 0 : 
		return 1 // check for 0 
	if n < 0 : 
		x **=-1 // change the power sign 
		n *= -1 // change the sign  
	if n % 2 == 1 : 
		return x * fn(x,n-1) // if odd then x * x^(n-1), cause n-1 would be even hence divisible 
	else :
		num = fn(x,n//2) // directly sending back the x^n/2 
		return num*num 
```

## Implementation
### Language: Python
```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n == 0 : 
            return 1 
        if n < 0 : 
            x **= -1
            n *= -1 

        if n % 2 == 1 : 
            return x * self.myPow(x,n-1)
        else : 
             num = self.myPow(x,n//2)
             return num*num
```


## Explanation




## Additional Notes
Add any additional notes or comments here.

## References
- [Leetcode problem](https://leetcode.com/problems/powx-n/description/)
- [Striver](https://takeuforward.org/data-structure/implement-powxn-x-raised-to-the-power-n/)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements