---
tags:
  - Recursion
  - DSA
---
<iframe width="560" height="315" src="https://www.youtube.com/embed/ngCos392W4w?si=EDuNH4a8vMvhn0x2" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen></iframe>

# Steps to follow when solving a recursive problem 
Try answering the following questions 

1. What's the simplest possible input? - also can be defined as the base case 
2. Play around with the examples and try to visualize a pattern 
3. Relate the hard cases to simpler cases 
4. Generalize the Pattern 
5. Write the code by combining the recursive pattern with the base case. 


## Example 1 

Write a recursive function that given an input n sums all non negative integers up to n.

1. What's the simplest possible input ?
	$$
	\begin{aligned}
	\text{sum}(n=0) & = 0 \\
	\end{aligned}
	$$
1. play around the examples 
$$
\begin{aligned}
\text{sum}(n=0) & = 0 \\
\text{sum}(n=1) & = 1  \\ 
\text{sum}(n=2) &= 3 \\
\end{aligned}
$$
3. Relate with harder case and generalize the pattern
$$
\begin{aligned}
\text{sum}(n) &= n + sum(n-1)
\end{aligned}
$$

4. Code with base case and recursive pattern.
```python
def fn(a) : 
	# base case 
	if a == 0 :
		return 0 
	return a + fn(a-1) # pattern
```
## Example 2 

Write a function that takes two inputs `n` and `m` and outputs the number of unique paths from the top left corner to the bottom right corner of a `n x m` grid. 
_constraints_ : you can only move one down or right 1 unit at a time.

1. What's the simplest possible input? if n = 1 or m = 1
$$
gridpath(n,m)  =  1
$$
2. Play around with examples 
![[Pasted image 20240813121259.png]]
4. Relate the hard cases with similar ones 
![[Pasted image 20240813121358.png]]
5. Generalize the pattern 
$$
\begin{aligned}
gridpath(n,m) = gridpath(n,m-1) + gridpath(n-1,m) \\ 
\end{aligned}
$$
6. Code with it.
```python 
def fn(a,b) : 
	if n==0 or m==0 :
		return 0
	return fn(n-1,m) + fn(n,m-1)
```



## Example 3 

Write a function that counts the number of ways you can partition n objects using parts up to m assuming m>=0. 

1. What's the simplest possible input? - also can be defined as the base case 
$$
\begin{aligned}
fn(0,0) &= 1 \\
fn(0,1) &= 
\end{aligned}
$$
1. Play around with the examples and try to visualize a pattern 
2. Relate the hard cases to simpler cases 
3. Generalize the Pattern 
4. Write the code by combining the recursive pattern with the base case. 
