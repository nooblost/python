"""
The Basic import Statement

The simplest way to use a module is with the import keyword followed by the name of the module file (without the .py extension).

Let's say you want to use some mathematical functions. Python comes with a built-in module named math that contains many useful mathematical operations and constants. To use it, you start your script with:

import math
What does this line actually do?

Finds the Module: Python searches for a file named math.py (or other types of modules, but primarily .py files for now)
in a specific list of directories it knows about. This list includes the directory containing your current script and standard library locations.
Executes the Module (if needed): If the module hasn't been loaded before in the current program execution, Python runs the code inside math.py.
This makes all the functions, variables, and classes defined in math.py available.
Creates a Namespace: This is a very important point.
The import math statement does not directly copy all the functions like sqrt or constants like pi from the math module into your current script's main workspace.
Instead, it creates a single name in your script's namespace: math. This math name now refers to the module object itself.
"""

"""
Accessing Module Contents: Dot Notation

Because import math creates a namespace called math, you need to tell Python where to look for the functions or variables defined within that module. 
You do this using dot notation: module_name.item_name.

To use the square root function (sqrt) from the math module, you would write:

math.sqrt(16)
To access the constant pi (pi), you would write:

math.pi
This explicit module_name. prefix is beneficial because it prevents naming conflicts. 
If you had defined your own variable named pi in your script, it wouldn't clash with math.pi because they exist in different namespaces. 
Your pi is in the main script's namespace, while the mathematical constant is accessed through the math namespace.
"""

# Import the entire math module
import math

# Calculate the square root of 25
number = 25
square_root = math.sqrt(number)
print(f"The square root of {number} is {square_root}") # Output: The square root of 25 is 5.0

# Calculate the area of a circle with radius 3
radius = 3
area = math.pi * (radius ** 2) # Using math.pi and the power operator

print(f"\nThe area of a circle with radius {radius} is {area}\n")
# Output: The area of a circle with radius 3 is 28.274333882308138

import math
import random # Another standard library module for random numbers
import os     # Module for interacting with the operating system

print(math.sqrt(100))
print(random.randint(1, 10)) # Get a random integer between 1 and 10
print(os.getcwd())           # Get the current working directory

