# Arithmetic

apples = 5
oranges = 10
total_fruit = apples + oranges
print(total_fruit) # Output: 15

price = 9.99
tax = 0.80
total_cost = price + tax
print(total_cost) # Output: 10.79

budget = 100
spent = 35.50
remaining = budget - spent
print(remaining) # Output: 64.5

width = 8
height = 12
area = width * height
print(area) # Output: 96

total_distance = 100 # kilometers
time_hours = 2 # hours
speed = total_distance / time_hours
print(speed) # Output: 50.0

items = 10
people = 4
items_per_person = items / people
print(items_per_person) # Output: 2.5

cookies = 10
friends = 3
cookies_per_friend = cookies // friends
print(cookies_per_friend) # Output: 3 (Each friend gets 3 whole cookies)

value = 7
divisor = 2
result = value // divisor
print(result) # Output: 3 (7 divided by 2 is 3.5, rounded down is 3)

# Compare with standard division
print(10 / 3)  # Output: 3.3333333333333335
print(10 // 3) # Output: 3

total_cookies = 10
friends = 3
leftover_cookies = total_cookies % friends
print(leftover_cookies) # Output: 1 (After giving 3 cookies each, 1 is left)

number = 17
divisor = 5
remainder = number % divisor
print(remainder) # Output: 2 (17 divided by 5 is 3 with a remainder of 2)

num = 6
print(num % 2) # Output: 0 (So, 6 is even)

num = 7
print(num % 2) # Output: 1 (So, 7 is odd)

base = 2
exponent = 3
power_result = base ** exponent # Equivalent to 2 * 2 * 2
print(power_result) # Output: 8

side = 5
area_square = side ** 2 # Equivalent to 5 * 5 (5 squared)
print(area_square) # Output: 25

result = 2 + 3 * 4
print(result) # Output: 14 (Multiplication is done before addition: 2 + 12)

calculation = 100 - 20 / 5 * 2 + 3**2
# Step-by-step evaluation:
# 1. Exponentiation: 3**2 becomes 9
#    Expression: 100 - 20 / 5 * 2 + 9
# 2. Division/Multiplication (from left to right):
#    20 / 5 becomes 4.0
#    Expression: 100 - 4.0 * 2 + 9
#    4.0 * 2 becomes 8.0
#    Expression: 100 - 8.0 + 9
# 3. Addition/Subtraction (from left to right):
#    100 - 8.0 becomes 92.0
#    Expression: 92.0 + 9
#    92.0 + 9 becomes 101.0
print(calculation) # Output: 101.0

count = 0
count = count + 1 # Increment count by 1
print(count) # Output: 1

total_cost = 50
item_price = 15.50
total_cost = total_cost + item_price # Add item_price to total_cost
print(total_cost) # Output: 65.5

count = 0
count += 1 # Equivalent to count = count + 1
print(count) # Output: 1

score = 100
score -= 10 # Equivalent to score = score - 10
print(score) # Output: 90

multiplier = 5
multiplier *= 2 # Equivalent to multiplier = multiplier * 2
print(multiplier) # Output: 10

total = 50.0
total /= 4 # Equivalent to total = total / 4
print(total) # Output: 12.5