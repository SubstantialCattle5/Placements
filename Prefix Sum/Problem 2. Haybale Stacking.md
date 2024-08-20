---
tags:
  - usaco
  - prefixsum
Difficulty:
  - Medium
Date: 2024-08-20T14:24
Solved: true
---
## Problem Statement

Feeling sorry for all the mischief she has caused around the farm recently, Bessie has agreed to help Farmer John stack up an incoming shipment of hay bales. She starts with N (1 <= N <= 1,000,000, N odd) empty stacks, numbered 1..N. FJ then gives her a sequence of K instructions (1 <= K <= 25,000), each of the form "A B", meaning that Bessie should add one new haybale to the top of each stack in the range A..B. For example, if Bessie is told "10 13", then she should add a haybale to each of the stacks 10, 11, 12, and 13. After Bessie finishes stacking haybales according to his instructions, FJ would like to know the median height of his N stacks -- that is, the height of the middle stack if the stacks were to be arranged in sorted order (conveniently, N is odd, so this stack is unique). Please help Bessie determine the answer to FJ's question.

## Approach
### 2. Optimized
- **Description:** Create an array called diff which would contain all the slope changes in an array(meaning number of operations) and then use prefix sum on the `dx` array.
- **Time Complexity:** 
- **Space Complexity:** 

## Implementation
### Language: Python/Java/C++/Other
```python
stacks,operations = list(map(int,input().split()))

diff = [0] * (stacks+1) 
for i in range(operations) : 
    left,right = list(map(int,input().split()))
    diff[left] += 1 
    diff[right+1] -= 1

sub_sum = 0 
for idx in range(len(diff)) :
    sub_sum = sub_sum + diff[idx]
    diff[idx] = sub_sum
diff.sort() 

print(diff[len(diff)//2])
```


## Explanation
Explain how your code works here. Discuss any edge cases and how your code handles them.

## Additional Notes
Add any additional notes or comments here.

## References
- [Usaco](https://usaco.org/index.php?page=viewproblem2&cpid=104)
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