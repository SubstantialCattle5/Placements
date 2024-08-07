---
tags: []
Solved: false
Date: 2024-08-08T04:20
---
## Description

In BFS, we are required to traverse the graph breadth-wise or level-wise. This means that we would first move horizontally and visit all the nodes of the current layer before moving on to the next layer.

## Problem Statement

In BFS, we would start traversing from 1 (the root node) and visit its child nodes 8, 5, and 2. We would store them in the order in which they were visited. This would allow us to visit the child nodes of 8 first (i.e. 6, 4, and 3), then of 5 (i.e. null), and then of 2 (i.e. 9) and so on.


## Steps

In order to implement BFS, we use a queue data structure to store the nodes and a visited array to store all the visited nodes.

### Detailed Algorithm Steps:

1. **Initialization:**
   - Create a queue and enqueue the starting node.
   - Mark the starting node as visited.

2. **Process Queue:**
   - While the queue is not empty:
     - Dequeue a node from the queue.
     - For each adjacent node of the dequeued node:
       - If the adjacent node has not been visited:
         - Mark it as visited.
         - Enqueue the adjacent node.

3. **Completion:**
   - Repeat the process until the queue is empty.

## Implementation
### Language: Python

```python
from collections import deque

def bfs(graph, start):
    # Initialize the queue with the starting node
    queue = deque([start])
    # Initialize the visited set with the starting node
    visited = set([start])
    
    # List to store the order of visited nodes
    bfs_order = []

    while queue:
        # Dequeue a node from the queue
        node = queue.popleft()
        bfs_order.append(node)

        # Get all adjacent nodes of the dequeued node
        for neighbor in graph[node]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return bfs_order

# Example usage:
graph = {
    1: [8, 5, 2],
    8: [6, 4, 3],
    5: [],
    2: [9],
    6: [],
    4: [],
    3: [],
    9: []
}

print(bfs(graph, 1))  # Output: [1, 8, 5, 2, 6, 4, 3, 9]
```

## Complexity Analysis

### Time Complexity

The time complexity of BFS is \(O(V + E)\), where \(V\) is the number of vertices (nodes) and \(E\) is the number of edges in the graph. This is because each vertex and each edge is processed exactly once.

### Space Complexity

The space complexity of BFS is \(O(V)\) because, in the worst case, the queue will need to store all vertices in the level order.

## Applications

- **Shortest Path in Unweighted Graph:** BFS can be used to find the shortest path in an unweighted graph.
- **Web Crawlers:** BFS can be used to crawl websites by exploring all the links on a web page before moving on to the links on the next page.
- **Social Networking Sites:** BFS can be used to find the shortest path between two users, suggesting friends of friends.
- **Broadcasting in Networks:** BFS can be used to broadcast a message to all nodes in a network.

## References

- [Breadth-First Search (Wikipedia)](https://en.wikipedia.org/wiki/Breadth-first_search)
- [GeeksforGeeks - Breadth-First Search](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)

---

## Metadata

```dataview
table
    AlgorithmName as "Algorithm Name",
    Complexity as "Time Complexity"
where contains(file.name, "Algorithm")
sort file.ctime desc
```

**Tags:** #Algorithm #TechPlacements #DSA