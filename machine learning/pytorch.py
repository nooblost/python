import torch
print(f"MPS available: {torch.backends.mps.is_available()}")
print(torch.__version__)

# Check device
device = torch.device("mps")
print(f"Using device: {device}")

# Example: Tensor operations
x = torch.rand(4, 4).to(device)
y = torch.rand(4, 4).to(device)
z = x + y
print(z)

