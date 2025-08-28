numbers = [1, 5, 12, 8, 9, 21, 5, 3]
target = 9
found_at_index = -1 # Initialize with a value indicating not found

print(f"Searching for {target} in {numbers}...")

for index, num in enumerate(numbers):
    print(f"Checking index {index}: value {num}")
    if num == target:
        found_at_index = index
        print(f"Found {target}!")
        break # Exit the loop immediately

# Code here runs after the loop finishes or breaks
if found_at_index != -1:
    print(f"Target {target} first found at index {found_at_index}.")
else:
    print(f"Target {target} not found in the list.")

print("Search complete.")

data = [10, -5, 20, 0, -15, 30, 5]
positive_sum = 0

print(f"Processing data: {data}")

for num in data:
    print(f"Current number: {num}")
    if num <= 0:
        print("  Skipping non-positive number.")
        continue # Skip the rest of this iteration
    # This code only runs if continue was NOT executed
    print(f"  Adding {num} to sum.")
    positive_sum += num

print(f"\nSum of positive numbers: {positive_sum}")

for i in range(1, 4): # Outer loop
    print(f"Outer loop iteration {i}:")
    for j in ['a', 'b', 'c', 'STOP', 'd']: # Inner loop
        if j == 'STOP':
            print("  Inner loop breaking!")
            break # Breaks only the inner loop
        if j == 'b':
            print(f"  Skipping '{j}' in inner loop...")
            continue # Continues to next item in inner loop
        print(f"  Processing inner item: {j}")
    # This line is reached after the inner loop completes or breaks
    print(f"Outer loop iteration {i} finished.")
print("All loops complete.")