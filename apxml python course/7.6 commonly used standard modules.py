import math

# Calculate the square root of 16
sqrt_16 = math.sqrt(16)
print(f"The square root of 16 is: {sqrt_16}") # Output: The square root of 16 is: 4.0

# Get the value of Pi
pi_value = math.pi
print(f"The value of Pi is approximately: {pi_value}") # Output: The value of Pi is approximately: 3.141592653589793

# Calculate 2 raised to the power of 3
power_result = math.pow(2, 3)
print(f"2 raised to the power of 3 is: {power_result}") # Output: 2 raised to the power of 3 is: 8.0

# Round a number up to the nearest integer (ceiling)
ceil_result = math.ceil(4.2)
print(f"The ceiling of 4.2 is: {ceil_result}") # Output: The ceiling of 4.2 is: 5

# Round a number down to the nearest integer (floor)
floor_result = math.floor(4.9)
print(f"The floor of 4.9 is: {floor_result}\n") # Output: The floor of 4.9 is: 4

import random

# Generate a random floating-point number between 0.0 (inclusive) and 1.0 (exclusive)
random_float = random.random()
print(f"A random float between 0.0 and 1.0: {random_float}")

# Generate a random integer between 1 and 10 (inclusive)
random_int = random.randint(1, 10)
print(f"A random integer between 1 and 10: {random_int}")

# Choose a random element from a list
options = ['rock', 'paper', 'scissors']
choice = random.choice(options)
print(f"Random choice from {options}: {choice}")

# Shuffle a list in place (modifies the original list)
deck = ['Ace', 'King', 'Queen', 'Jack']
print(f"Original deck: {deck}")
random.shuffle(deck)
print(f"Shuffled deck: {deck}\n")

import datetime

# Get the current date and time
now = datetime.datetime.now()
print(f"Current date and time: {now}")

# Get just the current date
today = datetime.date.today()
print(f"Today's date: {today}")

# Create a specific date object
specific_date = datetime.date(2024, 7, 26)
print(f"A specific date: {specific_date}")

# Get components of the current time
current_hour = now.hour
current_minute = now.minute
print(f"Current time: {current_hour}:{current_minute}")

# Format a date into a string (e.g., YYYY-MM-DD)
formatted_date = now.strftime("%Y-%m-%d")
print(f"Formatted date: {formatted_date}")

# Format date and time (e.g., Month Day, Year HH:MM:SS)
formatted_datetime = now.strftime("%B %d, %Y %H:%M:%S")
print(f"Formatted date and time: {formatted_datetime}")

