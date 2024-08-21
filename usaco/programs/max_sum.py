def solution(length,arr) : 
    prefixSum = [0 for _ in range(length)]
    summer = 0 
    for idx in range(length) : 
        summer = arr[idx]+summer
        prefixSum[idx] = summer 
    max_sum = float("-inf")
    for jdx in range(length) : 
        summer = prefixSum[idx] - min(prefixSum[idx:-1] if idx != length -1 else [0])
        summer=max(max_sum,summer)
    print(summer)
if __name__ == "__main__":
    #length = int(input())
    #arr = list(ap(int,input().split()))
    length = 8 
    arr = [-1,3,-2,5,3,-5,2,2]
    solution(length,arr)
