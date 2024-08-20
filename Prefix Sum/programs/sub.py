def solve(arr): 
    n = len(arr)
    
    prefix,suffix = [0] * len(arr), [0] * len(arr)

    for i in range(0,n): 
        prefix[i] = i + arr[i] 
    for i in range(0,n) :
        suffix[i]= arr[i] - i 

    for i in range(1,n) : 
        prefix[i] = max(prefix[i-1],prefix[i])
    for j in range(n-2,-1,-1):
        suffix[j] = max(suffix[j+1], suffix[j] )
    res = 0 
    for idx in range(1,n-1) : 
        res = max(res,arr[idx] + prefix[idx-1] + suffix[idx+1])
    print(res)
if __name__ == "__main__":
    solve([5,1,4,2,3])
