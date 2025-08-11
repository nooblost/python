print("What is your name?")
user_name = input()
print("Hello,", user_name)

user_name = input("Enter your name: ")
print("Hello,", user_name)

age_input = input("Enter your age: ")
print("Type of age_input:", type(age_input))
# Attempting addition might cause an error or unexpected behavior
# next_year = age_input + 1 # This would raise a TypeError

age_str = input("Enter your age: ")
age_int = int(age_str) # Convert the input string to an integer

next_year_age = age_int + 1
print("Next year, you will be", next_year_age)

# You can also combine input and conversion in one step:
height_str = input("Enter your height in meters: ")
height_float = float(height_str) # Convert the input string to a float

print("Your height is:", height_float, "meters")