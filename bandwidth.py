def max_bw():
	import torch
	import time
	import os
	 
	os.system('nvidia-smi')
	iters = 1000
	val = torch.randn(2**16, device='cuda')
	torch.cuda.synchronize()
	begin = time.time()
	for _ in range(iters):
		val = val + 1
	torch.cuda.synchronize()
	print("Memory Bandwidth: ", (iters/(time.time() - begin)) * val.numel() * 4 * 2 / 1e12, "TB/s")
	
	val = torch.randn(8192, 8192, device='cuda', dtype=torch.float16)
	torch.cuda.synchronize()
	begin = time.time()
	for _ in range(iters):
		torch.mm(val, val)
	torch.cuda.synchronize()
	print("FLOPS: ", (iters/(time.time() -begin)) * val.shape[0] ** 3 * 2 / 1e12, "TF/s")


# Memory Bandwidth:  0.018452670998414043 TB/s
# FLOPS:  59.178217022520506 TF/s
max_bw()