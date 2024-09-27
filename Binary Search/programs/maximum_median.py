from typing import Callable

def check(x:int) -> bool :
    '''
    checks if x number of operations is sufficient
    '''
    mid = (len(array) - 1 )// 2
    ops = 0 
    for i in range(mid,len(array))  :
        ops += max(0,x-array[i])
    return ops <= number_of_ops 

def last_true(lo:int,hi:int,f:Callable[[int],bool]) -> int :
    lo -= 1
    while lo<hi : 
        mid = (lo+hi+1) // 2
        if f(mid) : 
            lo = mid 
        else : 
            hi = mid -1 
    return lo 
if __name__ == "__main__":
    size,number_of_ops = (int(num) for num in input().split()) 
    array = sorted([int(num) for num in input().split()])
    print(last_true(1,int(2e9),check))
