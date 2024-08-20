def solve(arr) :
    n = len(arr)
    if n == 0 : 
        return 
    prefix,suffix = [0] * len(arr),[0] * len(arr) 
    # at element i prefix max element present
    for i in range(n) : 
        prefix[i],suffix[i] = arr[i] -  i , arr[i] + i

    for idx,num in enumerate(arr) : 
    # prefix - max element before this
        prefix[idx] = max(prefix[idx-1],prefix[idx])
    # suffix - max element after this 
    suffix[-1] = arr[-1]
    for idx in range(n-2,0,-1) : 
        suffix[idx]=max(suffix[idx+1],suffix[idx])
    # max(res,prefix[i]+arr[i]+prefix[j])
    
    res = 0 
    for idx in range(1,n-1) :
        res = max(res,prefix[idx-1]+arr[idx]+suffix[idx+1])

    print(res)


if __name__ == "__main__":
    solve([5 ,1, 4, 2, 3])
