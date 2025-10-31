with open('path/to/your/file.txt', 'mode') as file_variable:
    # Code to work with the file goes here
    # Use file_variable to read or write
    # e.g., content = file_variable.read()
    pass # Replace pass with your file operations

# Execution continues here after the 'with' block
# The file is automatically closed by this point

# Assume 'example.txt' contains the line: "Hello from the file!"

try:
    with open('example.txt', 'r') as f:
        content = f.read()
        print("File content read successfully:")
        print(content)
    # File is now closed automatically
    print("File has been closed.")

except FileNotFoundError:
    print("Error: The file 'example.txt' was not found.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
    # File is still closed automatically if it was opened before the error

# Writing to a file

lines_to_write = ["First line.\n", "Second line.\n", "Third line.\n"]

try:
    with open('output.txt', 'w') as outfile:
        outfile.writelines(lines_to_write)
        print("Data written to output.txt successfully.")
    # File is now closed automatically

    # Let's verify by reading it back (using 'with' again!)
    with open('output.txt', 'r') as infile:
        print("\nVerifying file content:")
        print(infile.read())

except IOError as e:
    print(f"An error occurred during file writing or reading: {e}")
except Exception as e:
    print(f"An unexpected error occurred: {e}")

