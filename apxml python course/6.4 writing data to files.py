# Open 'output.txt' in write mode
# If 'output.txt' exists, its contents will be erased!
# If it doesn't exist, it will be created.
file_object = open('output.txt', 'w')
# ... perform write operations ...
file_object.close() # Remember to close

# 'w' option erases all data if file already exists

# Preferred way: Using 'with'
with open('output.txt', 'w') as f:
    # 'f' is our file object, ready for writing
    pass # We'll add write operations here
# File is automatically closed when exiting the 'with' block

# Define the text we want to write
message = "Hello from Python!\n" # Note the newline character \n

try:
    # Open the file in write mode using 'with'
    with open('greeting.txt', 'w') as f:
        f.write(message) # Write the string to the file
    print("Successfully wrote to greeting.txt")

    # Optional: Verify by reading the file back
    with open('greeting.txt', 'r') as f:
        content = f.read()
        print("File content:")
        print(content)

except IOError as e:
    print(f"An error occurred: {e}")

# writing multiple lines

lines_to_write = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]

try:
    with open('multiple_lines.txt', 'w') as f:
        for line in lines_to_write:
            f.write(line) # Write each line including its newline
    print("Successfully wrote multiple lines.")
except IOError as e:
    print(f"An error occurred: {e}")

# Using writelines(): This method takes a list (or any iterable) of strings and writes each string to the file.
# Like write(), it does not add newline characters automatically; your strings must already contain them if needed.

lines_to_write = [
    "Report Header\n",
    "--------------\n",
    "Data point 1: Value A\n",
    "Data point 2: Value B\n"
]

try:
    with open('report.txt', 'w') as f:
        f.writelines(lines_to_write) # Write all strings from the list
    print("Successfully wrote report using writelines().")
except IOError as e:
    print(f"An error occurred: {e}")

# Writing non-string data
# write() requires strings, nothing else. 

item = "Widget"
quantity = 15
price = 29.95
total_cost = quantity * price

try:
    with open('order_summary.txt', 'w') as f:
        f.write("Order Summary\n")
        f.write("=============\n")
        f.write("Item: " + item + "\n")
        f.write("Quantity: " + str(quantity) + "\n") # Convert integer to string
        f.write("Price per item: $" + str(price) + "\n") # Convert float to string
        f.write("Total Cost: $" + str(total_cost) + "\n") # Convert float to string
    print("Successfully wrote order summary.")
except IOError as e:
    print(f"An error occurred: {e}")