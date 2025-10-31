def greet(name, greeting="Hello"):
  """Prints a greeting.

  Args:
    name: The name of the person to greet.
    greeting: The greeting message to use (defaults to "Hello").
  """
  print(f"{greeting}, {name}!")

# Calling the function
greet("Alice")             # Uses the default greeting
greet("Bob", "Good morning") # Overrides the default greeting

"""
Rules for ordering argument parameters:

"""

def create_user(username, is_active=True, permissions="read"):
  print(f"Creating user: {username}")
  print(f"Active: {is_active}")
  print(f"Permissions: {permissions}\n")

def add_item(item, my_list=[]):
  """Adds an item to a list. (Demonstrates mutable default issue)"""
  my_list.append(item)
  print(f"List is now: {my_list}")

print("First call:")
add_item("apple")

print("\nSecond call:")
add_item("banana") # Unexpectedly adds to the list from the first call!

print("\nThird call, providing a list:")
add_item("cherry", ["start"]) # Works as expected when a list is provided

def add_item_safe(item, my_list=None):
  """Adds an item to a list safely."""
  if my_list is None:
    my_list = [] # Create a new list if none was provided
  my_list.append(item)
  print(f"List is now: {my_list}")

print("First call (safe):")
add_item_safe("apple")

print("\nSecond call (safe):")
add_item_safe("banana") # Starts with a new empty list

print("\nThird call, providing a list (safe):")
add_item_safe("cherry", ["start"])