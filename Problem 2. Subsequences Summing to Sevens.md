---
tags:
  - usaco
  - prefixsum
Date: 2024-08-17T16:02
Difficulty:
  - easy
Solved: true
---
## Problem Statement

Farmer John's N cows are standing in a row, as they have a tendency to do from time to time. Each cow is labeled with a distinct integer ID number so FJ can tell them apart. FJ would like to take a photo of a contiguous group of cows but, due to a traumatic childhood incident involving the numbers 1…6, he only wants to take a picture of a group of cows if their IDs add up to a multiple of 7.

Please help FJ determine the size of the largest group he can photograph.


## Example

- **Input:** 
The first line of input contains N ($1≤N≤50,000$). The next $N$ lines each contain the $N$ integer IDs of the cows (all are in the range $0…1,000,0000$).

- **Output:** 
Please output the number of cows in the largest consecutive group whose IDs sum to a multiple of 7. If no such group exists, output 0.

## Constraints
List any constraints or limitations here.

## Approach
### 1. Brute Force
- **Description:** Explain the brute force approach.
- **Time Complexity:** 
- **Space Complexity:** 

### 2. Optimized
- **Description:** .
- **Time Complexity:** 
- **Space Complexity:** 

## Pseudocode
Provide the pseudocode for the solution here.

## Implementation
### Language: Python/Java/C++/Other
```python
# Open the input and output files
with open('div7.in', 'r') as fin, open('div7.out', 'w') as fout:
    # Read the length of the input
    length_of_input = int(fin.readline().strip())
    
    # Initialize the list to store cow IDs
    cows = list()
    
    # Read all cow IDs
    for _ in range(length_of_input):
        cows.append(int(fin.readline().strip()))
    
    # Initialize the running sum modulo 7 and frequency array
    running_mod = 0
    freq_cows = [-1 for _ in range(7)]
    max_res = 0
    
    # Iterate over the list of cows
    for idx, cow in enumerate(cows):
        running_mod = (running_mod + cow) % 7
        if freq_cows[running_mod] == -1:
            freq_cows[running_mod] = idx
        else:
            max_res = max(max_res, idx - freq_cows[running_mod])
    
    # Write the result to the output file
    fout.write(f"{max_res}\n")
```


## Explanation


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

**Tags:** #DSA #Algorithms #TechPlacements