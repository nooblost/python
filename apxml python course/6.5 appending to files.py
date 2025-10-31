# log.txt already exists and contains "Event: System Start\n"

# Open log.txt in append mode ('a')
with open('log.txt', 'a') as f:
    # Write a new line to the end of the file
    # Note: We add '\n' to ensure the new entry starts on a new line
    f.write("Event: User Login\n")
    f.write("Event: Data Processed\n")

# The 'with' block automatically closes the file

# Let's verify the content
with open('log.txt', 'r') as f:
    content = f.read()
    print(content)

