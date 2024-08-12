---
tags:
  - scam
  - Algorithm
---
## Description
Binary exponentiation, also known as exponentiation by squaring, is a technique used to quickly calculate powers with a time complexity of \(O(\log n)\). This method is particularly useful for operations requiring **associativity**, such as modular arithmetic.

## Basic Idea

Every integer can be represented in binary form, which is a base-2 representation using only 0s and 1s. For example:

- The number 13 in binary is $(1101_2)$.

The exponent \(n\) can be expressed as a sum of powers of 2:

$$
n = 2^3 + 2^2 + 2^0 = 8 + 4 + 1 = 13
$$

### How Binary Exponentiation Works

To calculate \(a^n\) using binary exponentiation, follow these steps:

1. **Write the exponent \(n\) in binary**:
    - \(13 = $1101_2$\), so \(13 = 2^3 + 2^2 + 2^0\).
2. **Compute the powers of \(a\)** that correspond to the set bits (1s) in the binary representation of \(n\):
    - \(a^1\) for the \(2^0\) position,
    - \(a^4\) for the \(2^2\) position,
    - \(a^8\) for the \(2^3\) position.
3. **Multiply these powers together** to get the final result: 
    $$
    a^{13} = a^8 \cdot a^4 \cdot a^1
    $$
4. **Optimize using squaring**:
    - To compute \(a^8\), start with \(a^1 = a\).
    - Square it to get \(a^2\).
    - Square \(a^2\) to get \(a^4\).
    - Square \(a^4\) to get \(a^8\).

### Example: Calculating \(3^{13}\)

1. **Binary Representation**:
    - \(13 = 1101_2\).
2. **Calculate Powers**:
    - \(3^1 = 3\)
    - \(3^2 = 9\)
    - \(3^4 = 81\)
    - \(3^8 = 6561\)
3. **Multiply the Relevant Powers**:
    - Since \(13 = 1101_2\), we multiply \(3^8\), \(3^4\), and \(3^1\):
    $$
    3^{13} = 6561 \times 81 \times 3 = 1594323
    $$

### Problem Description
This algorithm efficiently solves the problem of calculating large powers by reducing the number of necessary multiplications, making it suitable for problems involving large exponents, especially in fields like cryptography and computational mathematics.

## Pseudocode
Here is the pseudocode for binary exponentiation:

```
function binpow(a, b):
    res = 1
    while b > 0:
        if b & 1:
            res = res * a
        a = a * a
        b = b >> 1
    return res
```

## Implementation

#### Iterative 
```python
def binpow(a, b):
    res = 1
    while b > 0: 
        if b & 1: # does bitwise check for 1 so if 1011 & 0001 
            res *= a # if true meaning odd multiply response with a 
        a *= a # increase the power of a so a^n 
        b >>= 1 # shift operation
    return res
```


#### Recursively 
```python 
def binpow(a,b) : 
	if b == 0 : 
		return 1
	res = binpow(a,b/2)
	if b%2 == 0 : 
		return res * res * a 
	else : 
		return res * res 
```
## Complexity Analysis

### Time Complexity
- **Time Complexity:** \(O(\log b)\), because the algorithm reduces the exponent by half in each iteration, resulting in logarithmic time complexity.

### Space Complexity
- **Space Complexity:** \(O(1)\), as the algorithm only uses a constant amount of additional space.

## Applications

### Effective computation of large exponents modulo a number

**Problem:** Compute   $x^n mod (m)$  . This is a very common operation. For instance it is used in computing the [modular multiplicative inverse](https://cp-algorithms.com/algebra/module-inverse.html).

**Soln** : Since $mod(m)$ is associative in nature, it doesn't interfere with multiplications. 
$(a*b)mod(m)=a*mod(m)*b*mod(m)$

```python
def binpow(a,b):
	if b == 0 : 
		return 1 
	res = binpow(a,b/2)
	if res%2 != 0 :
		res = res * res * a  % mod 
	elif : 
		res*=res % mod 
```


## Effective computation of Fibonacci Sequence 
**Problem**: Compute $n^{\text{th}}$ fibonacci number $F_n$ 

**Solution:** To compute the next Fibonacci number, only last two previous ones are needed 

## References
- [Binary Exponentiation - GeeksforGeeks](https://www.geeksforgeeks.org/binary-exponentiation/)
- [Exponentiation by Squaring - Wikipedia](https://en.wikipedia.org/wiki/Exponentiation_by_squaring)

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

---
