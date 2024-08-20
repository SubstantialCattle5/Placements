---
tags:
  - usaco
  - prefixsum
Difficulty:
  - easy
Solved: true
Date: 2024-08-20T11:24
---

## Problem Statement
The long road through Farmer John's farm has N crosswalks across it, conveniently numbered $1…N$($1≤N≤100,000$). To allow cows to cross at these crosswalks, FJ installs electric crossing signals, which light up with a green cow icon when it is ok for the cow to cross, and red otherwise. Unfortunately, a large electrical storm has damaged some of his signals. Given a list of the damaged signals, please compute the minimum number of signals that FJ needs to repair in order for there to exist some contiguous block of at least K working signals.

## Example
- **Input:** 
The first line of input contains N, K, and B $(1≤B,K≤N)$. The next $B$ lines each describe the ID number of a broken signal..
- **Output:**
Please compute the minimum number of signals that need to be repaired in order for there to be a contiguous block of $K$ working signals somewhere along the road.
## Approach
### 1. Brute Force
- **Description:** Create a window and calculate the number of ones.
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** create a prefix, and then check if the window has how many ones.
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
```
for window size {
	limit +=1 
	if (encounter a broken light) {
	broken_light +=1 
	} 
	if (limit == k) { 
		check if its the global min 
		limit -=1 
		if window[start] == 1 {
		decrease broken_light by 1 
		}
	}
}
```

## Implementation
### Language: Python/Java/C++/Other
```python
# Add your code here
```



## Explanation
The question can be solved using prefix with window, prefix essentially skips the window size computation and window has to always be of size `k`

## References
- [usaco](https://usaco.org/index.php?page=viewproblem2&cpid=715)
- [[1D Prefix Sum]]

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms #TechPlacements