import torch
import time

start_time = time.time()
torch.cuda.is_available()
torch.cuda.synchronize() 
end_time = time.time()

initialization_time = end_time - start_time

# CUDA initialization time: 76.8589973449707 ms
print(f"CUDA initialization time: {initialization_time * 1000} ms")