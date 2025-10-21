def add_numbers(num1, num2):
    """Calculates the sum of two numbers."""
    total = num1 + num2
    return total

# Call the function and store the returned value
sum_result = add_numbers(5, 3)
print(f"The sum is: {sum_result}")

# You can also use the returned value directly in other expressions
another_result = add_numbers(10, 2) * 2
print(f"Another calculated result: {another_result}\n")

def create_greeting(name):
    """Creates a personalized greeting string."""
    return f"Hello, {name}! Greet."

def is_even(number):
    """Checks if a number is even."""
    if number % 2 == 0:
        return True
    else:
        return False # Could also just be 'return number % 2 == 0'

def get_first_three_evens():
    """Returns a list of the first three even numbers."""
    return [2, 4, 6]

# Using the functions
greeting = create_greeting("Alice")
print(greeting)

check_num = 10
if is_even(check_num):
    print(f"{check_num} is even.")
else:
    print(f"{check_num} is odd.")

even_list = get_first_three_evens()
print(f"First three evens: {even_list}\n")

# Multiple return statements

def print_message(message):
    """Prints a message but doesn't explicitly return anything."""
    print(message)

result = print_message("This function prints.")
print(f"The return value is: {result}")
print(f"Is the result None? {result is None}\n")

def get_number_sign(num):
    """Determines the sign of a number."""
    if num > 0:
        return "Positive"  # Exits here if num > 0
    elif num < 0:
        return "Negative"  # Exits here if num < 0
    else:
        return "Zero"      # Exits here if num == 0

sign1 = get_number_sign(15)
sign2 = get_number_sign(-3)
sign3 = get_number_sign(0)

print(f"Sign of 15: {sign1}")
print(f"Sign of -3: {sign2}")
print(f"Sign of 0: {sign3}\n")

def get_coordinates():
    """Returns a pair of coordinates."""
    x = 10
    y = 25
    return x, y # Returns the tuple (10, 25)

coords = get_coordinates()
print(f"Coordinates tuple: {coords}")
print(f"X coordinate: {coords[0]}")
print(f"Y coordinate: {coords[1]}")

# You can also unpack the tuple directly into variables
x_val, y_val = get_coordinates()
print(f"Unpacked X: {x_val}")
print(f"Unpacked Y: {y_val}")