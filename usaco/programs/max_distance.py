a = input()
x = [int(num) for num in input().split()] 
y = [int(num) for num in input().split()]

print(zip(x,y).values())
