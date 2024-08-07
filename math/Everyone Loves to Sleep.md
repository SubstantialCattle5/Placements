---
tags:
  - codeforces
  - math
Date: 2024-08-07T23:59
Difficulty:
  - "900"
Solved: false
---

- **Difficulty:** #900rating
- **Category:** #math 

## Problem Statement

Every day Vlad has to do \( n \) things, each at a certain time. For each of these things, he has an alarm clock set; the \( i \)-th of them is triggered at $h_i$ hours and $m_i$ minutes every day ($0 \leq h_i < 24$, $0 \leq m_i < 60$). Vlad uses the 24-hour time format, so after $h = 12, m = 59$ comes $h = 13, m = 0$,and after $h = 23, m = 59$ comes $h = 0, m = 0$.

This time Vlad went to bed at $H$ hours and $M$ minutes ($0 \leq H < 24$, $0 \leq M < 60$) and asks you to answer: how much he will be able to sleep until the next alarm clock.

If any alarm clock rings at the time when he went to bed, then he will sleep for a period of time of length 0.

## Example

## Input 

The first line of input data contains an integer $(1≤t≤100)$ — the number of test cases in the test.

The first line of the case contains three integers $n$, $H$ and $M$ $(1≤n≤10,0≤H<24,0≤M<60≤𝑛≤10,0≤𝐻<24,0≤𝑀<60)$ — the number of alarms and the time Vlad went to bed.

The following $n$ lines contain two numbers each $hi$ and $mi$ $(0≤hi<24,0≤mi<60)$ — the time of the $i$ alarm. It is acceptable that two or more alarms will trigger at the same time.

Numbers describing time do not contain leading zeros.

```sh
3
1 6 13
8 0
3 6 0
12 30
14 45
6 0
2 23 35
20 15
10 30
```
## Output 

Output $t$ lines, each containing the answer to the corresponding test case. As an answer, output two numbers  — the number of hours and minutes that Vlad will sleep, respectively. If any alarm clock rings at the time when he went to bed, the answer will be 0.

```sh
1 47
0 0
10 55
```

## Approach
### 1. Brute Force
- **Description:** Explain the brute force approach.
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** Explain the optimized approach.
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
Provide the pseudocode for the solution here.

## Implementation
### Language: Python
```python
# Add your code here
```

## Explanation
Explain how your code works here. Discuss any edge cases and how your code handles them.

## Additional Notes
Add any additional notes or comments here.

## References
- [Link to LeetCode/GitHub/GFG problem](#)
- [Link to any other useful resources](#)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements