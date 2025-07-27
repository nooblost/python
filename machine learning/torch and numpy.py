import torch
import numpy as np

device = torch.device("mps")

# Create a tensor from a Python list
data_list = [[1, 2], [3, 4]]
tensor_from_list = torch.tensor(data_list)

print("Tensor from list:")
print(tensor_from_list)
print(f"Data type: {tensor_from_list.dtype}")
print(f"Shape: {tensor_from_list.shape}")

# Create a tensor from a NumPy array
data_numpy = np.array([[5.0, 6.0], [7.0, 8.0]])
tensor_from_numpy = torch.tensor(data_numpy)

print("\nTensor from NumPy array:")
print(tensor_from_numpy)
print(f"Data type: {tensor_from_numpy.dtype}")
print(f"Shape: {tensor_from_numpy.shape}")

# Define the desired shape
shape = (2, 3) # 2 rows, 3 columns

# Create tensors with specific values
zeros_tensor = torch.zeros(shape)
ones_tensor = torch.ones(shape)
empty_tensor = torch.empty(shape) # Values are arbitrary

print(f"\nZeros Tensor (shape {shape}):")
print(zeros_tensor)

print(f"\nOnes Tensor (shape {shape}):")
print(ones_tensor)

print(f"\nEmpty Tensor (shape {shape}):")
print(empty_tensor)

# Create a tensor of ones with integer type
ones_int_tensor = torch.ones(shape, dtype=torch.int32)
print(f"\nOnes Tensor (dtype=torch.int32):")
print(ones_int_tensor)

# Create tensors with random values
rand_tensor = torch.rand(shape) # Uniform distribution [0, 1)
randn_tensor = torch.randn(shape) # Standard normal distribution

print(f"\nRandom Tensor (Uniform [0, 1), shape {shape}):")
print(rand_tensor)

print(f"\nRandom Tensor (Standard Normal, shape {shape}):")
print(randn_tensor)

# Use an existing tensor as a template
base_tensor = torch.tensor([[1, 2], [3, 4]], dtype=torch.float32)
print(f"\nBase Tensor (shape {base_tensor.shape}, dtype {base_tensor.dtype}):")
print(base_tensor)

# Create tensors matching the base tensor's properties
zeros_like_base = torch.zeros_like(base_tensor)
rand_like_base = torch.rand_like(base_tensor)

print("\nZeros tensor like base:")
print(zeros_like_base)
print(f"Shape: {zeros_like_base.shape}, dtype: {zeros_like_base.dtype}")

print("\nRandom tensor like base:")
print(rand_like_base)
print(f"Shape: {rand_like_base.shape}, dtype: {rand_like_base.dtype}")