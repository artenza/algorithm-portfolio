import timeit
import random
from memory_profiler import memory_usage
import matplotlib.pyplot as plt

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def generate_data(size, data_type="random"):
    if data_type == "random":
        return [random.randint(0, 1000) for _ in range(size)]
    elif data_type == "nearly_sorted":
        arr = list(range(size))
        arr[size // 2] = 0  # Introducing a slight disorder
        return arr
    elif data_type == "reverse_sorted":
        return list(range(size, 0, -1))

def benchmark_sorting_algorithm(algorithm, data_type):
    sizes = [1000, 5000, 10000, 20000]
    times = []
    memory_usages = []
    for size in sizes:
        data = generate_data(size, data_type)
        time_taken = timeit.timeit(lambda: algorithm(data), number=1)
        mem_usage = memory_usage((algorithm, (data,)))
        times.append(time_taken)
        memory_usages.append(max(mem_usage))
        print(f"Data Type: {data_type}, Size: {size}, Time: {time_taken:.5f} sec, Memory: {max(mem_usage)} MB")
    return sizes, times, memory_usages

if __name__ == '__main__':
    data_types = ["random", "nearly_sorted", "reverse_sorted"]
    plt.figure(figsize=(12, 6))

    for data_type in data_types:
        sizes, times, memory_usages = benchmark_sorting_algorithm(bubble_sort, data_type)

        # Plotting the results for execution time
        plt.subplot(1, 2, 1)
        plt.plot(sizes, times, marker='o', label=f'{data_type} data')
        plt.title('Execution Time for Different Data Types')
        plt.xlabel('Data Size')
        plt.ylabel('Time (seconds)')
        plt.legend()

        # Plotting the results for memory usage
        plt.subplot(1, 2, 2)
        plt.plot(sizes, memory_usages, marker='o', label=f'{data_type} data')
        plt.title('Memory Usage for Different Data Types')
        plt.xlabel('Data Size')
        plt.ylabel('Memory Usage (MB)')
        plt.legend()

    plt.tight_layout()
    plt.show()
        