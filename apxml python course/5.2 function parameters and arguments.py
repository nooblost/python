# Define a function with one parameter named 'user_name'
def greet(user_name):
  """Prints a simple greeting."""
  print(f"Hello, {user_name}!\n")

# Call the function, passing the argument "Alice"
greet("Alice")

# Call the function again with a different argument
greet("Bob")

# Multiple arguments

def describe_pet(animal_type, pet_name):
  """Displays information about a pet."""
  print(f"I have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name}.")

# Call with positional arguments
describe_pet("hamster", "Harry")
print("---") # Just to separate outputs
describe_pet("dog", "Willie")

# Keyword arguments

def describe_pet(animal_type, pet_name):
  """Displays information about a pet."""
  print(f"I have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name}.")

# Call using keyword arguments
describe_pet(animal_type="hamster", pet_name="Harry")
print("---")
# Order doesn't matter with keyword arguments
describe_pet(pet_name="Willie", animal_type="dog")

# Combining positional and keyword arguments

#positional arguments MUST come before keyword arguments

def describe_pet(animal_type, pet_name):
  """Displays information about a pet."""
  print(f"I have a {animal_type}.")
  print(f"My {animal_type}'s name is {pet_name}.")

# Valid: Positional argument first
describe_pet("cat", pet_name="Whiskers")

# Invalid: Keyword argument cannot be followed by a positional one
#describe_pet(animal_type="dog", "Buddy") # This would cause a SyntaxError

