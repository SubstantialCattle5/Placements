# Reading input
with open('hps.in', 'r') as file:
    length_of_inputs = int(file.readline().strip())
    moves = [file.readline().strip() for _ in range(length_of_inputs)]

# Arrays to store prefix and suffix wins for each move type
prefix_p = [0] * length_of_inputs
prefix_h = [0] * length_of_inputs
prefix_s = [0] * length_of_inputs

suffix_p = [0] * length_of_inputs
suffix_h = [0] * length_of_inputs
suffix_s = [0] * length_of_inputs

# Calculate prefix arrays
for i in range(length_of_inputs):
    prefix_p[i] = (prefix_p[i-1] if i > 0 else 0) + (1 if moves[i] == 'P' else 0)
    prefix_h[i] = (prefix_h[i-1] if i > 0 else 0) + (1 if moves[i] == 'H' else 0)
    prefix_s[i] = (prefix_s[i-1] if i > 0 else 0) + (1 if moves[i] == 'S' else 0)

# Calculate suffix arrays
for i in range(length_of_inputs-1, -1, -1):
    suffix_p[i] = (suffix_p[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'P' else 0)
    suffix_h[i] = (suffix_h[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'H' else 0)
    suffix_s[i] = (suffix_s[i+1] if i < length_of_inputs-1 else 0) + (1 if moves[i] == 'S' else 0)

# Maximize the number of wins by choosing the best split point
max_wins = 0

for i in range(length_of_inputs - 1):
    # Try all combinations of gestures before and after the switch
    max_wins = max(max_wins, prefix_p[i] + max(suffix_h[i+1], suffix_s[i+1]))
    max_wins = max(max_wins, prefix_h[i] + max(suffix_p[i+1], suffix_s[i+1]))
    max_wins = max(max_wins, prefix_s[i] + max(suffix_p[i+1], suffix_h[i+1]))

# Consider cases with no switch (full sequence with a single gesture)
max_wins = max(max_wins, prefix_p[-1], prefix_h[-1], prefix_s[-1])

# Output the result
with open('hps.out', 'w') as file:
    file.write(str(max_wins) + '\n')
