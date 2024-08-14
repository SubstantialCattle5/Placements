---
tags:
  - graph
Solved: true
Date: 2024-08-08T04:20
Rating:
  - Medium
---
---
- **Difficulty:** #Medium
- **Category:** #graph
---

## Problem Statement

There are `n` cities. Some of them are connected, while some are not. If city `a` is connected directly with city `b`, and city `b` is connected directly with city `c`, then city `a` is connected indirectly with city `c`.

A **province** is a group of directly or indirectly connected cities and no other cities outside of the group.

You are given an `n x n` matrix `isConnected` where `isConnected[i][j] = 1` if the `ith` city and the `jth` city are directly connected, and `isConnected[i][j] = 0` otherwise.

Return _the total number of **provinces**_.
## Example
**Example 1:**

![](https://assets.leetcode.com/uploads/2020/12/24/graph1.jpg)

**Input:** isConnected = `[[1,1,0],[1,1,0],[0,0,1]]`
**Output:** 2

## Constraints

- `1 <= n <= 200`
- `n == isConnected.length`
- `n == isConnected[i].length`
- `isConnected[i][j]` is `1` or `0`.
- `isConnected[i][i] == 1`
- `isConnected[i][j] == isConnected[j][i]`

## Approach
### 1. Brute Force
- **Description:** implement a bfs + count each time the bfs is called.
#### Time Complexity:$O(n^2)$

Here is the breakdown of the time complexity:

1. **Initialization of the `visited` list:**
   ```python
   visited = [False] * len(isConnected)
   ```
   
   This takes \(O(n)\) time, where \(n\) is the number of cities (nodes) in the graph.

2. **Outer loop to check each node:**
   ```python
   for idx in range(len(isConnected)):
       if not visited[idx]:
           bfs(idx)
           count +=1
   ```
   This loop runs \(n\) times, where \(n\) is the number of cities.

3. **BFS traversal:**
   The BFS function (`bfs(node)`) processes each node and its adjacent nodes. The BFS function uses a queue to traverse all connected nodes starting from the given `node`.

   - The `while not q.empty()` loop runs for each node in the current connected component.
   - Inside the BFS function, there is a nested loop:
     ```python
     for i in range(len(isConnected)):
         if isConnected[n][i] and not visited[i]:
             q.put(i)
             visited[i] = True
     ```
     This inner loop runs \(n\) times for each node in the queue.

Considering the BFS traversal for all nodes in the graph:

- Each node is enqueued and dequeued exactly once.
- For each node, we iterate over all other nodes to check for connections.

Therefore, the BFS function as a whole runs in \(O(n + n^2)\), which simplifies to \(O(n^2)\) since the inner loop runs \(n\) times for each of the \(n\) nodes.

4. **Total Time Complexity:**
   Since the BFS is called for each connected component, and each node is visited exactly once, the overall time complexity is dominated by the BFS traversal.

Thus, the total time complexity of the `findCircleNum` function is \(O(n^2)\).
#### Space Complexity:$O(n)$
### 2. Optimized
- **Description:** disjoint union crack.
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
```
bfs(node,visited,adj)
main() {
adj -> nxn matrix 
visited -> [False] * len(adj)
count -> 0 
for (int i = 0 ; i < len(adj) ; i++) { 
	if not visited[i] : # to check if the index has been visted or not
		bfs(i,visited,adj) 
		count +=1 
}
}
```

## Implementation
### Language: Python

```python
from queue import Queue 

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        visited = [False] * len(isConnected)
        count = 0
        def bfs(node) :
            q = Queue() 
            q.put(node)
            while not q.empty() : 
                n = q.get() 
                visited[n] = True 
                for i in range(len(isConnected)) : 
                    if isConnected[n][i] and not visited[i] : 
                        q.put(i)
                        visited[i] = True 


        for idx in range(len(isConnected)) : 
            if not visited[idx] : 
                bfs(idx)
                count +=1 
        
        return count 
       
```


## Explanation
Explain how your code works here. Discuss any edge cases and how your code handles them.

## Additional Notes
The most optimized method is using disjointed union for dense graphs need to figure out how to implement those. 

## References
- [Leetcode](https://leetcode.com/problems/number-of-provinces/description/)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements