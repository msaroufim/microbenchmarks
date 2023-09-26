import time

start_time = time.time()
import torch
import torch._dynamo
import torch._inductor
end_time = time.time()
time_taken = end_time - start_time

# Time taken to import torch: 3221.297264099121 ms
print(f"Time taken to import torch: {time_taken * 1000} ms")