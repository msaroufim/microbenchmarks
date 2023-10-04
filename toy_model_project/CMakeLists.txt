cmake_minimum_required(VERSION 3.0 FATAL_ERROR)
project(toy_model)

# Find the Torch package
find_package(Torch REQUIRED)

# Set C++17 as the standard
set(CMAKE_CXX_STANDARD 17)

# Create the executable with the source file
add_executable(toy_model toy_model.cpp)

# Link the Torch libraries to the executable
target_link_libraries(toy_model "${TORCH_LIBRARIES}")
