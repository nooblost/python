programmers = {'Alice', 'Bob', 'Charlie', 'David'}
data_scientists = {'Charlie', 'David', 'Eve', 'Frank'}

print(f"Programmers: {programmers}")
print(f"Data Scientists: {data_scientists}\n")

# Using the | operator
all_staff = programmers | data_scientists
print(f"Union (|): {all_staff}")

# Using the union() method
all_staff_method = programmers.union(data_scientists)
print(f"Union (method): {all_staff_method}")

# Note: The order doesn't matter for union
print(f"Is programmers | data_scientists == data_scientists | programmers? {programmers | data_scientists == data_scientists | programmers}\n")

# Using the & operator
common_roles = programmers & data_scientists
print(f"Intersection (&): {common_roles}")

# Using the intersection() method
common_roles_method = programmers.intersection(data_scientists)
print(f"Intersection (method): {common_roles_method}\n")

# Elements in programmers but NOT in data_scientists
only_programmers = programmers - data_scientists
print(f"Difference (programmers - data_scientists): {only_programmers}")

# Using the difference() method
only_programmers_method = programmers.difference(data_scientists)
print(f"Difference (method): {only_programmers_method}")

# Elements in data_scientists but NOT in programmers
only_data_scientists = data_scientists - programmers
print(f"Difference (data_scientists - programmers): {only_data_scientists}\n")

# Using the ^ operator
exclusive_roles = programmers ^ data_scientists
print(f"Symmetric Difference (^): {exclusive_roles}")

# Using the symmetric_difference() method
exclusive_roles_method = programmers.symmetric_difference(data_scientists)
print(f"Symmetric Difference (method): {exclusive_roles_method}\n")

