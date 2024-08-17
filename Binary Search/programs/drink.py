# Input
n = int(input())  # Number of shops
prices = list(map(int, input().split()))  # Prices in each shop

q = int(input())  # Number of days
queries = []
for _ in range(q):
    queries.append(int(input()))  # Amount of money Vasiliy can spend on each day

# Sort prices for binary search
prices.sort()

# Function to implement binary search
def count_shops(prices, money):
    left, right = 0, len(prices) - 1
    while left <= right:
        mid = (left + right) // 2
        if prices[mid] <= money:
            left = mid + 1
        else:
            right = mid - 1
    return left

# Process each query
for money in queries:
    answer = count_shops(prices, money)
    print(answer)
