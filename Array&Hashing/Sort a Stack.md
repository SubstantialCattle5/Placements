---
Attempted: 2024-08-13T18:05
Date: 2024-08-13T18:05
Difficulty:
  - Easy
Solved: true
tags:
  - arrayhashing
---
## Problem Statement

Given a stack, the task is to sort it such that the top of the stack has the greatest element.

## Example

**Input:**  
Stack: 3 2 1

**Output:**  
Stack: 3 2 1

## Constraints

- \(1 \leq N \leq 100\)

## Approach

### 1. Recursive Approach

1. **Base Case:**  
   The simplest possible input is when the stack has only one element. In this case, the stack is already sorted.

2. **Pattern Visualization:**
   - For a stack with two elements, the larger element should be at the top.
   - For larger stacks, the approach involves sorting the stack minus the top element and then inserting the top element back in its correct position.

3. **Relating Hard Cases to Simpler Cases:**
   - Consider the case of sorting a stack with three elements. If we can sort the stack with two elements and then place the third element correctly, the stack will be sorted.

4. **Generalizing the Pattern:**
   - Pop the top element from the stack.
   - Recursively sort the remaining stack.
   - Insert the popped element back into the stack in its correct position.

5. **Combine the Recursive Pattern with the Base Case:**
   - The recursive function sorts the stack by ensuring that every element is inserted in the correct order as the stack unwinds.

### 2. Optimized Approach

- **Description:** The optimized approach leverages recursion to handle the sorting. The stack is sorted by repeatedly popping the top element, sorting the rest of the stack, and then inserting the popped element back into the sorted stack.

- **Time Complexity:** \(O(N^2)\), where \(N\) is the number of elements in the stack. For each element, the function might traverse the entire stack to place it in the correct position.

- **Space Complexity:** \(O(N)\), due to the recursion stack used during the sorting process.

## Pseudocode

```plaintext
function sortStack(stack):
    if stack is not empty:
        temp = stack.pop()
        sortStack(stack)
        insertInSortedOrder(stack, temp)

function insertInSortedOrder(stack, element):
    if stack is empty OR element > stack.peek():
        stack.push(element)
    else:
        temp = stack.pop()
        insertInSortedOrder(stack, element)
        stack.push(temp)
```

## Implementation

### Language: Python

```python
def sortStack(stack):
    if stack:
        temp = stack.pop()
        sortStack(stack)
        insertInSortedOrder(stack, temp)

def insertInSortedOrder(stack, element):
    if not stack or element > stack[-1]:
        stack.append(element)
    else:
        temp = stack.pop()
        insertInSortedOrder(stack, element)
        stack.append(temp)

# Example usage:
stack = [3, 2, 1]
sortStack(stack)
print(stack)  # Output: [3, 2, 1]
```

### Language: Java

```java
import java.util.Stack;

public class SortStack {
    public static void sortStack(Stack<Integer> stack) {
        if (!stack.isEmpty()) {
            int temp = stack.pop();
            sortStack(stack);
            insertInSortedOrder(stack, temp);
        }
    }

    private static void insertInSortedOrder(Stack<Integer> stack, int element) {
        if (stack.isEmpty() || element > stack.peek()) {
            stack.push(element);
        } else {
            int temp = stack.pop();
            insertInSortedOrder(stack, element);
            stack.push(temp);
        }
    }

    public static void main(String[] args) {
        Stack<Integer> stack = new Stack<>();
        stack.push(3);
        stack.push(2);
        stack.push(1);
        sortStack(stack);
        System.out.println(stack);  // Output: [3, 2, 1]
    }
}
```

### Language: C++

```cpp
#include <iostream>
#include <stack>
using namespace std;

void insertInSortedOrder(stack<int> &stack, int element) {
    if (stack.empty() || element > stack.top()) {
        stack.push(element);
    } else {
        int temp = stack.top();
        stack.pop();
        insertInSortedOrder(stack, element);
        stack.push(temp);
    }
}

void sortStack(stack<int> &stack) {
    if (!stack.empty()) {
        int temp = stack.top();
        stack.pop();
        sortStack(stack);
        insertInSortedOrder(stack, temp);
    }
}

int main() {
    stack<int> stack;
    stack.push(3);
    stack.push(2);
    stack.push(1);
    sortStack(stack);
    while (!stack.empty()) {
        cout << stack.top() << " ";
        stack.pop();
    }  // Output: 3 2 1
}
```

## Explanation

- **Edge Cases:**  
  - **Empty Stack:** The function handles empty stacks gracefully by immediately returning without performing any operations.
  - **Single Element Stack:** The stack is already sorted, so the function doesn't need to perform any sorting.
  - **Stack with Identical Elements:** The function will correctly place identical elements in their original order, maintaining the stability of the sort.

- **How the Code Works:**  
  - The function `sortStack` is called recursively until the stack is empty. Each recursive call pops the top element and then sorts the rest of the stack. The `insertInSortedOrder` function then inserts the popped element back into the stack in its correct position, ensuring the stack is sorted.

## Additional Notes

- This recursive approach is elegant and works well for small to medium-sized stacks. However, for very large stacks, this approach may lead to a deep recursion stack, potentially causing stack overflow errors in languages with limited recursion depth.
- An iterative approach or using a different data structure, such as a priority queue, may be more efficient for very large datasets.

## References

- [LeetCode Problem on Sorting a Stack](#)
- [GeeksforGeeks Article on Stack Sorting Algorithms](https://www.geeksforgeeks.org/sort-stack-using-temporary-stack/)

---

## Metadata

```dataview
table
    Difficulty as "Difficulty",
    Category as "Category"
where contains(file.name, "DSA Question")
```

**Tags:** #DSA #Algorithms #TechPlacements