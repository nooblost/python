# Assume we have a file named 'greet.txt' with the following content:
# Hello, Python learner!
# Start file handling.
# Enjoy reading files.

# Example: Reading the entire content of greet.txt
try:
    with open('greet.txt', 'r') as file:
        content = file.read()
        print("--- File Content (using read()) ---")
        print(content)
        print("--- End of Content ---")
except FileNotFoundError:
    print("Error: greet.txt not found.")

# Example: Reading only the first 10 bytes
try:
    with open('greet.txt', 'r') as file:
        partial_content = file.read(10)
        print("--- First 10 Bytes ---")
        print(partial_content)
        print("--- End of Partial Content ---")
except FileNotFoundError:
    print("Error: greet.txt not found.")

# Example: Reading lines one by one with readline()
try:
    with open('greet.txt', 'r') as file:
        print("--- Reading lines with readline() ---")
        line1 = file.readline()
        print(f"Line 1: {line1}", end='') # end='' prevents extra newline

        line2 = file.readline()
        print(f"Line 2: {line2}", end='')

        line3 = file.readline()
        print(f"Line 3: {line3}", end='')

        # Calling it again after the last line
        end_of_file = file.readline()
        print(f"End of file check: '{end_of_file}' (Empty string indicates EOF)")
        print("--- Done reading lines ---")
except FileNotFoundError:
    print("Error: greet.txt not found.")

    # Example: Reading all lines into a list
    try:
        with open('greet.txt', 'r') as file:
            lines_list = file.readlines()
            print("--- Reading lines with readlines() ---")
            print(f"Type of result: {type(lines_list)}")
            print(f"Number of lines: {len(lines_list)}")
            print("Content of list:")
            print(lines_list)

            # Example of accessing individual lines
            if len(lines_list) > 0:
                print(f"First line from list: {lines_list[0]}", end='')
            print("--- Done reading lines ---")

    except FileNotFoundError:
        print("Error: greet.txt not found.")

# Recommended approach: Iterating directly over the file object
try:
    with open('greet.txt', 'r') as file:
        print("--- Iterating directly over the file object ---")
        line_number = 1
        for line in file:
            # Process each line here
            # Often useful to strip whitespace/newlines
            processed_line = line.strip()
            print(f"Line {line_number}: '{processed_line}'")
            line_number += 1
        print("--- Done iterating ---")
except FileNotFoundError:
    print("Error: greet.txt not found.")