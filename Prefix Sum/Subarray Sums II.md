---
tags:
  - usaco
  - prefixsum
Difficulty:
  - medium
Solved: true
Date: 2024-08-17T21:59
---
## Problem Statement

You have probably heard of the game "Rock, Paper, Scissors". The cows like to play a similar game they call "Hoof, Paper, Scissors".

The rules of "Hoof, Paper, Scissors" are simple. Two cows play against each other. They both count to three and then each simultaneously makes a gesture that represents either a hoof, a piece of paper, or a pair of scissors. Hoof beats scissors (since a hoof can smash a pair of scissors), scissors beats paper (since scissors can cut paper), and paper beats hoof (since the hoof can get a papercut). For example, if the first cow makes a "hoof" gesture and the second a "paper" gesture, then the second cow wins. Of course, it is also possible to tie, if both cows make the same gesture.

Farmer John wants to play against his prize cow, Bessie, at $N$ games of "Hoof, Paper, Scissors" ($1≤N≤100,000$). Bessie, being an expert at the game, can predict each of FJ's gestures before he makes it. Unfortunately, Bessie, being a cow, is also very lazy. As a result, she tends to play the same gesture multiple times in a row. In fact, she is only willing to switch gestures at most once over the entire set of games. For example, she might play "hoof" for the first $x$ games, then switch to "paper" for the remaining $N-x$ games.

Given the sequence of gestures FJ will be playing, please determine the maximum number of games that Bessie can win.

## Example
- **Input:** 
	The first line of the input file contains $N$.
	The remaining $N$ lines contain FJ's gestures, each either H, P, or S.
```
5
P
P
H
P
S
```
- **Output:** 
	Print the maximum number of games Bessie can win, given that she can only change gestures at most once.
```
4
```

## Approach
### 1. Brute Force
- **Description:** Use prefix sums and try to find the inflection point for all three moves. The point where the sum is maximum is the answer.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

### 2. Optimized
- **Description:** Use both prefix and suffix sums to reduce the number of operations in the main loop.
- **Time Complexity:** $O(n)$
- **Space Complexity:** $O(n)$

## Pseudocode
```
1. Create prefix sums for all three gestures.
2. Create suffix sums for all three gestures.
3. Find the inflection point for all three cases and find the maximum possible wins.
```

## Implementation
### Language: Python
```python
# Reading input
with open('hps.in', 'r') as file:
    length_of_inputs = int(file.readline().strip())
    moves = [file.readline().strip() for _ in range(length_of_inputs)]

# Arrays to store prefix and suffix wins for each move type
prefix_p = [0] * length_of_inputs
prefix_h = [0] * length_of_inputs
prefix_s = [0] * length_of_inputs

suffix_p = [0] * length_of_inputs
suffix_h = [0] * length_of_inputs
suffix_s = [0] * length_of_inputs

# Calculate prefix arrays
for i in range(length_of_inputs):
    prefix_p[i] = (prefix_p[i-1] if i > 0 else 0) + (1 if moves[i] == 'P' else 0)
    prefix_h[i] = (prefix_h[i-1] if i > 0 else 0) + (1 if moves[i] == 'H' else 0)
    prefix_s[i] = (prefix_s[i-1] if i > 0 else 0) + (1 if moves[i] == 'S' else 0)

# Calculate suffix arrays
for i in range(length_of_inputs-1, -1, -1):
    suffix_p[i] = (suffix_p[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'P' else 0)
    suffix_h[i] = (suffix_h[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'H' else 0)
    suffix_s[i] = (suffix_s[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'S' else 0)

# Maximize the number of wins by choosing the best split point
max_wins = 0

for i in range(length_of_inputs - 1):
    # Try all combinations of gestures before and after the switch
    max_wins = max(max_wins, prefix_p[i] + max(suffix_h[i+1], suffix_s[i+1]))
    max_wins = max(max_wins, prefix_h[i] + max(suffix_p[i+1], suffix_s[i+1]))
    max_wins = max(max_wins, prefix_s[i] + max(suffix_p[i+1], suffix_h[i+1]))

# Consider cases with no switch (full sequence with a single gesture)
max_wins = max(max_wins, prefix_p[-1], prefix_h[-1], prefix_s[-1])

# Output the result
with open('hps.out', 'w') as file:
    file.write(str(max_wins) + '\n')
```

## Explanation
The code calculates prefix and suffix sums for each of the three gestures (P, H, S). It then tries to find the optimal point to switch gestures to maximize the number of wins. The solution considers both scenarios where Bessie switches gestures and where she does not.

Edge cases include scenarios where:
- Bessie might not need to switch gestures at all.
- All gestures might be the same.

## Additional Notes
This problem demonstrates the use of prefix and suffix sums to optimize the solution for large input sizes.

## References
- [Usaco.org](https://usaco.org/index.php?page=viewproblem2&cpid=691)
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

---

Let me know if you need any changes or additions!