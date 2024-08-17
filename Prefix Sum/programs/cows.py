# Open input and output files
with open('bcount.in', 'r') as fin:
    with open('bcount.out', 'w') as fout:
        # Read input values for the number of cows and number of queries
        number_of_cows, number_of_queries = map(int, fin.readline().split())

        # Initialize prefix sum arrays for each breed
        prefix_holsteins = [0] * (number_of_cows + 1)
        prefix_guernseys = [0] * (number_of_cows + 1)
        prefix_jerseys = [0] * (number_of_cows + 1)

        # Fill the prefix sum arrays
        for i in range(1, number_of_cows + 1):
            cow = int(fin.readline().strip())
            prefix_holsteins[i] = prefix_holsteins[i - 1] + (1 if cow == 1 else 0)
            prefix_guernseys[i] = prefix_guernseys[i - 1] + (1 if cow == 2 else 0)
            prefix_jerseys[i] = prefix_jerseys[i - 1] + (1 if cow == 3 else 0)

        # Process each query
        for _ in range(number_of_queries):
            query_i, query_j = map(int, fin.readline().split())
            
            # Calculate the number of cows of each breed in the range [query_i, query_j]
            holsteins_count = prefix_holsteins[query_j] - prefix_holsteins[query_i - 1]
            guernseys_count = prefix_guernseys[query_j] - prefix_guernseys[query_i - 1]
            jerseys_count = prefix_jerseys[query_j] - prefix_jerseys[query_i - 1]
            
            # Write the result for this query to the output file
            fout.write(f"{holsteins_count} {guernseys_count} {jerseys_count}\n")
