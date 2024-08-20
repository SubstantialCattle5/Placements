def min_operations(length,arr) : 
    if len(set(arr)) == 1 or length == 1 : 
        print(1)
        return
    operations = 0
    print(7%7)
    for idx in range(length-1) :
    # compare next elements 
        print(idx)
        if arr[idx] <= arr[idx%length+1] : 
            operations +=1 
            arr.pop(idx%length+1)

    operations = operations if len(set(arr)) == 1 else len(arr) -1 
    print(operations)
    # delete them if ai < a[imodm] + 1 



if __name__ == "__main__":
    #tests = int(input())
    tests = 7 
    test_cases = [
    (1, [1]),
    (3, [1, 2, 3]),
    (3, [1, 2, 2]),
    (5, [5, 4, 3, 2, 1]),
    (6, [1, 1, 2, 2, 3, 3]),
    (8, [8, 7, 6, 3, 8, 7, 6, 3]),
    (6, [1, 1, 4, 5, 1, 4])
]
    for i in range(tests) : 
        #length = int(input()) 
        #arr = list(map(int,input()))
        min_operations(test_cases[i][0],test_cases[i][1])
