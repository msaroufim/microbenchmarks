import time
from multiprocessing import Process

def simple_function():
    return

# Timing a simple function call
start_time = time.time()
simple_function()
function_duration = time.time() - start_time

# Timing the start (and end) of a new process
start_time = time.time()
p = Process(target=simple_function)
p.start()
p.join()
process_duration = time.time() - start_time

# function duration in ms: 0.000476837158203125
# process duration in ms: 3.0982494354248047
print(f"function duration in ms: {function_duration * 1000}")
print(f"process duration in ms: {process_duration * 1000}")