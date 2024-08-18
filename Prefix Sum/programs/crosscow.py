number_of_crossroads, working_subarray, broken_signal= [int(i) for i in input().split()] 
broken_signals_list = list() 

for i in range(broken_signal) :
    broken_signals_list.append(int(input()))

broken_signals_list.sort() 

min_fixes = float("inf")
k_ptr = 0 
l,r = 1,1
fixes = 0 
while l<=r :  
    if r in broken_signals_list : 
        fixes = fixes + 1 
    if r ==  working_subarray : 
        min_fixes = min(min_fixes,fixes)
        l = r 
        fixes = 0
    r+=1 
    

print(min_fixes)
