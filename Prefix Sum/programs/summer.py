# Open the input and output files
with open('div7.in', 'r') as fin, open('div7.out', 'w') as fout:
    # Read the length of the input
    length_of_input = int(fin.readline().strip())
    
    # Initialize the list to store cow IDs
    cows = list()
    
    # Read all cow IDs
    for _ in range(length_of_input):
        cows.append(int(fin.readline().strip()))
    
    # Initialize the running sum modulo 7 and frequency array
    running_mod = 0
    freq_cows = [-1 for _ in range(7)]
    max_res = 0
    
    # Iterate over the list of cows
    for idx, cow in enumerate(cows):
        running_mod = (running_mod + cow) % 7
        if freq_cows[running_mod] == -1:
            freq_cows[running_mod] = idx
        else:
            max_res = max(max_res, idx - freq_cows[running_mod])
    
    # Write the result to the output file
    fout.write(f"{max_res}\n")
