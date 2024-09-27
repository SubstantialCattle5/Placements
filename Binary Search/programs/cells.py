from typing import Callable 
# if city - cell = -ve
def check(city,cell) : 
    if city - cell < 0 : 
        return False
    return True

def binary_search(i:int,check:Callable) -> int : 
    city = cities[i]
    lo,hi=0,cell_size - 1
    while lo<=hi : 
        mid = lo + (hi-lo) // 2
        if check(city,cells[mid]):  
            lo = mid 
        else : 
            hi = mid - 1 
        distance_lo = abs(city-cells[lo]) if lo < cell_size else float('inf')
        distance_hi = abs(city-cells[hi]) if hi >= 0 else float('inf')
    return min(distance_hi,distance_lo)

if __name__ == "__main__":
    city_size,cell_size = (int(num) for num in input().split())
    cities = [int(num) for num in input().split()]
    cells = [int(num) for num in input().split()]
    r = 0 
    for i in range(0,city_size) : 
        r = max(r,binary_search(i,check))
    print(r)
