---
tags:
  - binarysearch
Solved: true
Date: 2024-08-16T03:59
---
## Problem Statement
Given a sorted array of integers `nums` and a target value `target`, write a function to find the starting and ending position of `target` in `nums`. If `target` is not found in the array, return `[-1, -1]`.

- **Input:** A sorted array `nums` of integers and an integer `target`.
- **Output:** An array of two integers representing the first and last positions of `target` in `nums`. If `target` is not present, return `[-1, -1]`.

## Example
- **Input:** `nums = [5,7,7,8,8,10]`, `target = 8`
- **Output:** `[3, 4]`

- **Input:** `nums = [5,7,7,8,8,10]`, `target = 6`
- **Output:** `[-1, -1]`

## Constraints
- `1 <= nums.length <= 10^5`
- `-10^4 <= nums[i], target <= 10^4`
- `nums` is sorted in non-decreasing order.

## Approach
### 1. Brute Force
- **Description:** 
  - Iterate through the array to find the first occurrence of the `target`. 
  - Continue iterating to find the last occurrence.
  - This approach works but is inefficient for large arrays.
- **Time Complexity:** O(n)
- **Space Complexity:** O(1)

### 2. Optimized
- **Description:** 
  - Use binary search to find the first occurrence of the `target`.
  - Use binary search again to find the last occurrence of the `target`.
  - This approach is more efficient because it reduces the time complexity by using binary search.
- **Time Complexity:** O(log n)
- **Space Complexity:** O(1)

## Pseudocode
```plaintext
function findFirstPosition(nums, target):
    left = 0
    right = len(nums) - 1
    firstPos = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            firstPos = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return firstPos

function findLastPosition(nums, target):
    left = 0
    right = len(nums) - 1
    lastPos = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            lastPos = mid
            left = mid + 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return lastPos

function searchRange(nums, target):
    firstPos = findFirstPosition(nums, target)
    if firstPos == -1:
        return [-1, -1]
    lastPos = findLastPosition(nums, target)
    return [firstPos, lastPos]
```

## Implementation
### Language: Python
```python
def findFirstPosition(nums, target):
    left, right = 0, len(nums) - 1
    firstPos = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            firstPos = mid
            right = mid - 1  # continue searching in the left half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return firstPos

def findLastPosition(nums, target):
    left, right = 0, len(nums) - 1
    lastPos = -1
    
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            lastPos = mid
            left = mid + 1  # continue searching in the right half
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return lastPos

def searchRange(nums, target):
    firstPos = findFirstPosition(nums, target)
    if firstPos == -1:
        return [-1, -1]
    lastPos = findLastPosition(nums, target)
    return [firstPos, lastPos]
```

## Explanation
The code first performs a binary search to find the first occurrence of the target in the sorted array. It continues searching in the left half of the array if the target is found to ensure it's the first occurrence.

Similarly, the code performs another binary search to find the last occurrence of the target by searching the right half after finding a match.

This approach efficiently finds both the first and last positions of the target in the array.

### Edge Cases:
- If `target` is not present in `nums`, the function returns `[-1, -1]`.
- If all elements in `nums` are equal to `target`, the function returns `[0, len(nums) - 1]`.

## Additional Notes
This problem is a classic example of how binary search can be used for more than just finding the presence of an element in a sorted array. It demonstrates the power of binary search in narrowing down the search range efficiently.

## References
- [LeetCode Problem: Find First and Last Position of Element in Sorted Array](https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/)
- [GeeksforGeeks: Binary Search](https://www.geeksforgeeks.org/binary-search/)

---

## Metadata
```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms #TechPlacements #binarysearch
