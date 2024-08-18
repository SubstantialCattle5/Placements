from collections import defaultdict

for _ in range(int(input())) : 
    length_of_array = int(input())
    arr = [int(i) for i in input()]
    
    preFixSum = [0] * (len(arr) +1)
    for idx,element in enumerate(arr) : 
        preFixSum[idx+1] = preFixSum[idx] + element

    #-> 3 - 1 + 1 = 3 
    #-> iff : r-l+1 = sum(arr[l...r]) = preFixSum[r] - preFixSum[l-1]
    # -> preFixSum[l-1] - l +1 = preFixSum[r] - r
    freq = defaultdict(int) # -> [preFixSum[l] - l  ] : freq 

    # freq loop 
    for idx,pre in enumerate(preFixSum): 
        freq[preFixSum[idx] - idx] += 1 

    # good subarrays 
    subarrays = 0
    for f in freq.values() : 
        subarrays += f*(f-1)//2 
    print(subarrays)
    
    
