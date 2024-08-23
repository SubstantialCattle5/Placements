size,target = list(map(int,input().split()))
arr = list(map(int,input().split()))

arr.sort() 

for idx,number in enumerate(arr) : 
    new_target = target - number 
    if new_target < 0 : 
        continue 
    l,r = idx+1,len(arr)-1 

    while l < r :
        if l !=idx and r != idx and l!=r and arr[l] + arr[r] == new_target and arr[l] != arr[r] != number:
            print(idx+1,l+1,r+1)
            exit() 
        elif arr[l] + arr[r] > new_target : 
            r-=1 
        else :
            l+=1 
print("IMPOSSIBLE")

    
