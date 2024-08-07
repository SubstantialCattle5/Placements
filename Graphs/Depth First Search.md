---
tags: []
Solved: false
Date: 2024-08-08T04:20
---
## Description
DFS explores the traversal by following the depth. It goes from the parent to the leaf of the node then backtracks and goes to the other unvisited nodes.

## Steps
List the steps of the algorithm in detail:
1. We start with the root node 
2. We check if the adjacent nodes have been visited
3. if not we just recursively call on them 

## Implementation
### Language: Python
```python
# Add your Python code here
    def dfs(self,node,visited,res,adj) : 
        visited[node] = True 
        res.append(node)
        for n in adj[node] : # goes through all the adjacent nodes
            if not visited[n] : 
                self.dfs(n,visited,res,adj)
    # Function to return a list containing the DFS traversal of the graph.
    def dfsOfGraph(self, V, adj):
        visited = [False] * V
        res = [] 
        self.dfs(0,visited,res,adj)
        
        return res
```


## Complexity Analysis

To determine the time and space complexity of the provided Depth First Search (DFS) implementation for a graph, let's analyze the code step by step.

### Time Complexity

1. **Initialization**:
    - `visited = [False] * V`: This takes \(O(V)\) time because it initializes a list of size \(V\).

2. **DFS Traversal**:
    - `self.dfs(0, visited, res, adj)`: This function call initiates the DFS traversal from node 0.
    - Inside the `dfs` function:
        - `visited[node] = True`: This takes \(O(1)\) time.
        - `res.append(node)`: This takes \(O(1)\) time.
        - `for n in adj[node]`: This loop iterates through all adjacent nodes of the current node. The total number of iterations across all calls to `dfs` is equal to the number of edges in the graph, \(E\).

    - For each adjacent node:
        - `if not visited[n]`: This check takes \(O(1)\) time.
        - `self.dfs(n, visited, res, adj)`: This recursive call is made only once per node, marking it as visited and processing its neighbors.

Overall, each node and each edge is processed exactly once, leading to a time complexity of:
\[ O(V + E) \]

### Space Complexity

1. **Visited List**:
    - `visited = [False] * V`: This requires \(O(V)\) space to store the visited state of each node.

2. **Result List**:
    - `res`: This stores the nodes in the order they are visited, requiring \(O(V)\) space.

3. **Call Stack**:
    - In the worst case, the depth of the recursive call stack can go up to \(O(V)\). This happens in the case of a graph that is essentially a single long path (e.g., a linear graph).

Combining these, the overall space complexity is:
\[ O(V) \]

### Summary

- **Time Complexity**: \(O(V + E)\)
- **Space Complexity**: \(O(V)\)



## Applications

1. **Pathfinding**: Finds paths between nodes in a graph.
2. **Graph Traversal**: Identifies all nodes in connected components.
3. **Topological Sorting**: Orders tasks based on dependencies in a directed acyclic graph.
4. **Maze Generation and Solving**: Creates and solves mazes.
5. **Component Analysis**: Finds strongly connected components in directed graphs.
6. **Puzzle Games**: Solves configuration-based puzzles like Sudoku.
7. **Artificial Intelligence**: Implements search strategies in decision-making algorithms.
8. **Network Analysis**: Assesses network connectivity and structure.
9. **Web Crawlers**: Navigates and indexes web pages by exploring links.

## References
-  [wiki](https://en.wikipedia.org/wiki/Graph_traversal)

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
