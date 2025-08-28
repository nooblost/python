age = 25
has_ticket = True

# Is the person old enough AND has a ticket?
can_enter = (age >= 18) and (has_ticket == True)
print(f"Age is 25, has ticket: {can_enter}") # Output: True

age = 16
# Now the first condition (age >= 18) is False
can_enter = (age >= 18) and (has_ticket == True)
print(f"Age is 16, has ticket: {can_enter}") # Output: False

age = 30
has_ticket = False
# Now the second condition (has_ticket == True) is False
can_enter = (age >= 18) and (has_ticket == True)
print(f"Age is 30, no ticket: {can_enter}") # Output: False

is_weekend = False
is_holiday = True

# Is it the weekend OR a holiday?
day_off = is_weekend or is_holiday
print(f"Weekend: False, Holiday: True -> Day off: {day_off}") # Output: True

is_weekend = True
is_holiday = False
# The first condition is True
day_off = is_weekend or is_holiday
print(f"Weekend: True, Holiday: False -> Day off: {day_off}") # Output: True

is_weekend = False
is_holiday = False
# Both conditions are False
day_off = is_weekend or is_holiday
print(f"Weekend: False, Holiday: False -> Day off: {day_off}") # Output: False

is_logged_in = False
print(f"Is logged in: {is_logged_in}") # Output: False

# Check if the user is NOT logged in
needs_login = not is_logged_in
print(f"Needs login: {needs_login}") # Output: True

is_raining = True
print(f"Is raining: {is_raining}") # Output: True

# Check if it is NOT raining
can_go_outside = not is_raining
print(f"Can go outside: {can_go_outside}") # Output: False

age = 22
is_student = True
has_coupon = False

# Eligible if (age < 25 AND is a student) OR has a coupon
is_eligible_discount = (age < 25 and is_student) or has_coupon
# Evaluates as: (True and True) or False
# -> True or False
# -> True
print(f"Eligible for discount: {is_eligible_discount}") # Output: True

# Change coupon status
has_coupon = True
age = 30
is_student = False

is_eligible_discount = (age < 25 and is_student) or has_coupon
# Evaluates as: (False and False) or True
# -> False or True
# -> True
print(f"Eligible for discount (different criteria): {is_eligible_discount}") # Output: True

# Order of operations: not > and > or