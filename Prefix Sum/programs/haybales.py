stacks,operations = list(map(int,input().split()))

diff = [0] * (stacks+1) 
for i in range(operations) : 
    left,right = list(map(int,input().split()))
    diff[left] += 1 
    diff[right+1] -= 1

sub_sum = 0 
for idx in range(len(diff)) :
    sub_sum = sub_sum + diff[idx]
    diff[idx] = sub_sum
diff.sort() 

print(diff[len(diff)//2])
    

