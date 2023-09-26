import time

start_time = time.time()
import torch
end_time = time.time()
time_taken = end_time - start_time

# Time taken to import torch: 1291.698932647705 ms
print(f"Time taken to import torch: {time_taken * 1000} ms")