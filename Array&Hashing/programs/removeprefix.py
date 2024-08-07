from collections import defaultdict, deque

if __name__ == "__main__":
    number_of_questions = int(input())
    for _ in range(number_of_questions):
        length = int(input())
        arr = list(map(int, input().split()))
        
        freq = defaultdict(int)
        count = 0
        window = deque()
        
        for num in arr:
            # Add to the window and update the frequency map
            window.append(num)
            freq[num] += 1
            
            # While there are duplicates in the window, adjust the window
            while freq[num] > 1:
                removed = window.popleft()
                freq[removed] -= 1
                if freq[removed] == 0:
                    del freq[removed]
                count += 1
        
        print(count)
