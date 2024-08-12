---
tags:
  - graph
  - Matrix
  - Array
Date: 2024-08-11T13:52
Solved: true
Rating:
  - " Medium"
---

## Problem Statement

You are given an `m x n` matrix `maze` (**0-indexed**) with empty cells (represented as `'.'`) and walls (represented as `'+'`). You are also given the `entrance` of the maze, where `entrance = [entrancerow, entrancecol]`denotes the row and column of the cell you are initially standing at.

In one step, you can move one cell **up**, **down**, **left**, or **right**. You cannot step into a cell with a wall, and you cannot step outside the maze. Your goal is to find the **nearest exit** from the `entrance`. An **exit** is defined as an **empty cell** that is at the **border** of the `maze`. The `entrance` **does not count** as an exit.

Return _the **number of steps** in the shortest path from the_ `entrance` _to the nearest exit, or_ `-1` _if no such path exists_.

## Example

**Input:** maze = `[["+","+","+"],[".",".","."],["+","+","+"]]`, entrance = [1,0]
**Output:** 2
**Explanation:** There is 1 exit in this maze at [1,2].
[1,0] does not count as an exit since it is the entrance cell.
Initially, you are at the entrance cell [1,0].
- You can reach [1,2] by moving 2 steps right.
Thus, the nearest exit is [1,2], which is 2 steps away.


## Constraints

- `maze.length == m`
- `maze[i].length == n`
- `1 <= m, n <= 100`
- `maze[i][j]` is either `'.'` or `'+'`.
- `entrance.length == 2`
- `0 <= entrancerow < m`
- `0 <= entrancecol < n`
- `entrance` will always be an empty cell.

## Approach

### Optimized Approach
- **Description:** 
  - We use a breadth-first search (BFS) to find the shortest path from the entrance to the nearest exit. BFS is ideal because it explores all possible paths level by level, ensuring that the first exit found is the nearest one.
  - We start by marking the entrance as visited and explore all four possible directions (up, down, left, right) from the current cell.
  - For each move, we check if it leads to an exit (an empty cell on the border of the maze that isn't the entrance). If so, we return the number of steps taken to reach it.
  - If no exits are found by the end of the BFS, we return `-1`.

- **Time Complexity:** 
  - `O(m * n)` where `m` is the number of rows and `n` is the number of columns in the maze. This is because, in the worst case, we might have to visit every cell in the maze.

- **Space Complexity:** 
  - `O(m * n)` for the `visited` matrix to track visited cells and the BFS queue.

## Pseudocode
```
1. Initialize directions array with the possible moves (up, down, left, right).
2. Initialize a queue for BFS and add the entrance position to it.
3. Initialize a `visited` matrix to track visited cells and mark the entrance as visited.
4. Initialize `min_distance` to 0.

5. While the queue is not empty:
    a. Increment `min_distance`.
    b. For each cell in the current level:
        i. Dequeue the cell (x, y).
        ii. For each direction in directions:
            1. Calculate the new position (nx, ny).
            2. If (nx, ny) is within bounds, not visited, and is an empty cell:
                a. Mark (nx, ny) as visited.
                b. If (nx, ny) is on the border and is not the entrance:
                    - Return `min_distance`.
                c. Enqueue (nx, ny).
                    
6. If no exit is found, return -1.
```

## Implementation
### Language: Python
```python
from queue import Queue
from typing import List

class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        path = Queue()
        path.put(entrance)
        min_distance = 0
        rows, cols = len(maze), len(maze[0])
        
        visited = [[False] * cols for _ in range(rows)]
        visited[entrance[0]][entrance[1]] = True  # Mark entrance as visited

        while not path.empty():
            min_distance += 1
            for _ in range(path.qsize()):
                x, y = path.get()
                
                for dx, dy in directions:
                    nx, ny = x + dx, y + dy
                    
                    if 0 <= nx < rows and 0 <= ny < cols and not visited[nx][ny]:
                        visited[nx][ny] = True
                        
                        if maze[nx][ny] == ".":
                            if nx == 0 or ny == 0 or nx == rows - 1 or ny == cols - 1:
                                if [nx, ny] != entrance:
                                    return min_distance
                            path.put((nx, ny))
        
        return -1  # No exit found
```

## Explanation
- **BFS Initialization:** We begin by setting up a queue for BFS and a `visited` matrix to avoid revisiting cells. The entrance is marked as visited and added to the queue.
- **BFS Execution:** We increment the `min_distance` each time we process a new level of BFS. For each cell, we explore its neighboring cells. If a neighboring cell is an empty cell and on the maze's border (and isn't the entrance), we return the current `min_distance`.
- **Edge Case Handling:** If no exits are reachable, the function returns `-1`.

## Additional Notes
- The BFS ensures that we find the shortest path to the nearest exit.
- This approach handles edge cases such as small mazes, where the entrance might be the only empty cell but not an exit.

## References
- [LeetCode Problem Link](https://leetcode.com/problems/nearest-exit-from-entrance-in-maze/)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #DataStructures #Algorithms #TechPlacements