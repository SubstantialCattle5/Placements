---
tags:
  - codeforces
  - greedy
Date: 2024-08-08T00:13
Difficulty:
  - "800"
Solved: true
---
---
- **Difficulty:** #800rating
- **Category:** Greedy
---

## Problem Statement
Given an integer `s`, find the minimum number with the sum of digits equal to `s` such that all digits are distinct.

## Example
- **Input:**
  ```
  4
  20
  8
  45
  10
  ```
- **Output:**
  ```
  389
  8
  123456789
  19
  ```

## Constraints
- \(1 \leq t \leq 45\)
- \(1 \leq s \leq 45\)

## Approach
### Brute Force
- **Description:** Generate all possible numbers with distinct digits and check their sums.
- **Time Complexity:** High, not feasible for large input ranges.
- **Space Complexity:** High, storing all possible numbers.

### Optimized
- **Description:** Use a greedy approach to construct the number from the highest possible digits while keeping the sum constraint.
- **Time Complexity:** \(O(1)\), as the maximum number of digits is limited (at most 9).
- **Space Complexity:** \(O(1)\)

## Pseudocode
```
function minimumVariedNumber(s):
    if s > 45:
        return -1  // Not possible as 1+2+...+9 = 45
    
    result = []
    current_digit = 9
    
    while s > 0:
        if s >= current_digit:
            result.append(current_digit)
            s -= current_digit
        else:
            result.append(s)
            s = 0
        current_digit -= 1
    
    return result reversed as a single number
```

## Implementation
### Language: Python
```python
def minimum_varied_number(t, test_cases):
    results = []
    for s in test_cases:
        if s > 45:
            results.append(-1)  # Not possible case
            continue
        
        result = []
        current_digit = 9
        
        while s > 0:
            if s >= current_digit:
                result.append(current_digit)
                s -= current_digit
            else:
                result.append(s)
                s = 0
            current_digit -= 1
        
        result.reverse()
        number = int(''.join(map(str, result)))
        results.append(number)
    
    return results

# Reading input
t = int(input())
test_cases = [int(input()) for _ in range(t)]

# Getting results
results = minimum_varied_number(t, test_cases)

# Printing results
for result in results:
    print(result)
```

## Explanation
This solution constructs the minimum number by starting with the largest possible digit (9) and adding it to the result list if it does not exceed the remaining sum `s`. It continues this process by decrementing the digit until the sum `s` is reduced to zero. The resulting digits are then reversed to form the smallest possible number.

### Edge Cases
- When `s` is exactly 45, the result should be `123456789`.
- When `s` is a single digit, the result is the digit itself.

## Additional Notes
This approach ensures the number is the smallest by always trying to use the largest digits first and stopping as soon as the exact sum is formed.

## References
- [Codeforces.com](https://codeforces.com/contest/1714/problem/C)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements