---
tags:
  - Algorithm
  - sorting
---

## Description

**Bubble sort** is a **sorting algorithm** that compares two adjacent elements and swaps them until they are in the intended order.

Just like the movement of air bubbles in the water that rise up to the surface, each element of the array move to the end in each iteration. Therefore, it is called a bubble sort.

## Example

- **Input:** Unsorted Array.
- **Output:** Sorted Array.

## Steps

![[Pasted image 20240807212743.png]]

## Optimized Bubble Sort Algorithm

In the above algorithm, all the comparisons are made even if the array is already sorted.

This increases the execution time.

To solve this, we can introduce an extra variable swapped. The value of swapped is set true if there occurs swapping of elements. Otherwise, it is set **false**.

After an iteration, if there is no swapping, the value of swapped will be **false**. This means elements are already sorted and there is no need to perform further iterations.

This will reduce the execution time and helps to optimize the bubble sort

## Pseudocode

```typescript
bubbleSort(array)
  swapped <- false
  for i <- 1 to indexOfLastUnsortedElement-1
    if leftElement > rightElement
      swap leftElement and rightElement
      swapped <- true
end bubbleSort
```

## Implementation
### Language: Python
```python
# Bubble sort in Python
# Optimized Bubble sort in Python

def bubbleSort(array):
    
  # loop through each element of array
  for i in range(len(array)):
        
    # keep track of swapping
    swapped = False
    
    # loop to compare array elements
    for j in range(0, len(array) - i - 1):

      # compare two adjacent elements
      # change > to < to sort in descending order
      if array[j] > array[j + 1]:

        # swapping occurs if elements
        # are not in the intended order
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp

        swapped = True
          
    # no swapping means the array is already sorted
    # so no need for further comparison
    if not swapped:
      break

data = [-2, 45, 0, 11, -9]

bubbleSort(data)

print('Sorted Array in Ascending Order:')
print(data)
```


## Complexity Analysis

| Best                 | $O(n)$   |
| -------------------- | -------- |
| Worst                | $O(n^2)$ |
| Average              | $O(n^2)$ |
| **Space Complexity** | O(1)     |
| **Stability**        | Yes      |
## Applications

Bubble sort is used if

- complexity does not matter
- short and simple code is preferred

## References
- [Link to any relevant papers, articles, or documentation](#)
- [Link to any related algorithms or topics](#)

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
