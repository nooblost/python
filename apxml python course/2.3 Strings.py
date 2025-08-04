# 2.3 Texts (strings)

# Using single quotes
message_single = 'Hello, Python learner!'
print(message_single)

# Using double quotes
message_double = "This also works just fine."
print(message_double)

# What if your string contains a single quote? Use double quotes to enclose it.
quote = "He said, 'Python is fun!'"
print(quote)

# What if your string contains a double quote? Use single quotes.
reply = 'She responded, "Indeed it is."'
print(reply)

# Triple double quotes for multi-line string
multi_line_doc = """This is the first line.
This is the second line.
And "quotes" or 'apostrophes' can be used freely inside."""
print(multi_line_doc)

# Triple single quotes work the same way
multi_line_alt = '''Another way to write
multi-line text,
very convenient.'''
print(multi_line_alt)

# Triple double quotes for multi-line string
multi_line_doc = """This is the first line.
This is the second line.
And "quotes" or 'apostrophes' can be used freely inside."""
print(multi_line_doc)

# Triple single quotes work the same way
multi_line_alt = '''Another way to write
multi-line text,
very convenient.'''
print(multi_line_alt)

# Basic String Operations
first_name = "Ada"
last_name = "Lovelace"
space = " "

# Concatenation
full_name = first_name + space + last_name
print(full_name) # Output: Ada Lovelace

# Repetition
separator = "-" * 10 # Repeat the hyphen 10 times
print(separator)   # Output: ----------
print(first_name * 3) # Output: AdaAdaAda

# Indexing
language = "Python"

# Accessing characters by positive index
print(language[0]) # Output: P (the first character)
print(language[1]) # Output: y (the second character)
print(language[5]) # Output: n (the sixth character)

# Accessing characters using negative index (starts from the end)
print(language[-1]) # Output: n (the last character)
print(language[-2]) # Output: o (the second-to-last character)

# Slicing
language = "Python"

# Get characters from index 1 up to (but not including) index 4
print(language[1:4]) # Output: yth

# Get characters from the beginning up to index 3 (exclusive)
print(language[:3])  # Output: Pyt

# Get characters from index 2 to the end
print(language[2:])  # Output: thon

# Get the whole string (less common, but shows the defaults)
print(language[:])   # Output: Python

# Get every second character
print(language[::2]) # Output: Pto

# Get the string in reverse
print(language[::-1]) # Output: nohtyP

# String Immutability
greeting = "hello"
# greeting[0] = "H" # This will cause a TypeError: 'str' object does not support item assignment

# To "change" the greeting, create a new string
new_greeting = "H" + greeting[1:]
print(new_greeting) # Output: Hello
print(greeting)     # Output: hello (original string is unchanged)

# String methods
text = "  Learning Python is Fun!  "

# Length
print(len(text)) # Output: 27

# Case conversion
print(text.lower()) # Output:   learning python is fun!
print(text.upper()) # Output:   LEARNING PYTHON IS FUN!

# Stripping whitespace
print(text.strip())  # Output: Learning Python is Fun!
print(text.lstrip()) # Output: Learning Python is Fun!
print(text.rstrip()) # Output:   Learning Python is Fun!

# Finding substrings
print(text.find("Python")) # Output: 11 (index where 'Python' starts)
print(text.find("Java"))   # Output: -1 (not found)

# Replacing substrings
print(text.replace("Fun", "Awesome")) # Output:   Learning Python is Awesome!

# Checking start/end (use strip first for accuracy here)
clean_text = text.strip()
print(clean_text.startswith("Learning")) # Output: True
print(clean_text.endswith("!"))        # Output: True

# Splitting a string into a list
words = clean_text.split(" ")
print(words) # Output: ['Learning', 'Python', 'is', 'Fun!']

# Joining a list into a string
joined_string = "---".join(words)
print(joined_string) # Output: Learning---Python---is---Fun!

# Original string remains unchanged due to immutability
print(text) # Output:   Learning Python is Fun!

# Formatted Strings
name = "Alice"
age = 30
city = "New York"

# Using f-string for clean formatting
intro_fstring = f"My name is {name}, I am {age} years old, and I live in {city}."
print(intro_fstring)
# Output: My name is Alice, I am 30 years old, and I live in New York.

# You can also include expressions inside the braces
radius = 5
area = 3.14159 * radius**2
print(f"A circle with radius {radius} has an area of {area:.2f}.")
# Output: A circle with radius 5 has an area of 31.42.
# Note: :.2f formats the float to 2 decimal places.

# Newline
print("First line.\nSecond line.")
# Output:
# First line.
# Second line.

# Tab
print("Column1\tColumn2")
# Output: Column1    Column2

# Literal backslash
print("This is a path: C:\\Users\\Name")
# Output: This is a path: C:\Users\Name

# Literal quotes within string defined by same quotes
print('He said, \'Hello!\'') # Output: He said, 'Hello!'
print("She replied, \"Hi!\"") # Output: She replied, "Hi!"