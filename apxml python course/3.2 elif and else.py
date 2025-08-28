number = -10

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")

# If number is 0, neither condition above is True, so nothing happens yet.

number = 0

print(f"Checking the number: {number}")

if number > 0:
    print("The number is positive.")
elif number < 0:
    print("The number is negative.")
else:
    # This block runs only if number is not > 0 AND number is not < 0
    print("The number is zero.")

print("Finished checking.")

# Order matters

score = 85

if score >= 70: # This is True first
    grade = 'C'
elif score >= 80: # This is also True, but checked later
    grade = 'B'
else:
    grade = 'Not C or B'

print(grade) # Output: C

score = 85

if score >= 90:
    grade = 'A'
elif score >= 80: # Checked second, True for 85
    grade = 'B'
elif score >= 70: # Checked third
    grade = 'C'
# ... other grades
else:
    grade = 'F'

print(grade) # Output: B