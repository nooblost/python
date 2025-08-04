# Booleans
is_learning = True
is_finished = False

print(is_learning)
print(is_finished)

age = 20
is_adult = age >= 18  # Is age greater than or equal to 18?
print(is_adult)      # Output: True

temperature = 15.5
is_cold = temperature < 10.0 # Is temperature less than 10.0?
print(is_cold)       # Output: False

name = "Alice"
is_bob = name == "Bob" # Is the name equal to "Bob"?
print(is_bob)          # Output: False

logged_in = True
is_admin = False

# 'and' requires both sides to be True for the result to be True
can_access_admin_panel = logged_in and is_admin
print(can_access_admin_panel) # Output: False

# 'or' requires at least one side to be True for the result to be True
can_view_content = logged_in or is_admin
print(can_view_content)       # Output: True

# 'not' inverts the boolean value
is_guest = not logged_in
print(is_guest)               # Output: False

items = []
if items: # items is empty, so it's falsy
    print("There are items in the list.")
else:
    print("The list is empty.") # This will be printed

user_name = "Charlie"
if user_name: # user_name is not empty, so it's truthy
    print(f"Hello, {user_name}!") # This will be printed
else:
    print("User name is missing.")

count = 0
if count: # count is 0, so it's falsy
    print("Count is positive.")
else:
    print("Count is zero.") # This will be printed