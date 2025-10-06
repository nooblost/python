# An empty list
empty_list = []
print(empty_list)

# A list of integers
numbers = [1, 2, 3, 5, 8]
print(numbers)

# A list of strings
fruits = ["apple", "banana", "cherry"]
print(fruits)

# A list with mixed data types
mixed_list = [10, "hello", 3.14, True]
print(mixed_list)

# A list of tasks for the day
tasks = ["email team", "review report"]
print(f"Tasks to do: {tasks}")

# Add a new task to the end
tasks.append("buy groceries")
print(f"After append: {tasks}")

# Insert a high-priority task at the beginning (index 0)
tasks.insert(0, "call client")
print(f"After insert at index 0: {tasks}")

# Insert another task before 'buy groceries' (which is now at index 3)
tasks.insert(3, "prepare meeting notes")
print(f"After insert at index 3: {tasks}")

# Add more tasks from another list
more_tasks = ["schedule follow-up", "submit expenses"]
tasks.extend(more_tasks)
print(f"After extend: {tasks}")

numbers = [1, 2, 3]
extra_numbers = [4, 5]

# Using extend (correct way to add individual items)
numbers.extend(extra_numbers)
print(f"After extend: {numbers}") # Output: [1, 2, 3, 4, 5]

# Reset numbers and try append
numbers = [1, 2, 3]
numbers.append(extra_numbers)
print(f"After append: {numbers}") # Output: [1, 2, 3, [4, 5]] - Note the nested list!

# Let's go back to our colors list
colors = ["red", "yellow", "purple", "yellow"]
print(f"Current colors: {colors}")

# Remove the first instance of "yellow"
colors.remove("yellow")
print(f"After remove('yellow'): {colors}")

print(f"Current colors: {colors}") # Should be ['red', 'purple', 'yellow']

# Remove and get the item at index 1 ("purple")
removed_color = colors.pop(1)
print(f"Removed color: {removed_color}")
print(f"After pop(1): {colors}")

# Remove and get the last item (default behavior)
last_color = colors.pop()
print(f"Removed last color: {last_color}")
print(f"After pop(): {colors}")

numbers = [10, 20, 30, 40, 50, 60]
print(f"Original numbers: {numbers}")

# Remove the item at index 0
del numbers[0]
print(f"After del numbers[0]: {numbers}")

# Remove items from index 2 up to (but not including) index 4
# This removes the items currently at index 2 and 3 (30 and 40 originally, now 40 and 50)
del numbers[2:4]
print(f"After del numbers[2:4]: {numbers}")

# del can also delete the entire list variable, but that's different from clearing it
# del numbers
# print(numbers) # This would now cause a NameError

numbers = [10, 60] # From the previous example
print(f"Numbers before clear: {numbers}")

numbers.clear()
print(f"Numbers after clear: {numbers}")

# iterate list and show index of contents

fruits = ["apple", "banana", "cherry"]
for index, fruit in enumerate(fruits):
    print(f"Index: {index}, Fruit: {fruit}")

