---
tags:
  - binarysearch
Date: 2024-08-16T02:04
Solved: true
---
## Description

**Binary search** is a method that allows for quicker search of something by splitting the search interval into two. Its most common application is searching values in sorted arrays, however the splitting idea is crucial in many other typical tasks.

## Problem Statement

The most typical problem that leads to the binary search is as follows. You're given a sorted array  $A_0 \leq A_1 \leq \dots \leq A_{n-1}$ , check if   $k$  is present within the sequence. The simplest solution would be to perform a [[linear search]]. This approach would take $O(n)$ and wouldn't take the advantage of the list being a sorted array. 

Assuming we have two arbitrary indexes $L<R$ such that $A_L <= k <= A_R$. Because the array is sorted we will have the above situation or that it won't occur at all. 
If we pick an arbitrary index $M$ which lies b/w L and R, if we compare it with K it would end up generating two cases - 

1. $A_L<=k<=A_M$ where the problem would be reduced to the range $[L,M]$
2. $A_M<=k<=A_R$ where the problem would be reduced to the range $[M,R]$

If its impossible to pick M (condition being $R=L+1$ right next two each other), in that case we compare `k` directly with `L` & `R` . Otherwise we would want to pick $M$  in such manner that it reduces the active segment to a single element as quickly as possible _in the worst case_. 

For that case we end up taking `m` as $M=(L+R)/2$
## Lower Bound and Upper Bound

### **1. Lower Bound**
The **lower bound** of \( k \) in a sorted array is the position of the first element in the array that is **not less than** \( k \). In other words, it's the smallest index where the element is either equal to or greater than \( k \).

For example, consider the sorted array: `[1, 2, 4, 4, 5, 7]`
- The lower bound of \( k = 4 \) is at index `2`, because the first element that is not less than \( 4 \) is `4`, which appears at index `2`.

### **2. Upper Bound**
The **upper bound** of \( k \) in a sorted array is the position of the first element that is **greater than** \( k \). It's the smallest index where the element is strictly greater than \( k \).

Using the same array: `[1, 2, 4, 4, 5, 7]`
- The upper bound of \( k = 4 \) is at index `4`, because the first element greater than `4` is `5`, which appears at index `4`.

### **3. Finding the Range of \( k \)**
By finding both the lower and upper bounds, you can determine the range of elements in the array that are equal to \( k \).

In the previous example:
- Lower bound of \( k = 4 \) is at index `2`.
- Upper bound of \( k = 4 \) is at index `4`.

This means the elements equal to \( k = 4 \) are in the range `[2, 4)` (which includes index `2` and `3` but not `4`).

### **4. Checking if \( k \) is in the Array**
To check whether \( k \) is actually present in the array, you can simply:
1. Find the lower bound of \( k \).
2. Check if the element at this position equals \( k \).

If the element at the lower bound equals \( k \), then \( k \) is present in the array. If not, \( k \) is absent.

### **Example:**
Given array: `[1, 2, 4, 4, 5, 7]` and \( k = 4 \):
- Lower bound of \( k = 4 \) is at index `2`.
- Check if `array[2] == 4` (which it does), so \( k \) is present in the array.
- The upper bound tells us that the elements equal to `4` span from index `2` to index `4` (exclusive).

This approach is efficient, especially for large sorted arrays, as both lower and upper bounds can be found using binary search with a time complexity of \( O(\log n) \).

## Pseudo-code

We maintain a pair $L<R$ such that $A_L<=K<=A_R$, The active search interval being $[L,R)$. We use have closed interval to reduce the number of edge cases. 

1. $R=L+1$, R is the upper bound of $k$.
2. So we end up initializing R with ___past the end index___ and $L$ with ___before the beginning index___   
3. thus, R=length of the array and L=-1 
4. Its fine as long as we don't compute $A_R$, $A_L$ directly. 
5. Formally treating it as $A_R= \infty$ and $A_L= -\infty$. 
6. We specify $M$ as $(L+R)/2$
7. writing `m = l + (r - l) / 2` which always works for positive integer `l` and `r`, but might still overflow if `l` is a negative number
```cpp
... // a sorted array is stored as a[0], a[1], ..., a[n-1]
int l = -1, r = n;
while (r - l > 1) {
    int m = str::midpoint(l,r);
    if (k < a[m]) {
        r = m; // a[l] <= k < a[m] <= a[r]
    } else {
        l = m; // a[l] <= a[m] <= k < a[r]
    }
}
```
## Implementation

### Language: Python
```python
def binary_search(arr, k):
    l, r = 0, len(arr) - 1
    while l <= r:
        m = l + (r - l) // 2  # Calculate midpoint safely
        if arr[m] == k:
            return m
        elif arr[m] < k:
            l = m + 1
        else:
            r = m - 1
    return -1  # Element not found
```

## Complexity Analysis
### Time Complexity
Discuss the time complexity of the algorithm.

### Space Complexity
Discuss the space complexity of the algorithm.

## Applications

### Search on Arbitrary Predicate 

#### The Goal:
We want to find a specific index `L` in an array where a condition (let's call it `f(x)`) changes from `false` (0) to `true` (1). For example, imagine we have an array, and at each index, we check if a certain condition is met. The array is sorted in such a way that all the false values (0s) come before all the true values (1s).

#### How Binary Search Works Here:
1. **Initial Setup:** 
   - You start with two pointers: `l` (left) at the beginning of the array and `r` (right) at the end.
   - `f(l)` is false (0) and `f(r)` is true (1).

2. **Finding the Middle:**
   - You calculate the middle index `m` between `l` and `r`.
   - Check the condition at this middle index: `f(m)`.

3. **Updating Pointers:**
   - If `f(m)` is true, it means the transition from false to true must have happened before or at `m`, so you move `r` to `m`.
   - If `f(m)` is false, it means the transition hasn't happened yet, so you move `l` to `m`.

4. **Narrowing Down:**
   - Each time you do this, the gap between `l` and `r` gets smaller, because you keep narrowing down the section of the array where the transition might be.

5. **Stopping Condition:**
   - The loop stops when `r - l = 1`, meaning the two pointers are next to each other. At this point, `l` is the last index where `f(l)` is false, and `r` is the first index where `f(r)` is true.

#### Results:
- If you find such an `L`, it means `f(L) = 0` and `f(L+1) = 1`.
- If the whole array is false (0), `L` will be `n-1` (the last index).
- If the whole array is true (1), `L` will be `-1`, meaning there was no transition.

#### Why This Works:
- Binary search is efficient because it cuts the problem in half each time, making it much faster than checking every single index.
- The algorithm keeps the important invariant: `f(l) = 0` and `f(r) = 1`, ensuring that the transition point, if it exists, will be found.

So, in essence, this method allows you to efficiently find where a condition changes from false to true in a sorted array.

### Binary search on the answer

Such situation often occurs when we're asked to compute some value, but we're only capable of checking whether this value is at least $i$ .
#### Example 

For example, you're given an array   $a_1,\dots,a_n$  and you're asked to find the maximum floored average sum
$$
\left \lfloor \frac{a_l + a_{l+1} + \dots + a_r}{r-l+1} \right\rfloor
$$
Equivalently, it rewrites as
$$(a_l - \lambda) + (a_{l+1} - \lambda) + \dots + (a_r - \lambda) \geq 0$$

so now we need to check whether there is a subarray of a new array   $a_i - \lambda$  of length at least  $x+1$  with non-negative sum, which is doable with some prefix sums.

### Continuous search

#### 1. **Continuous Function Basics:**
   - Suppose you have a continuous function \( f(x) \) that smoothly changes its value as \( x \) changes.
   - Imagine the function is defined on a specific range \([L, R]\), where \( L \) and \( R \) are just two points on the \( x \)-axis.

#### 2. **Intermediate Value Theorem:**
   - This theorem tells us something simple but powerful: If \( f(L) \) (the value of the function at \( L \)) is less than or equal to \( f(R) \) (the value at \( R \)), then every value between \( f(L) \) and \( f(R) \) will be hit by the function at some point between \( L \) and \( R \).

#### 3. **Finding a Specific Value \( y \):**
   - If you want to find where the function equals a specific value \( y \) (and you know \( y \) is between \( f(L) \) and \( f(R) \)), there must be some point \( x \) in the interval \([L, R]\) where \( f(x) = y \).

#### 4. **Binary Search for \( x \):**
   - To find that \( x \) accurately, you can use a method similar to binary search. 
   - Start by picking the middle point \( M \) of the interval \([L, R]\).
   - Compare \( f(M) \) with \( y \):
     - If \( f(M) \) is greater than \( y \), it means \( x \) must be to the left, so you search in \([L, M]\).
     - If \( f(M) \) is less than or equal to \( y \), search in \([M, R]\).
   - Keep repeating this process, narrowing down the interval until you find \( x \) as close as you want to \( y \).

#### 5. **Example with a Polynomial:**
   - Consider a function like
	$$
	f(x) = x^3 + ax^2 + bx + c 
	$$
   - As \( x \) goes to very negative values (like \( L \) being a large negative number), \( f(x) \) goes to negative infinity. Similarly, as \( x \) goes to very positive values (like \( R \) being a large positive number), \( f(x) \) goes to positive infinity.
   - So, no matter what, by choosing big enough \( L \) and \( R \), you can make sure that \( f(L) < 0 \) and \( f(R) > 0 \).
   - This guarantees that the function must cross the x-axis somewhere between \( L \) and \( R \), meaning there’s a root (where \( f(x) = 0 \)) in that interval.
   - You can use binary search to find this root as accurately as you want.


### Search with powers of 2

### 1. **Basic Idea:**
   - Instead of keeping track of a segment (an interval) where you think the answer is, you maintain two things:
     - A **pointer** \( i \) that tells you your current position.
     - A **power** \( k \) that helps you decide how far to jump from your current position.

### 2. **How It Works:**
   - You start with the pointer \( i \) at the beginning of the range, say \( i = L \).
   - The power \( k \) starts from a large value and decreases over time.

### 3. **The Jumping Strategy:**
   - In each step, you check the position \( i + 2^k \):
     - If the condition (or "predicate") you're testing is still false at this new position, you move the pointer \( i \) to \( i + 2^k \). This means you can skip this section because you know the answer lies beyond this point.
     - If the condition becomes true at \( i + 2^k \), you stay at the current \( i \) because the answer might be closer than this jump.
   - After each test, you decrease \( k \) by 1, which means your jumps get smaller and more precise as you approach the answer.

### 4. **Where It’s Useful:**
   - **Tree Problems:** For example, finding the lowest common ancestor of two nodes in a tree, where you might want to find a common point by jumping in powers of 2 steps.
   - **Fenwick Tree (or Binary Indexed Tree):** If you’re looking for a specific element in a structure like a Fenwick tree, this method can help you quickly narrow down your search.

### 5. **Example:**
   - Imagine you have a line of dominoes and you're trying to find the first one that falls. If you start at the leftmost domino and jump ahead by 4 dominoes (say \( 2^2 = 4 \)), you can quickly skip over a bunch that haven’t fallen.
   - If the 4th domino has fallen, you know you went too far, so you then jump back a smaller distance, say 2 dominoes.
   - If that one hasn’t fallen, you keep moving forward but with smaller and smaller steps until you find the first fallen domino.

### 6. **Why It’s Efficient:**
   - This method allows you to cover large distances quickly when the answer is far away and then slow down to be precise when you're close to the answer.
   - It’s a bit like zooming out to get the big picture and then zooming in to see the details.

In summary, this is a clever twist on binary search that allows you to jump over large sections of data when you're far from the target and gradually make smaller jumps as you home in on the solution. This technique is especially handy in scenarios involving hierarchical structures like trees.

## Questions 

1. [[Find First and Last Position of Element in Sorted Array]]
2. 
## References
- [CPA algorithm](https://cp-algorithms.com/num_methods/binary_search.html)
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
