---
tags:
  - sorting
cssclasses:
---
## Description

Selection sort is a sorting algorithm that selects the `smallest element` from an unsorted list in each iteration and places that element at the `beginning` of the unsorted list.

## Problem Statement

Standard sorting problems 

## Example
- **Input:** Unsorted Array.
- **Output:** Sorted Array.

## Steps
List the steps of the selection sort in detail:
1. Set the first element as `minimum`.
![[Pasted image 20240807191636.png]]
2. Compare `minimum` with the second element. If the second element is smaller than `minimum`, assign the second element as `minimum`.  

Compare `minimum` with the third element. Again, if the third element is smaller, then assign `minimum` to the third element otherwise do nothing. The process goes on until the last element.

![[Pasted image 20240807191728.png]]
3. After each iteration, `minimum` is placed in the front of the unsorted list. ![[Pasted image 20240807192449.png]]

## Pseudocode

```python
selectionSort(array, size)
  repeat (size - 1) times
  set the first unsorted element as the minimum
  for each of the unsorted elements
    if element < currentMinimum
      set element as new minimum
  swap minimum with first unsorted position
end selectionSort
```

## Implementation
### Language: Python
```python

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print('Sorted Array in Ascending Order:')
print(data)
```

## Complexity Analysis
### Time Complexity

| Best                 | $O(n^2)$ |
| -------------------- | -------- |
| Worst                | $O(n^2)$ |
| Average              | $O(n^2)$ |
| **Space Complexity** | $O(1)$   |
| **Stability**        | No       |

## Applications

The selection sort is used when
- a small list is to be sorted
- cost of swapping does not matter
- checking of all the elements is compulsory
- cost of writing to a memory matters like in flash memory (number of writes/swaps is `O(n)` as compared to `O(n2)` of bubble sort)

## References

- [w3Schools](https://www.w3schools.com/dsa/dsa_algo_selectionsort.php)


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
