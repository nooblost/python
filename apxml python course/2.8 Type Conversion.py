count_float = 9.8
count_int = int(count_float)
print(count_int)  # Output: 9

price_float = 15.2
price_int = int(price_float)
print(price_int) # Output: 15

num_string = "101"
num_int = int(num_string)
print(num_int * 2) # Output: 202

whole_number = 50
float_number = float(whole_number)
print(float_number) # Output: 50.0

pi_string = "3.14159"
pi_float = float(pi_string)
print(pi_float) # Output: 3.14159

count_string = "100"
count_float_from_string = float(count_string)
print(count_float_from_string) # Output: 100.0

item_count = 5
message = "You have " + str(item_count) + " items in your cart."
print(message) # Output: You have 5 items in your cart.

temperature = 22.5
weather_report = "The temperature is " + str(temperature) + " degrees Celsius."
print(weather_report) # Output: The temperature is 22.5 degrees Celsius.

is_active = True
status_message = "User active status: " + str(is_active)
print(status_message) # Output: User active status: True

print(bool(100))        # Output: True
print(bool(-5.5))       # Output: True
print(bool("Python"))     # Output: True
print(bool([1, 2, 3]))  # Output: True

print(bool(0))          # Output: False
print(bool(0.0))        # Output: False
print(bool(""))          # Output: False
print(bool([]))         # Output: False
print(bool({}))         # Output: False
print(bool(None))       # Output: False

