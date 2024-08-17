---
Solved: true
Difficulty:
  - Easy
Date: 2024-08-15T16:51
Attempted: 2024-08-15T16:51
tags:
  - arrayhashing
  - Recursion
---

## Problem Statement

Given an integer **N** , Print all binary strings of size N which do not contain consecutive 1s.

A binary string is that string which contains only 0 and 1

## Example

N = 3

**Output:**

000 , 001 , 010 , 100 , 101

**Explanation:**

None of the above strings contain consecutive 1s. "110" is not an answer as it has '1's occuring consecutively.

## Constraints

1 <= N <= 20


## Approach
### 1. Brute Force
- **Description:** Generate all the binary combinations possible parse through it and find out the probable ones which will fit.
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** backtracking + if condition to check if its applicable or not.
- **Time Complexity:** 
- **Space Complexity:** 


## Implementation
### Language: Python/Java/C++/Other
```python
class Solution:
    def generateBinaryStrings(self, n):
        # Code here
        res = [] 
        def util(length:int,k:int,string:str) :
            if length == k : 
                res.append(string)
                return 
            util(length,k+1,string+"0")
            if not string or string[-1] == "0" : 
                util(length,k+1,string+"1")
        
        util(n,0,"")
        return res
```

## Explanation

In a backtracking solution we first add `0` without any checks and then add `1` if the previous input is `0` otherwise skip the stack call. This allows us to skip all the combinations where there might be consecutive ones. 

## Additional Notes

There are combination questions which follow a similar format like this, only difference being how the condition is being arranged. 

## References
- [GFG problem](https://www.geeksforgeeks.org/problems/generate-all-binary-strings/1?itm_source=geeksforgeeks&itm_medium=article&itm_campaign=practice_card)
- [Link to any other useful resources](#)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms #TechPlacements