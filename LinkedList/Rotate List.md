---
tags:
  - LinkedList
  - Medium
solved: true
date: 2024-08-11T01:46
---


- **Difficulty:** Medium
- **Category:** LinkedList

## Problem Statement
Given the `head` of a linked list, rotate the list to the right by `k`places.

## Example
**Input:** head = [1,2,3,4,5], k = 2
**Output:** [4,5,1,2,3]

## Constraints
- The number of nodes in the list is in the range `[0, 500]`.
- `-100 <= Node.val <= 100`
- `0 <= k <= 2 * 109`

## Approach
### 1. Brute Force
- **Description:** add somekind of listener for end node and whenever they try to meet there jump.
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** Solution would be same but rather than end node having a listener(condition) we can create a circular LinkedList and use it to traverse n-k%n (where n is the length of the LinkedList) to find the new head and then disconnect it.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(1)$

## Pseudocode
Provide the pseudocode for the solution here.

## Implementation
### Language: Python/Java/C++/Other
```python
class Solution:
	def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
		if head is None or k == 0 :		
			return head
		length = 1	
		cursor = head	
		while cursor.next :	
			cursor = cursor.next		
			length +=1		
			k%=length		
			cursor.next = head		
			x= length-k		
			for i in range(x) :		
				cursor = cursor.next
				ans = cursor.next
				cursor.next = None			
		return ans
```


## Explanation
it just works. 💪
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