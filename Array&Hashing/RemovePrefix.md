---
tags:
  - codeforces
  - arrayhashing
Date: 2024-08-07T22:35
Difficulty:
  - "800"
Solved: true
---

- **Difficulty:** #800rating
- **Category:** #Array #HashTable #Greedy

## Problem Statement

Polycarp was presented with some sequence of integers $a_𝑎$ of length $n_𝑛$ 
($1≤a_i≤n_1≤𝑎_𝑖≤𝑛$). A sequence can make Polycarp happy only if it consists of different numbers (i.e. distinct numbers).

In order to make his sequence like this, Polycarp is going to make some (possibly zero) number of moves.

In one move, he can:

- remove the first (leftmost) element of the sequence.

For example, in one move, the sequence `[3,1,4,3]` will produce the sequence `[1,4,3]`, which consists of different numbers.

Determine the minimum number of moves he needs to make so that in the remaining sequence all elements are different. In other words, find the length of the smallest prefix of the given sequence $a_𝑎$, after removing which all values in the sequence will be unique.

## Example
### Input

- The first line of the input contains a single integer `t` (1 ≤ t ≤ 10^4) — the number of test cases.

- Each test case consists of two lines:
  - The first line contains an integer `n` (1 ≤ n ≤ 2 × 10^5) — the length of the given sequence `a`.
  - The second line contains `n` integers `a1, a2, ..., an` (1 ≤ ai ≤ n) — elements of the given sequence `a`.

  It is guaranteed that the sum of `n` values over all test cases does not exceed 2 × 10^5.
```sh
5
4
3 1 4 3
5
1 1 1 1 1
1
1
6
6 5 4 3 2 1
7
1 2 1 7 1 2 1
```
### Output

For each test case, print your answer on a separate line — the minimum number of elements that must be removed from the beginning of the sequence so that all remaining elements are different.
```shell
1
4
0
0
5
```

## Constraints

1. Time limit per test _2 seconds_
2. Memory limit per test _256 megabytes_

## Approach
### 1. Brute Force
- **Description:** created a new set which contains all the unique elements and then while the length of the standard array wasn't equal to or less than the length of the set (which contains all the unique elements) it would remove elements from the left position. 
- **Time Complexity:** $O(n^2)$
- **Space Complexity:** $O(2*n)$
- Code : 
```python
if __name__ == "__main__": 
	number_of_questions = input() 
	for i in range(int(number_of_questions)) : 
		length = input() 
		arr = input() 
		nums = list(map(int,arr.split( ))) 
		count = 0 
		while len(nums) > len(set(nums)) : 
			count +=1 
			num = nums.pop(0)
		print(count)
```

### 2. Optimized
- **Description:** The frequency map hack + window hack.
- **Time Complexity:** $O(n^2)$ 
- **Space Complexity:** $O(n)$

## Pseudocode
Provide the pseudocode for the solution here.

## Implementation
### Language: Python/Java/C++/Other
```python
from collections import defaultdict, deque  
if __name__ == "__main__":
	number_of_questions = int(input())
	for _ in range(number_of_questions):
		length = int(input())
		arr = list(map(int, input().split()))	
		freq = defaultdict(int)	
		count = 0	
		window = deque()		
		for num in arr:		
			# Add to the window and update the frequency map			
			window.append(num)			
			freq[num] += 1			
			# While there are duplicates in the window, adjust the window		
			while freq[num] > 1:			
				removed = window.popleft()				
				freq[removed] -= 1		
				if freq[removed] == 0:			
					del freq[removed]			
			count += 1		
		print(count)
```

## Explanation
Explain how your code works here. Discuss any edge cases and how your code handles them.

## Additional Notes
Add any additional notes or comments here.

## References
- [Codeforces.com](https://codeforces.com/contest/1714/problem/B)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements