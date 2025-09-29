# Creating a set with unique elements
unique_numbers = {1, 2, 3, 4, 5}
print(unique_numbers)
# Output might be {1, 2, 3, 4, 5} or some other order

# Creating a set with duplicates - duplicates are automatically removed
colors = {'red', 'green', 'blue', 'red'}
print(colors)
# Output: {'blue', 'red', 'green'} (order may vary)

# Correct way to create an empty set
empty_s = set()
print(type(empty_s))
# Output: <class 'set'>
print(empty_s)
# Output: set()

# This creates an empty dictionary, NOT a set
empty_d = {}
print(type(empty_d))
# Output: <class 'dict'>

# Create a set from a list with duplicates
numbers_list = [1, 2, 2, 3, 4, 4, 4, 5]
unique_numbers_set = set(numbers_list)
print(unique_numbers_set)
# Output: {1, 2, 3, 4, 5} (order may vary)

# Create a set from a string
letters_set = set('hello')
print(letters_set)
# Output: {'h', 'l', 'o', 'e'} (order may vary)

permissions = {'read', 'write'}
print(permissions)
# Output: {'write', 'read'} (order may vary)

# Add a new permission
permissions.add('execute')
print(permissions)
# Output: {'write', 'read', 'execute'} (order may vary)

# Try adding an existing element - no change
permissions.add('read')
print(permissions)
# Output: {'write', 'read', 'execute'} (order may vary)

data_points = {10, 20, 30, 40}

# Remove an existing element using remove()
data_points.remove(20)
print(data_points)
# Output: {10, 40, 30} (order may vary)

# Try removing a non-existent element using remove() - This will cause an error
# data_points.remove(99) # Raises KeyError: 99

# Remove an existing element using discard()
data_points.discard(30)
print(data_points)
# Output: {10, 40} (order may vary)

# Try removing a non-existent element using discard() - No error
data_points.discard(99)
print(data_points)
# Output: {10, 40} (order may vary)

allowed_users = {'alice', 'bob', 'charlie'}

# Check if a user is allowed
print('bob' in allowed_users)
# Output: True

print('eve' in allowed_users)
# Output: False

# Check if a user is NOT allowed
print('david' not in allowed_users)
# Output: True

log_entries = ['user1', 'user2', 'user1', 'user3', 'user2', 'user1']

# Use a set to find unique users
unique_users_set = set(log_entries)
print(unique_users_set)
# Output: {'user2', 'user3', 'user1'} (order may vary)

# If you need a list of unique users (order might not be original)
unique_users_list = list(unique_users_set)
print(unique_users_list)
# Output: ['user2', 'user3', 'user1'] (order may vary)