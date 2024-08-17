---
tags:
  - prefixsum
  - DSA
  - Algorithm
  - usaco
Date: 2024-08-17T15:13
Solved: false
Difficulty:
  - "1300"
---

Let's say we have a one-indexed integer array $\texttt{arr}$ of size $N$ and we
want to compute the value of

$$
\texttt{arr}[a]+\texttt{arr}[a+1]+\cdots+\texttt{arr}[b]
$$

for $Q$ different pairs $(a,b)$ satisfying $1\le a\le b\le N$. We'll use the
following example with $N = 6$:


| Index $i$         | 1   | 2   | 3   | 4   | 5   | 6   |
| ----------------- | --- | --- | --- | --- | --- | --- |
| $\texttt{arr}[i]$ | 1   | 6   | 4   | 2   | 5   | 3   |

Naively, for every query, we can iterate through all entries from index $a$to index $b$ to add them up. Since we have $Q$ queries and each query requires a maximum of $\mathcal{O}(N)$ operations to calculate the sum, our total time complexity is $\mathcal{O}(NQ)$. For most problems of this nature, the
constraints will be $N, Q \leq 10^5$, so $NQ$ is on the order of $10^{10}$. This
is **not** acceptable; it will almost certainly exceed the time limit.

Instead, we can use prefix sums to process these array sum queries. We designate a prefix sum array $\texttt{prefix}$. First, because we're 1-indexing the array,set $\texttt{prefix}[0]=0$, then for indices $k$ such that $1 \leq k \leq N$,
define the prefix sum array as follows:

$$
\texttt{prefix}[k]=\sum_{i=1}^{k} \texttt{arr}[i]
$$

Basically, what this means is that the element at index $k$ of the prefix sum array stores the sum of all the elements in the original array from index $1$ up to $k$. This can be calculated easily in $\mathcal{O}(N)$ by the following
formula for each $1\le k\le N$:

$$
\texttt{prefix}[k]=\texttt{prefix}[k-1]+\texttt{arr}[k]
$$


For the example case, our prefix sum array looks like this:



| Index $i$            | 0   | 1   | 2   | 3   | 4   | 5   | 6   |
| -------------------- | --- | --- | --- | --- | --- | --- | --- |
| $\texttt{prefix}[i]$ | 0   | 1   | 7   | 11  | 13  | 18  | 21  |



Now, when we want to query for the sum of the elements of $\texttt{arr}$ between
(1-indexed) indices $a$ and $b$ inclusive, we can use the following formula:

$$
\sum_{i=L}^{R} \texttt{arr}[i] = \sum_{i=1}^{R} \texttt{arr}[i] - \sum_{i=1}^{L-1} \texttt{arr}[i]
$$

Using our definition of the elements in the prefix sum array, we have

$$
\sum_{i=L}^{R} \texttt{arr}[i]= \texttt{prefix}[R]-\texttt{prefix}[L-1]
$$

Since we are only querying two elements in the prefix sum array, we can
calculate subarray sums in $\mathcal{O}(1)$ per query, which is much better than
the $\mathcal{O}(N)$ per query that we had before. Now, after an
$\mathcal{O}(N)$ preprocessing to calculate the prefix sum array, each of the
$Q$ queries takes $\mathcal{O}(1)$ time. Thus, our total time complexity is
$\mathcal{O}(N+Q)$, which should now pass the time limit.

Let's do an example query and find the subarray sum between indices $a = 2$ and
$b = 5$, inclusive, in the 1-indexed $\texttt{arr}$. From looking at the
original array, we see that this is

$$
\sum_{i=2}^{5} \texttt{arr}[i] = 6 + 4 + 2 + 5 = 17.
$$

<center>

<table>
	<thead>
		<tr>
			<th>Index i</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>arr_i</td>
			<td>1</td>
			<td className="bg-yellow-100 dark:bg-yellow-800">6</td>
			<td className="bg-yellow-100 dark:bg-yellow-800">4</td>
			<td className="bg-yellow-100 dark:bg-yellow-800">2</td>
			<td className="bg-yellow-100 dark:bg-yellow-800">5</td>
			<td>3</td>
		</tr>
	</tbody>
</table>

</center>

Using prefix sums:

$$
\texttt{prefix}[5] - \texttt{prefix}[1] = 18 - 1 = 17.
$$

<center>

<table>
	<thead>
		<tr>
			<th>Index i</th>
			<th>0</th>
			<th>1</th>
			<th>2</th>
			<th>3</th>
			<th>4</th>
			<th>5</th>
			<th>6</th>
		</tr>
	</thead>
	<tbody>
		<tr>
			<td>prefix_i</td>
			<td className="bg-red-100 dark:bg-red-800">0</td>
			<td className="bg-red-100 dark:bg-red-800">1</td>
			<td className="bg-green-100 dark:bg-green-800">7</td>
			<td className="bg-green-100 dark:bg-green-800">11</td>
			<td className="bg-green-100 dark:bg-green-800">13</td>
			<td className="bg-green-100 dark:bg-green-800">18</td>
			<td>21</td>
		</tr>
	</tbody>
</table>

</center>
