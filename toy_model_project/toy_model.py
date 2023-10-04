import torch
import time

# Define a toy linear model
class Net(torch.nn.Module):
    def __init__(self, in_features, out_features):
        super(Net, self).__init__()
        self.linear = torch.nn.Linear(in_features, out_features)

    def forward(self, x):
        return self.linear(x)

if __name__ == '__main__':
    # Start measuring the total execution time
    start_total = time.time()

    # Measure time to initialize CUDA context
    start_cuda = time.time()
    device = torch.device("cuda")
    torch.cuda.synchronize()  # Ensure any prior CUDA work is complete
    end_cuda = time.time()
    diff_cuda = end_cuda - start_cuda
    print(f"Time to initialize CUDA context: {diff_cuda:.6f} s")

    # Create an instance of the toy linear model
    net = Net(5, 2)  # 5 input features, 2 output features

    # Move the model to GPU
    net.to(device)
   



    # Create a toy input tensor of size [10, 5] and move it to GPU
    input_tensor = torch.randn(10, 5).to(device)

    # Warm-up: Run inference multiple times
    warmup_runs = 10
    for _ in range(warmup_runs):
        dummy_output = net(input_tensor)

    # Measure time for inference
    start_inference = time.time()
    output = net(input_tensor)
    torch.cuda.synchronize()  # Ensure the inference operation is complete
    end_inference = time.time()
    diff_inference = end_inference - start_inference
    print(f"Time for inference: {diff_inference:.6f} s")

    # End of total execution time measurement
    end_total = time.time()
    diff_total = end_total - start_total
    print(f"Total execution time: {diff_total:.6f} s")
