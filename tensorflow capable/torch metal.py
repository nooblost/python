import torch
import time

# Check device
device = torch.device("mps" if torch.backends.mps.is_available() else "cpu")
print(f"Using device: {device}")

x = torch.rand(1000, 1000)

# CPU Benchmark
start = time.time()
for _ in range(100):
    y = x @ x
end = time.time()
print(f"CPU time: {end - start:.4f} sec")

# MPS Benchmark
x = x.to("mps")
start = time.time()
for _ in range(100):
    y = x @ x
end = time.time()
print(f"MPS time: {end - start:.4f} sec")

# Example: Tensor operations
x = torch.rand(3, 3, 3).to(device)
y = torch.rand(3, 3, 3).to(device)
z = x + y
print(z)