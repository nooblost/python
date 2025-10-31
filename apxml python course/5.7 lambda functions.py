# Using a standard function definition
def add(x, y):
  return x + y

# Using a lambda function
add_lambda = lambda x, y: x + y

# Both can be called in the same way
result1 = add(10, 5)
result2 = add_lambda(10, 5)

print(f"Result from def function: {result1}")  # Output: Result from def function: 15
print(f"Result from lambda function: {result2}") # Output: Result from lambda function: 15

numbers = [1, 2, 3, 4, 5]

# Use map with a lambda function to square each number
squared_numbers = map(lambda x: x * x, numbers)

# Convert the map object to a list to see the results
print(list(squared_numbers))  # Output: [1, 4, 9, 16, 25]

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# Use filter with a lambda function to get only even numbers
even_numbers = filter(lambda x: x % 2 == 0, numbers)

# Convert the filter object to a list
print(list(even_numbers)) # Output: [2, 4, 6, 8, 10]

# List of tuples (name, age)
people = [('Alice', 30), ('Bob', 25), ('Charlie', 35)]

# Sort the list by age (the second element of each tuple)
sorted_by_age = sorted(people, key=lambda person: person[1])

print(sorted_by_age) # Output: [('Bob', 25), ('Alice', 30), ('Charlie', 35)]