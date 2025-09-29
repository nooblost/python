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

