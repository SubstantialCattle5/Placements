---
tags:
  - codeforces
  - binarysearch
  - dp
  - implementation
Date: 2024-08-17T10:14
Solved: false
Difficulty:
  - "1100"
---
## Problem Statement

Vasiliy likes to rest after a hard work, so you may often meet him in some bar nearby. As all programmers do, he loves the famous drink "Beecola", which can be bought in _n_ different shops in the city. It's known that the price of one bottle in the shop _i_ is equal to _x__i_ coins.

Vasiliy plans to buy his favorite drink for _q_ consecutive days. He knows, that on the _i_-th day he will be able to spent _m__i_ coins. Now, for each of the days he want to know in how many different shops he can buy a bottle of "Beecola".


## Example
### **Input**

The first line of the input contains a single integer _n_ (1 ≤ _n_ ≤ 100 000) — the number of shops in the city that sell Vasiliy's favorite drink.

The second line contains _n_ integers $x_i$ (1 ≤ $x_i$≤ 100 000) — prices of the bottles of the drink in the _i_-th shop.

The third line contains a single integer _q_ (1 ≤ _q_ ≤ 100 000) — the number of days Vasiliy plans to buy the drink.

Then follow _q_ lines each containing one integer $m_i$ (1 ≤$m_i$≤ $10^9$) — the number of coins Vasiliy can spent on the _i_-th day.

### **Output**

Print _q_ integers. The _i_-th of them should be equal to the number of shops where Vasiliy will be able to buy a bottle of the drink on the _i_-th day.

## Constraints

1. **time limit per test  2 seconds**
2. **memory limit per test 256 megabytes**

## Approach
### 1. Brute Force
- **Description:** Implement binary search in a sorted shops array.
- **Time Complexity:** $O(mnlog(n))$
- **Space Complexity:** $O(n+m)$

### 2. Optimized
- **Description:** dp approach should me optimized, but need to checkk out memory limit
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
```java
prices.sort() 
fn binarySearch(prices,money) -> index 
for money in queries : 
	print = binarySearch(prices,money)	
```

## Implementation
### Language: Python
```python
n = int(input()) # Number of shops
prices = list(map(int, input().split())) # Prices in each shop
q = int(input()) # Number of days
queries = []
for _ in range(q):
	queries.append(int(input())) # Amount of money Vasiliy can spend on each day 
# Sort prices for binary search
prices.sort()
# Function to implement binary search
def count_shops(prices, money):
	left, right = 0, len(prices) - 1	
	while left <= right:	
		mid = (left + right) // 2
	if prices[mid] <= money:	
		left = mid + 1
	else : 	
		right = mid - 1
	return left
# Process each query
for money in queries:
	answer = count_shops(prices, money)
	print(answer)
```

## Explanation

So all the shops are sorted in an increasing manner. So we just need to find the index where the shop price would be closest to the money brother has. 
## Additional Notes
Add any additional notes or comments here.

## References
- [Link to Codeforces.com](https://codeforces.com/problemset/problem/706/B)
- [[Binary Search]]

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms #TechPlacements