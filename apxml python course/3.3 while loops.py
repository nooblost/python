# Initialize a counter variable BEFORE the loop
count = 1

    # The loop continues as long as 'count' is less than 5
while count < 5:
    print(f"Current count is: {count}")
    # IMPORTANT: Update the counter inside the loop!
    count = count + 1  # Or use the shorthand: count += 1

print("Loop finished!")

# Initialize response to something that ensures the loop runs at least once
response = ""

# Keep asking until the user types 'quit'
while response.lower() != 'quit':
    response = input("Enter some text (or type 'quit' to exit): ")
    print(f"You entered: {response}")

print("Okay, quitting now. Goodbye!")