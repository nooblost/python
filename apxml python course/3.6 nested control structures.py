is_student = True
has_valid_id = False
age = 20

print("Checking discount eligibility...")

if age < 25: # Outer condition: Age check
    print("Age requirement met.")
    if is_student: # Inner condition 1: Student status
        print("Student status confirmed.")
        if has_valid_id: # Inner condition 2: ID check
            print("Valid ID confirmed.")
            print("Congratulations! You are eligible for the discount.")
        else: # Inner else (belongs to ID check)
            print("Valid ID not found. Discount not applicable.")
    else: # Inner else (belongs to student status check)
        print("Not a student. Discount not applicable.")
else: # Outer else (belongs to age check)
    print("Age requirement not met. Discount not applicable.")

print("Eligibility check complete.\n")

# Nested for loops
print("Generating grid coordinates:")

# Outer loop iterates through x values
for x in range(3): # x will be 0, 1, 2
    # Inner loop iterates through y values for EACH x
    for y in range(2): # y will be 0, 1
        print(f"  ({x}, {y})") # Print the coordinate pair

print("Coordinate generation finished.\n")

# Nested while loops
outer_count = 0
print("Outer loop starting...")
while outer_count < 2:
    print(f"Outer loop iteration {outer_count}")
    inner_count = 0
    # Inner loop runs while inner_count < 3
    while inner_count < 3:
        print(f"  Inner loop iteration {inner_count}")
        inner_count += 1 # Important: update inner loop variable
    outer_count += 1 # Important: update outer loop variable
print("Outer loop finished.\n")

# Combining loops and conditionals
numbers = [11, 22, 37, 44, 58, 61, 76]
print("Even numbers found:")

for num in numbers:
    # Check the condition for each number in the list
    if num % 2 == 0: # Is the number divisible by 2?
        print(f"  {num}")

print("Search complete.\n")

data = ["apple", "banana", "cherry"]
# data = [] # Try uncommenting this line to see the difference

if data: # Checks if the list is not empty (non-empty lists are True-like)
    print("Processing data items:")
    for item in data:
        print(f"  - {item}")
else:
    print("No data items to process.\n")

    # Correct Indentation
    for i in range(2):
        print(f"Outer {i}")
        if i == 0:
            print("  Inner check for i=0")  # Indented under if
        for j in range(2):
            print(f"    Inner loop {j}")  # Indented under inner for

    # Incorrect Indentation (will likely cause errors or wrong logic)
    # for i in range(2):
    # print(f"Outer {i}") # Error: Expected an indented block
    # if i == 0:
    # print("  Inner check for i=0")
    # for j in range(2):
    # print(f"    Inner loop {j}") # Error or wrong scope