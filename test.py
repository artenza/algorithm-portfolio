import timeit
import random
import heapq
import matplotlib.pyplot as plt
from memory_profiler import memory_usage

def bubble_sort(arr):
    # Implement Bubble Sort here
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

def quick_sort(arr):
    # Implement Quick Sort here
    if len(arr) <= 1:
        return arr
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

def heap_sort(arr):
    # Implement Heap Sort here
    heapq.heapify(arr)
    return [heapq.heappop(arr) for _ in range(len(arr))]

def merge_sort(arr):
    # Implement Merge Sort here
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return merge(left, right)

def merge(left, right):
    result = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def generate_data(size):
    return [random.randint(0, 1000) for _ in range(size)]

def benchmark_sorting_algorithm(algorithm, size):
    data = generate_data(size)
    mem_usage_before = memory_usage(-1, interval=0.001, timeout=1, include_children=True)
    start_time = timeit.default_timer()
    algorithm(data)
    time_taken = timeit.default_timer() - start_time
    mem_usage_after = memory_usage(-1, interval=0.001, timeout=1, include_children=True)
    memory_used = max(mem_usage_after) - max(mem_usage_before)
    return time_taken, memory_used

# Reduced dataset sizes for quicker execution
sizes = [100, 200, 300, 400, 500]

time_results = {"Bubble Sort": [], "Quick Sort": [], "Heap Sort": [], "Merge Sort": []}
memory_results = {"Bubble Sort": [], "Quick Sort": [], "Heap Sort": [], "Merge Sort": []}

print("Benchmark Results:")
print("Size\t\tExecution Time (s)\tMemory Usage (MB)")
print("-" * 50)

for size in sizes:
    time_taken, memory_used = benchmark_sorting_algorithm(bubble_sort, size)
    time_results["Bubble Sort"].append(time_taken)
    memory_results["Bubble Sort"].append(memory_used)
    print(f"Bubble Sort ({size})\t{time_taken:.6f}\t\t\t{memory_used:.6f}")

    time_taken, memory_used = benchmark_sorting_algorithm(quick_sort, size)
    time_results["Quick Sort"].append(time_taken)
    memory_results["Quick Sort"].append(memory_used)
    print(f"Quick Sort ({size})\t{time_taken:.6f}\t\t\t{memory_used:.6f}")

    time_taken, memory_used = benchmark_sorting_algorithm(heap_sort, size)
    time_results["Heap Sort"].append(time_taken)
    memory_results["Heap Sort"].append(memory_used)
    print(f"Heap Sort ({size})\t{time_taken:.6f}\t\t\t{memory_used:.6f}")

    time_taken, memory_used = benchmark_sorting_algorithm(merge_sort, size)
    time_results["Merge Sort"].append(time_taken)
    memory_results["Merge Sort"].append(memory_used)
    print(f"Merge Sort ({size})\t{time_taken:.6f}\t\t\t{memory_used:.6f}")

# Plotting the results for Bubble Sort
plt.plot(sizes, time_results["Bubble Sort"], marker='o', label='Bubble Sort')
plt.xlabel("Data Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Bubble Sort Performance")
plt.legend()
plt.show()

# Plotting the results for Quick Sort
plt.plot(sizes, time_results["Quick Sort"], marker='o', label='Quick Sort')
plt.xlabel("Data Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Quick Sort Performance")
plt.legend()
plt.show()

# Plotting the results for Heap Sort
plt.plot(sizes, time_results["Heap Sort"], marker='o', label='Heap Sort')
plt.xlabel("Data Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Heap Sort Performance")
plt.legend()
plt.show()

# Plotting the results for Merge Sort
plt.plot(sizes, time_results["Merge Sort"], marker='o', label='Merge Sort')
plt.xlabel("Data Size")
plt.ylabel("Execution Time (seconds)")
plt.title("Merge Sort Performance")
plt.legend()
plt.show()

# Plotting the memory usage for Bubble Sort, Quick Sort, Heap Sort, and Merge Sort
plt.plot(sizes, memory_results["Bubble Sort"], marker='o', label='Bubble Sort')
plt.plot(sizes, memory_results["Quick Sort"], marker='o', label='Quick Sort')
plt.plot(sizes, memory_results["Heap Sort"], marker='o', label='Heap Sort')
plt.plot(sizes, memory_results["Merge Sort"], marker='o', label='Merge Sort')
plt.xlabel("Data Size")
plt.ylabel("Memory Usage (MB)")
plt.title("Memory Usage Comparison")
plt.legend()
plt.show()
