# Example dictionary: Student grades
student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Access Bob's grade
bob_grade = student_grades['Bob']
print(f"Bob's grade is: {bob_grade}") # Output: Bob's grade is: 92

# Access Alice's grade
alice_grade = student_grades['Alice']
print(f"Alice's grade is: {alice_grade}\n") # Output: Alice's grade is: 85


student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Get Bob's grade (key exists)
bob_grade = student_grades.get('Bob')
print(f"Bob's grade (using get): {bob_grade}") # Output: Bob's grade (using get): 92

# Try to get David's grade (key does not exist)
david_grade = student_grades.get('David')
print(f"David's grade (using get): {david_grade}") # Output: David's grade (using get): None


student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Get David's grade, return 0 if not found
david_grade = student_grades.get('David', 0)
print(f"David's grade (with default): {david_grade}") # Output: David's grade (with default): 0

# Get Alice's grade (key exists, default is ignored)
alice_grade = student_grades.get('Alice', 0)
print(f"Alice's grade (with default): {alice_grade}\n") # Output: Alice's grade (with default): 85


student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# Check if 'Alice' is a key
if 'Alice' in student_grades:
    print("Alice is in the dictionary.")
    # Safe to access now
    print(f"Alice's grade: {student_grades['Alice']}")
else:
    print("Alice is not in the dictionary.")

# Check if 'David' is a key
if 'David' in student_grades:
    print("David is in the dictionary.")
else:
    print("David is not in the dictionary.\n") # This will be printed

    student_grades = {'Alice': 85, 'Bob': 92, 'Charlie': 78}
    print(f"Original grades: {student_grades}")

    # Add a new student, David
    student_grades['David'] = 88
    print(f"After adding David: {student_grades}")

    # Update Bob's grade
    student_grades['Bob'] = 95
    print(f"After updating Bob's grade: {student_grades}\n")


student_grades = {'Alice': 85, 'Bob': 95, 'Charlie': 78, 'David': 88}
print(f"Grades before deletion: {student_grades}")

# Remove Charlie from the dictionary
del student_grades['Charlie']
print(f"Grades after deleting Charlie: {student_grades}\n")


student_grades = {'Alice': 85, 'Bob': 95, 'David': 88}
print(f"Grades before pop: {student_grades}")

# Remove David and store his grade
davids_removed_grade = student_grades.pop('David')
print(f"Removed David's grade: {davids_removed_grade}") # Output: Removed David's grade: 88
print(f"Grades after popping David: {student_grades}\n")  # Output: Grades after popping David: {'Alice': 85, 'Bob': 95}


student_grades = {'Alice': 85, 'Bob': 95}

# Try to pop 'Charlie', provide a default value
result = student_grades.pop('Charlie', 'Not Found')
print(f"Result of popping Charlie: {result}") # Output: Result of popping Charlie: Not Found
print(f"Grades remain unchanged: {student_grades}\n") # Output: Grades remain unchanged: {'Alice': 85, 'Bob': 95}


student_grades = {'Alice': 85, 'Bob': 95}
student_grades['Eve'] = 90 # Add Eve last

# Remove and return the last added item (in Python 3.7+)
last_item = student_grades.popitem()
print(f"Removed item: {last_item}") # Output: Removed item: ('Eve', 90)
print(f"Dictionary after popitem: {student_grades}") # Output: Dictionary after popitem: {'Alice': 85, 'Bob': 95}