
def solution(length,free_mins,books) : 
    window_sum = 0
    number_of_books = 0 
    l,r = 0,0 
    while r < length : 
        if books[r] <= free_mins-window_sum : 
            
            number_of_books = max(number_of_books,r-l+1)            
            window_sum += books[r]
            r+=1
        else :   
            window_sum-=books[l]
            l+=1 
    
    
    print(number_of_books)

# [3] number_of_books = 1  
#  [3,1] number_of_books = 2 
# [3,1,2]

if __name__ == "__main__":
    length,free_mins = list(map(int,input().split()))
    books = list(map(int,input().split()))

    solution(length,free_mins,books)

