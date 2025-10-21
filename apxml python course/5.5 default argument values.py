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
  print(f"Permissions: {permissions}")

