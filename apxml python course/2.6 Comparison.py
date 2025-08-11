# Comparing numbers
print(5 == 5)
print(10 == 7)

# Comparing strings
print("hello" == "hello")
print("Python" == "python") # Case matters!

# Assigning the result to a variable
are_numbers_equal = (100 == 100)
print(are_numbers_equal)

# Comparing numbers
print(5 != 5)
print(10 != 7)

# Comparing strings
print("hello" != "")
print("Python" != "Python")

# Assigning the result
are_different = ("apple" != "orange")
print(are_different)

print(5 < 10)
print(10 < 5)
print(5 < 5) # Not less than, so False

# Strings are compared lexicographically (like in a dictionary)
print("apple" < "banana")
print("cat" < "car") # 't' comes after 'r'

print(10 > 5)
print(5 > 10)
print(5 > 5) # Not greater than, so False

print("zebra" > "apple")

print(5 <= 10)
print(10 <= 5)
print(5 <= 5) # Equal to, so True

print(10 >= 5)
print(5 >= 10)
print(5 >= 5) # Equal to, so True

print(5 == 5.0)
print(10 > 9.99)
print(3 <= 3.0)