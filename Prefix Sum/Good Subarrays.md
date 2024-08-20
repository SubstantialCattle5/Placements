---
tags:
  - usaco
  - codeforces
  - prefixsum
Date: 2024-08-20T18:29
Difficulty:
  - "1600"
Solved: true
---
## Problem Statement

![[Pasted image 20240820183301.png]]

## Example
- **Input:** 
![[Pasted image 20240820183317.png]]


## Approach
### 1. Brute Force
- **Description:** Create all possible subarrays and try to calculate how to add the [[Good Subarrays]].
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** prefix sum hack + sum distribution.
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
```
1. create a prefix sum array 
2. create a new hashmap which would have sum distribution. 
3. there are nc2 ways of creating a good array. 
```

## Implementation
### Language: Python/Java/C++/Other
```python
def solution(numbers) : 
	prefix = [0]*(len(numbers)+1) 
	for idx,number in enumerate(numbers) :
		prefix[idx+1] = prefix[idx] + number

	# distribution 
	freq = dict() 
	for idx,pre in enumerate(prefix) :
		freq[pre-idx] = freq.get(pre-idx,0) + 1 

	res = 0 
	for ff in freq.values() : 
		res += ff * (ff-1) // 2 
	return res
```

## Explanation
1. Creates a prefix sum array.
2. prefix essentially allows us to do this
$$ prefixArray[r] - prefixArray[l] = r-l + 1  $$

4. Rearranging it will result in, 
$$
prefixArray[r] - r = prefixArray[l] - l + 1 
$$
5. So now we just need to check how many times $$prefixArray[r] -r$$ occurs and based on it we run the combinatorics formula $nC_2$

## Additional Notes
 Hate this question. 

## References
- [Codeforces.com](https://codeforces.com/contest/1398/problem/C)
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