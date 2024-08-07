n = input()
for _ in range(int(n)) : 
    num = int(input())
    ans = ""
    running_sum = 0 
    for n in range(9,0,-1): 
        if running_sum + n  <= num : 
            running_sum+=n 
            ans+=str(n) 
        if running_sum == num : 
            break 
    print(ans[::-1])

        # 9 
        # 9 8 -> 17 
        # 9 8  ->  



    
