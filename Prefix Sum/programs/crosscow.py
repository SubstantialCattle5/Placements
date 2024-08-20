# Input processing
inputs = input().split()
number_of_lights, min_lights_to_work, broken_lights = [int(input) for input in inputs]

broken_lights_array = [0 for _ in range(number_of_lights)]
for _ in range(broken_lights):
    broken_light = int(input())
    broken_lights_array[broken_light - 1] = 1  # Mark the broken lights

# Initialize variables
min_number_of_fixed_lights = float("inf")
count = 0
lights_to_work = 0

# Sliding window to find the minimum number of repairs needed
for idx, light in enumerate(broken_lights_array):
    count += 1
    if light == 1:
        lights_to_work += 1
    if count == min_lights_to_work:
        min_number_of_fixed_lights = min(lights_to_work, min_number_of_fixed_lights)
        count -= 1
        if broken_lights_array[idx - min_lights_to_work + 1] == 1:
            lights_to_work -= 1

# Output the result
print(min_number_of_fixed_lights)
