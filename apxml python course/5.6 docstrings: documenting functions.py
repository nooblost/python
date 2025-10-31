def greet(name):
    """Prints a simple greeting."""
    print(f"Hello, {name}!")

def calculate_rectangle_area(length, width):
    """
    Calculates the area of a rectangle.

    This function takes the length and width of a rectangle
    and returns its calculated area.

    Args:
        length (float): The length of the rectangle.
        width (float): The width of the rectangle.

    Returns:
        float: The calculated area of the rectangle.
    """
    if length < 0 or width < 0:
        # We'll learn about raising errors later, for now just return None
        print("Error: Length and width cannot be negative.")
        return None
    return length * width

print(calculate_rectangle_area.__doc__)