import torch
device = torch.device("mps")

# Create two tensors
a = torch.tensor([[1., 2.], [3., 4.]]).to(device)
b = torch.tensor([[5., 6.], [7., 8.]]).to(device)

# Addition
sum_tensor = a + b
print("Addition (a + b):\n", sum_tensor)
print("Addition (torch.add(a, b)):\n", torch.add(a, b))

# Subtraction
diff_tensor = a - b
print("\nSubtraction (a - b):\n", diff_tensor)

# Element-wise Multiplication
mul_tensor = a * b
print("\nElement-wise Multiplication (a * b):\n", mul_tensor)
print("Element-wise Multiplication (torch.mul(a, b)):\n", torch.mul(a, b))

# Division
div_tensor = a / b
print("\nDivision (a / b):\n", div_tensor)

# Exponentiation
pow_tensor = a ** 2
print("\nExponentiation (a ** 2):\n", pow_tensor)
print("Exponentiation (torch.pow(a, 2)):\n", torch.pow(a, 2))