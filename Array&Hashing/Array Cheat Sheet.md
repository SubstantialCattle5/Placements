---
tags:
  - Array
---
# **Index**
1. **[[#1. Basic Operations on Arrays]]**
   - Traversal
   - Insertion
   - Deletion
   - Searching
   - Merging

2. [[#2. Sorting Techniques]]
   - Bubble Sort
   - Selection Sort
   - Merge Sort
   - Quick Sort
   - Counting Sort

3. **[[Two-Pointer Technique]]**
   - Finding pairs with a given sum
   - Trapping Rain Water
   - Dutch National Flag Problem

4. **Sliding Window Technique**
   - Maximum sum subarray of size K
   - Longest substring without repeating characters

5. **Prefix Sum / Suffix Sum**
   - Range sum queries
   - Subarray with a given sum

6. **Kadane’s Algorithm**
   - Maximum subarray sum

7. **Binary Search on Arrays**
   - Standard binary search
   - Variants (first/last occurrence, closest element)
   - Search in a rotated sorted array

8. **Matrix Problems (2D Arrays)**
   - Search in a sorted matrix
   - Spiral order traversal
   - Rotate matrix by 90 degrees

9. **Important Problem Patterns**
   - Subarray with a given sum
   - Rearranging array elements
   - Merge two sorted arrays
   - Find the intersection of two arrays
   - Find missing number/duplicate
   - Rearrange array to alternate positive and negative numbers
   - Next permutation

10. **Edge Case Considerations**
    - Arrays of size 0 or 1
    - All elements are the same
    - Target sum/value not present
    - Handling negative numbers

11. **Time and Space Complexity**
    - Time complexity of array operations
    - Space complexity considerations (in-place vs. extra space)




### Basic Operations on Arrays

Arrays are one of the most fundamental data structures, and understanding basic operations on arrays is critical for solving many coding problems.

#### **1.1. Traversal**
Traversal refers to accessing each element of the array. The goal is to visit every element for processing.

- **How**: Typically done using loops (e.g., `for`, `while`).
- **Time Complexity**: O(n), where `n` is the size of the array.
  
   **Example**:
   ```python
   arr = [1, 2, 3, 4, 5]
   for i in arr:
       print(i)
   ```
   - **Use case**: Print all elements, calculate sum, find min/max element.

#### **1.2. Insertion**
Insertion is adding an element at a specific index or at the end of the array. In most array-based problems, it is assumed the array has a fixed size, so insertions can involve shifting elements.

- **At End**: Insertions at the end of the array can be done in O(1).
- **At Specific Position**: Inserting at any index requires shifting elements, which takes O(n) time in the worst case.
  
   **Example**: Insert `x` at index `i`.
   ```python
   arr = [1, 2, 3, 4, 5]
   arr.insert(2, 10)  # Insert 10 at index 2
   print(arr)  # Output: [1, 2, 10, 3, 4, 5]
   ```
   - **Use case**: Add an element to a sorted array, adding a new element while maintaining the order.

#### **1.3. Deletion**
Deletion involves removing an element from the array. Like insertion, deletion can involve shifting elements, which makes it costly in terms of time complexity.

- **From End**: Deletion from the end is O(1).
- **From Specific Position**: Deletion from any index requires shifting the elements after the deleted element, which is O(n).

   **Example**: Delete element at index `i`.
   ```python
   arr = [1, 2, 3, 4, 5]
   arr.pop(2)  # Remove element at index 2
   print(arr)  # Output: [1, 2, 4, 5]
   ```
   - **Use case**: Remove duplicates, delete specific elements while traversing.

#### **1.4. Searching**
Searching refers to finding the index of an element in the array. There are different searching methods based on whether the array is sorted or unsorted.

- **Linear Search**: O(n) time complexity, search for the element by checking each item in the array.
   ```python
   arr = [1, 2, 3, 4, 5]
   target = 3
   for i in range(len(arr)):
       if arr[i] == target:
           print(i)  # Output: 2
   ```
   - **Use case**: Search an element in an unsorted array.
   
- **Binary Search**: O(log n) time complexity, applicable only for sorted arrays.
   ```python
   def binary_search(arr, low, high, target):
       while low <= high:
           mid = (low + high) // 2
           if arr[mid] == target:
               return mid
           elif arr[mid] < target:
               low = mid + 1
           else:
               high = mid - 1
       return -1

   arr = [1, 2, 3, 4, 5]
   target = 3
   print(binary_search(arr, 0, len(arr)-1, target))  # Output: 2
   ```
   - **Use case**: Search for an element in a sorted array efficiently.

#### **1.5. Merging**
Merging involves combining two or more arrays. Depending on the context, merging may require maintaining sorted order.

- **Merge Unsorted Arrays**: O(n + m) time complexity, where `n` and `m` are the sizes of the two arrays.
- **Merge Sorted Arrays**: O(n + m), where you traverse both arrays simultaneously using two pointers.

   **Example**: Merge two sorted arrays.
   ```python
   def merge_sorted_arrays(arr1, arr2):
       result = []
       i = j = 0
       while i < len(arr1) and j < len(arr2):
           if arr1[i] < arr2[j]:
               result.append(arr1[i])
               i += 1
           else:
               result.append(arr2[j])
               j += 1
       result.extend(arr1[i:])
       result.extend(arr2[j:])
       return result

   arr1 = [1, 3, 5]
   arr2 = [2, 4, 6]
   print(merge_sorted_arrays(arr1, arr2))  # Output: [1, 2, 3, 4, 5, 6]
   ```
   - **Use case**: Merging two sorted lists while maintaining the order.

---

### Sorting Techniques

Sorting algorithms are vital for optimizing other operations like searching and merging. Interviewers frequently ask about sorting algorithms, especially focusing on time complexity and stability.

#### **2.1. Bubble Sort**
- **Description**: Repeatedly compare adjacent elements and swap them if they are in the wrong order. This is done until the array is sorted.
- **Time Complexity**: O(n²) in the worst and average case. O(n) if the array is already sorted (with an optimized version).
- **Space Complexity**: O(1) (in-place).
  
   **Example**:
   ```python
   def bubble_sort(arr):
       n = len(arr)
       for i in range(n):
           swapped = False
           for j in range(0, n-i-1):
               if arr[j] > arr[j+1]:
                   arr[j], arr[j+1] = arr[j+1], arr[j]
                   swapped = True
           if not swapped:
               break

   arr = [5, 1, 4, 2, 8]
   bubble_sort(arr)
   print(arr)  # Output: [1, 2, 4, 5, 8]
   ```
   - **Use case**: Rarely used due to inefficiency. However, useful for small datasets or when the array is almost sorted.

#### **2.2. Selection Sort**
- **Description**: Repeatedly select the smallest element from the unsorted portion of the array and place it at the beginning.
- **Time Complexity**: O(n²) in all cases (worst, average, best).
- **Space Complexity**: O(1) (in-place).
  
   **Example**:
   ```python
   def selection_sort(arr):
       n = len(arr)
       for i in range(n):
           min_idx = i
           for j in range(i+1, n):
               if arr[j] < arr[min_idx]:
                   min_idx = j
           arr[i], arr[min_idx] = arr[min_idx], arr[i]

   arr = [64, 25, 12, 22, 11]
   selection_sort(arr)
   print(arr)  # Output: [11, 12, 22, 25, 64]
   ```
   - **Use case**: Simple to understand but inefficient for large datasets.

#### **2.3. Merge Sort**
- **Description**: Divide the array into two halves, recursively sort them, and then merge the sorted halves.
- **Time Complexity**: O(n log n) in all cases.
- **Space Complexity**: O(n) (due to auxiliary space for merging).
  
   **Example**:
   ```python
   def merge_sort(arr):
       if len(arr) > 1:
           mid = len(arr) // 2
           left_half = arr[:mid]
           right_half = arr[mid:]

           merge_sort(left_half)
           merge_sort(right_half)

           i = j = k = 0
           while i < len(left_half) and j < len(right_half):
               if left_half[i] < right_half[j]:
                   arr[k] = left_half[i]
                   i += 1
               else:
                   arr[k] = right_half[j]
                   j += 1
               k += 1

           while i < len(left_half):
               arr[k] = left_half[i]
               i += 1
               k += 1

           while j < len(right_half):
               arr[k] = right_half[j]
               j += 1
               k += 1

   arr = [38, 27, 43, 3, 9, 82, 10]
   merge_sort(arr)
   print(arr)  # Output: [3, 9, 10, 27, 38, 43, 82]
   ```
   - **Use case**: Preferred for large datasets where stability and worst-case guarantees are important.

#### **2.4. Quick Sort**
- **Description**: Pick a pivot element, partition the array such that elements smaller than the pivot are on the left and elements larger are on the right, then recursively sort the two partitions.
- **Time Complexity**: O(n log n) on average, O(n²) in

 the worst case.
- **Space Complexity**: O(log n) for the recursion stack.
  
   **Example**:
   ```python
   def partition(arr, low, high):
       pivot = arr[high]
       i = low - 1
       for j in range(low, high):
           if arr[j] <= pivot:
               i += 1
               arr[i], arr[j] = arr[j], arr[i]
       arr[i + 1], arr[high] = arr[high], arr[i + 1]
       return i + 1

   def quick_sort(arr, low, high):
       if low < high:
           pi = partition(arr, low, high)
           quick_sort(arr, low, pi - 1)
           quick_sort(arr, pi + 1, high)

   arr = [10, 7, 8, 9, 1, 5]
   quick_sort(arr, 0, len(arr) - 1)
   print(arr)  # Output: [1, 5, 7, 8, 9, 10]
   ```
   - **Use case**: Frequently used due to its average-case efficiency, though care must be taken to avoid worst-case behavior.

#### **2.5. Counting Sort**
- **Description**: Counting sort counts the number of occurrences of each element and then arranges them in sorted order.
- **Time Complexity**: O(n + k), where `n` is the number of elements and `k` is the range of input.
- **Space Complexity**: O(k) for the count array.
  
   **Example**:
   ```python
   def counting_sort(arr, max_val):
       count = [0] * (max_val + 1)
       output = [0] * len(arr)

       for num in arr:
           count[num] += 1

       for i in range(1, len(count)):
           count[i] += count[i - 1]

       for num in reversed(arr):
           output[count[num] - 1] = num
           count[num] -= 1

       return output

   arr = [4, 2, 2, 8, 3, 3, 1]
   max_val = max(arr)
   sorted_arr = counting_sort(arr, max_val)
   print(sorted_arr)  # Output: [1, 2, 2, 3, 3, 4, 8]
   ```
   - **Use case**: Efficient for sorting integers when the range of values is limited.





