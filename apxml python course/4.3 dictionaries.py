# An empty dictionary
empty_dict = {}

# A dictionary storing student grades
student_grades = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 78
}

print(student_grades)
# Output: {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Keys can be different immutable types (strings, numbers, tuples)
mixed_keys = {
    "name": "Example Item",
    101: "Item ID",
    ("x", "y"): "Coordinates"
}
print(mixed_keys)
# Output: {'name': 'Example Item', 101: 'Item ID', ('x', 'y'): 'Coordinates'}

"""
all keys must be unique
"""

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Get Bob's grade
bobs_grade = student_grades["Bob"]
print(f"Bob's grade is: {bobs_grade}")
# Output: Bob's grade is: 92

# Trying to access a non-existent key causes an error
# print(student_grades["David"]) # This would raise a KeyError

student_grades = {"Alice": 85, "Bob": 92, "Charlie": 78}

# Get Alice's grade using get()
alice_grade = student_grades.get("Alice")
print(f"Alice's grade (using get): {alice_grade}")
# Output: Alice's grade (using get): 85

# Try to get David's grade (doesn't exist)
david_grade = student_grades.get("David")
print(f"David's grade (using get): {david_grade}")
# Output: David's grade (using get): None

# Provide a default value if the key is missing
eve_grade = student_grades.get("Eve", "Not Found")
print(f"Eve's grade (using get with default): {eve_grade}")
# Output: Eve's grade (using get with default): Not Found

student_grades = {"Alice": 85, "Bob": 92}
print(f"Original grades: {student_grades}")

# Add a new student
student_grades["Charlie"] = 78
print(f"After adding Charlie: {student_grades}")

# Update Bob's grade
student_grades["Bob"] = 95
print(f"After updating Bob: {student_grades}")

student_grades = {"Alice": 85, "Bob": 95, "Charlie": 78}
print(f"Initial dictionary: {student_grades}")

# Remove Charlie using del
del student_grades["Charlie"]
print(f"After deleting Charlie: {student_grades}")

# Remove Bob using pop() and get the removed value
bobs_removed_grade = student_grades.pop("Bob")
print(f"Removed Bob's grade: {bobs_removed_grade}")
print(f"Dictionary after popping Bob: {student_grades}")

student_grades = {"Alice": 85, "Bob": 95, "Charlie": 78}

print(f"Keys: {student_grades.keys()}")
print(f"Values: {student_grades.values()}")
print(f"Items: {student_grades.items()}")
print(f"Number of students: {len(student_grades)}")

# Check if 'Alice' is in the dictionary
if "Alice" in student_grades:
    print("Alice is in the grades dictionary.")

# Check if 'David' is in the dictionary
if "David" not in student_grades:
    print("David is not in the grades dictionary.")