"""
Tuples are immutable, cannot be changed after creation
"""

# An empty tuple
empty_tuple = ()
print(empty_tuple)

# A tuple with integers
coordinates = (10, 20)
print(coordinates)

# A tuple with mixed data types
person_info = ("Alice", 30, "New York")
print(person_info)

# Parentheses are sometimes optional if the context is clear
another_tuple = 100, 200, 300
print(another_tuple)
print(type(another_tuple)) # Output: <class 'tuple'>

# This is NOT a tuple, it's just the integer 5
not_a_tuple = (5)
print(type(not_a_tuple)) # Output: <class 'int'>

# This IS a single-item tuple
single_item_tuple = (5,)
print(type(single_item_tuple)) # Output: <class 'tuple'>
print(single_item_tuple)

rgb_color = (255, 165, 0) # Orange color

# Access the first element (index 0)
red_value = rgb_color[0]
print(f"Red: {red_value}") # Output: Red: 255

# Access the third element (index 2)
blue_value = rgb_color[2]
print(f"Blue: {blue_value}") # Output: Blue: 0

weekdays = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")

# Get elements from index 1 up to (but not including) index 4
mid_week = weekdays[1:4]
print(mid_week) # Output: ('Tue', 'Wed', 'Thu')

# Get the last two elements
weekend = weekdays[-2:]
print(weekend) # Output: ('Sat', 'Sun')

# Using a tuple as a dictionary key
location_temps = {
    (40.7128, -74.0060): 22,  # New York City coordinates -> temperature
    (34.0522, -118.2437): 28, # Los Angeles coordinates -> temperature
}

print(location_temps[(40.7128, -74.0060)]) # Output: 22

# Trying to use a list as a key would cause a TypeError
# location_temps[[34.0522, -118.2437]] = 28 # Error!

numbers = (1, 2, 5, 2, 8, 2, 10)

# Count occurrences of the number 2
count_of_2 = numbers.count(2)
print(f"The number 2 appears {count_of_2} times.") # Output: The number 2 appears 3 times.

# Find the index of the first occurrence of 8
index_of_8 = numbers.index(8)
print(f"The number 8 first appears at index {index_of_8}.") # Output: The number 8 first appears at index 4.

# Trying to find a value not in the tuple raises an error
# index_of_99 = numbers.index(99) # Uncommenting this line leads to

packed_data = "Max", 25, "Berlin" # Values are packed into a tuple
print(packed_data)      # Output: ('Max', 25, 'Berlin')
print(type(packed_data)) # Output: <class 'tuple'>

point = (15, 40)

# Unpack the tuple into variables x and y
x, y = point

print(f"x coordinate: {x}") # Output: x coordinate: 15
print(f"y coordinate: {y}") # Output: y coordinate: 40

# This is useful for swapping variables too!
a = 10
b = 20
a, b = b, a # Pack (b, a) into a tuple, then unpack into a, b
print(f"a: {a}, b: {b}") # Output: a: 20, b: 10

