import time
from multiprocessing import Process, cpu_count

def simple_function():
    return

def spawn_multiple_processes():
    processes = []
    for _ in range(cpu_count()):
        p = Process(target=simple_function)
        p.start()
        processes.append(p)
    for p in processes:
        p.join()

# Timing a simple function call
start_time = time.time()
simple_function()
function_duration = time.time() - start_time

# Timing the start (and end) of multiple new processes
start_time = time.time()
spawn_multiple_processes()
process_duration = time.time() - start_time

# function duration in ms: 0.0007152557373046875
# process duration in ms: 5.2852630615234375
# On a machine with 8 CPUs
print(f"function duration in ms: {function_duration * 1000}")
print(f"process duration in ms: {process_duration * 1000}")
