"""Importing specific functions from modules"""

import math

radius = 5
area = math.pi * (radius ** 2)
hypotenuse = math.sqrt(3**2 + 4**2)

print(f"Area: {area}")
print(f"Hypotenuse: {hypotenuse}\n")

from math import pi, sqrt

radius = 5
# Notice no 'math.' prefix is needed now
area = pi * (radius ** 2)
hypotenuse = sqrt(3**2 + 4**2)

print(f"Area: {area}")
print(f"Hypotenuse: {hypotenuse}")
# Output:
# Area: 78.53981633974483
# Hypotenuse: 5.0

# Caution: Generally discouraged!
from math import *

# Now all names from math are directly available
print(pi)
print(sqrt(16))
print(cos(0))
# Output:
# 3.141592653589793
# 4.0
# 1.0

""" High risk of namespace collisions: imported names will overwrite user defined functions.
    Reduced readability: difficult to see where function or variable originates.
"""


"""Importing with an alias"""

from math import pi as mathematical_pi

# Use our own variable named 'pi'
pi = 3.14 # A less precise version, maybe for specific needs

radius = 5
piarea = pi * (radius ** 2)
# Use the aliased import for the precise value
area = mathematical_pi * (radius ** 2)

print(f"Our pi: {pi}\n")
print(f"Pi area: {piarea}\n")
print(f"Imported pi: {mathematical_pi}\n")
print(f"Calculated area: {area}")

# Output:
# Our pi: 3.14
# Imported pi: 3.141592653589793
# Calculated area: 78.53981633974483

