# Read mode 'r'

# Open data.txt for reading (explicitly)
try:
    with open('data.txt', 'r') as f:
        content = f.read()
        print("File content:", content)
except FileNotFoundError:
    print("Error: data.txt not found.")

# Write mode 'w'

# Open output.txt for writing. Creates it or erases existing content.
with open('output.txt', 'w') as f:
    f.write("This is the first line.\n")
    f.write("This overwrites anything previously in the file.")

# Append mode 'a'

# Open log.txt for appending. Creates it if it doesn't exist.
with open('log.txt', 'a') as f:
    f.write("New log entry added.\n")

# Exclusive creation 'x': creates new file, if file exists, FileExistError.
# Prevents accidentally overwriting existing file

# Try to create a new config file; fail if it exists.
try:
    with open('config_new.ini', 'x') as f:
        f.write("[Settings]\n")
        f.write("Mode=Test\n")
        print("config_new.ini created successfully.")
except FileExistsError:
    print("Error: config_new.ini already exists. Cannot overwrite.")

# Mode modifiers

# Text mode 't': This is the default modifier if none is specified.

# In text mode, Python handles encoding (converting strings to bytes when writing, and bytes to strings when reading) and
# automatically translates platform-specific line endings (like \n on Linux/macOS and \r\n on Windows) to Python's standard \n.
# So, 'r' is the same as 'rt', and 'w' is the same as 'wt'.

# Binary mode 'b': file should be handled as bytes.
# Use with non-text files like audio, video, executables etc.