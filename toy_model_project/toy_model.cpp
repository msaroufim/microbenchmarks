#include <torch/torch.h>
#include <iostream>
#include <chrono>

// Define a toy linear model
struct Net : torch::nn::Module {
    Net(int in_features, int out_features) 
        : linear(register_module("linear", torch::nn::Linear(in_features, out_features))) 
    {}

    torch::Tensor forward(torch::Tensor x) {
        return linear->forward(x);
    }

    torch::nn::Linear linear{nullptr};
};

int main() {
    // Start measuring the total execution time
    auto start_total = std::chrono::high_resolution_clock::now();

    // Measure time to initialize CUDA context
    auto start_cuda = std::chrono::high_resolution_clock::now();
    torch::Device device(torch::kCUDA);
    torch::cuda::synchronize();  // Add synchronization after CUDA context initialization
    auto end_cuda = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff_cuda = end_cuda - start_cuda;
    std::cout << "Time to initialize CUDA context: " << diff_cuda.count() << " s" << std::endl;

    // Create an instance of the toy linear model
    Net net(5, 2);  // 5 input features, 2 output features

    // Move the model to GPU
    net.to(device);

    // Create a toy input tensor of size [10, 5] and move it to GPU
    torch::Tensor input = torch::randn({10, 5}).to(device);

    // Warm-up: Run inference multiple times
    const int warmup_runs = 10;  // you can adjust this number as needed
    for (int i = 0; i < warmup_runs; ++i) {
        torch::Tensor dummy_output = net.forward(input);
    }

    torch::cuda::synchronize();  // Synchronize before starting the timer for inference

    // Measure time for inference
    auto start_inference = std::chrono::high_resolution_clock::now();
    torch::Tensor output = net.forward(input);
    torch::cuda::synchronize();  // Synchronize after inference to get accurate timing
    auto end_inference = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff_inference = end_inference - start_inference;
    std::cout << "Time for inference: " << diff_inference.count() << " s" << std::endl;

    // End of total execution time measurement
    auto end_total = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> diff_total = end_total - start_total;
    std::cout << "Total execution time: " << diff_total.count() << " s" << std::endl;

    return 0;
}
