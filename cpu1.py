import psutil

# Function to get CPU and memory utilization
def get_cpu_memory_usage():
    cpu_percent = psutil.cpu_percent()
    virtual_memory = psutil.virtual_memory()
    memory_percent = virtual_memory.percent
    return cpu_percent, memory_percent

if __name__ == "__main__":
    # Start monitoring CPU and memory before running your code
    initial_cpu, initial_memory = get_cpu_memory_usage()

    # Your existing Python code goes here
         
    # End monitoring CPU and memory after running your code
    final_cpu, final_memory = get_cpu_memory_usage()

    # Calculate the difference to get the actual CPU and memory usage during the execution of your code
    cpu_usage = final_cpu - initial_cpu
    memory_usage = final_memory - initial_memory

    # Print the results
    print(f"CPU Usage: {cpu_usage}%")
    print(f"Memory Usage: {memory_usage}%")

