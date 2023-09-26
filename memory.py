import gc
import torch 
import psutil 
import os

def measure_memory_for_large_tensor():
    # Force a garbage collection to start with a cleaner slate
    gc.collect()
    
    # Measure initial memory usage
    process = psutil.Process(os.getpid())
    initial_memory = process.memory_info().rss / (1024 ** 3)  # in GB
    
    # Create a torch tensor (10,000 x 10,000 tensor of float32 values)
    tensor = torch.randn(10000, 10000)
    
    # Measure memory after tensor creation
    final_memory = process.memory_info().rss / (1024 ** 3)  # in GB
    
    # Calculate tensor size in GB
    tensor_size_gb = 10000 * 10000 * 4 / (1024 ** 3)
    
    # Calculate the overhead
    overhead = final_memory - initial_memory - tensor_size_gb
    
    # Return the overhead and tensor size in GB
    return overhead, tensor_size_gb

# Let's run the function to get the overhead and tensor size for a 10,000 x 10,000 tensor
overhead_large_tensor, tensor_size_large_tensor = measure_memory_for_large_tensor()
overhead_large_tensor, tensor_size_large_tensor


# Overhead of creating a 10,000 x 10,000 tensor: 0.0013189315795898438 GB
# Tensor size of a 10,000 x 10,000 tensor: 0.3725290298461914 GB
# Overhead as a percentage of tensor size: 0.354048 %
print(f"Overhead of creating a 10,000 x 10,000 tensor: {overhead_large_tensor} GB")
print(f"Tensor size of a 10,000 x 10,000 tensor: {tensor_size_large_tensor} GB")
print(f"Overhead as a percentage of tensor size: {overhead_large_tensor / tensor_size_large_tensor * 100} %")