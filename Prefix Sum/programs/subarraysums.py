a = input().split()
n, target = [int(i) for i in a]
arr_str = input().split()
arr = [int(num) for num in arr_str]

prefix = [0] * n
prefix[0] = arr[0]

for idx in range(1, n):
    prefix[idx] = arr[idx] + prefix[idx - 1]

freq = {0: 1}  # We start with prefix sum 0 having one occurrence (to handle subarrays starting from index 0)
count = 0

for p in prefix:
    # Check if (p - target) exists in the frequency map
    if (p - target) in freq:
        count += freq[p - target]

    # Update the frequency map with the current prefix sum
    if p in freq:
        freq[p] += 1
    else:
        freq[p] = 1

print(count)
