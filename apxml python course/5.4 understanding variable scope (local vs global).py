def greet_user():
    message = "Hello from inside the function!\n" # message is local to greet_user
    print(message)

greet_user()

# Now, let's try to access 'message' outside the function:
# print(message) # This line will cause a NameError

app_version = "1.0" # app_version is a global variable

def display_version():
    print("Inside the function, app version is:", app_version) # Accessing the global variable

print("Outside the function, app version is:", app_version)
display_version()

animal = "Global Fox" # Global variable

def print_local_animal():
    animal = "Local Bear" # Local variable with the same name
    print("Inside function:", animal)

print("Outside function (before call):", animal)
print_local_animal()
print("Outside function (after call):", animal)

counter = 0 # Global variable

def increment_counter():
    global counter # Declare intention to use the global 'counter'
    counter += 1   # Modify the global variable
    print("Counter inside function:", counter)

print("Counter before:", counter)
increment_counter()
increment_counter()
print("Counter after:", counter)

# Alternative approach (often preferred)
counter = 0 # Global variable

def calculate_new_count(current_count):
    # This function doesn't modify global state directly
    return current_count + 1

print("Counter before:", counter)
counter = calculate_new_count(counter) # Update global variable based on return value
print("Counter after first update:", counter)
counter = calculate_new_count(counter)
print("Counter after second update:", counter)