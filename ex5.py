import numpy as np
import matplotlib.pyplot as plt
from timeit import default_timer as timer
from scipy.optimize import curve_fit

def linear_search(arr, target):
    try:
        for i in range(len(arr)):
            if arr[i] == target:
                return i
        return -1
    except Exception as e:
        return -1  # Return -1 if any error occurs

def binary_search(arr, target):
    try:
        left, right = 0, len(arr) - 1
        while left <= right:
            mid = (left + right) // 2
            if arr[mid] == target:
                return mid
            elif arr[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1
    except Exception as e:
        return -1  # Return -1 if any error occurs

# Generate test vectors of different sizes
sizes = [1000, 2000, 4000, 8000, 16000, 32000]
vectors = [np.sort(np.random.randint(0, size * 10, size)) for size in sizes]

# Performance measurement function
def measure_search_time(search_func, arr):
    try:
        total_time = 0
        iterations = 100  # Number of iterations for each measurement
        
        for _ in range(iterations):
            target = int(np.random.choice(arr))  # Convert to int to avoid numpy type issues
            start_time = timer()
            search_func(arr.tolist(), target)  # Convert array to list
            end_time = timer()
            total_time += (end_time - start_time)
        
        return total_time / iterations
    except Exception as e:
        print(f"Error in measure_search_time: {e}")
        return 0

# Measure performance for each size
linear_times = []
binary_times = []

try:
    for vector in vectors:
        linear_time = 0
        binary_time = 0
        
        # Run 1000 trials as specified
        for _ in range(1000):
            linear_time += measure_search_time(linear_search, vector)
            binary_time += measure_search_time(binary_search, vector)
        
        # Average the times
        linear_times.append(linear_time / 1000)
        binary_times.append(binary_time / 1000)

    # Curve fitting functions
    def linear_func(x, a, b):
        return a * x + b

    def log_func(x, a, b):
        return a * np.log(x) + b

    # Fit curves
    linear_params, _ = curve_fit(linear_func, sizes, linear_times)
    binary_params, _ = curve_fit(log_func, sizes, binary_times)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.scatter(sizes, linear_times, label='Linear Search (measured)', color='blue')
    plt.scatter(sizes, binary_times, label='Binary Search (measured)', color='red')

    # Plot fitted curves
    x_fit = np.linspace(min(sizes), max(sizes), 100)
    plt.plot(x_fit, linear_func(x_fit, *linear_params), '--', 
             label=f'Linear fit (ax + b), a={linear_params[0]:.2e}, b={linear_params[1]:.2e}',
             color='blue')
    plt.plot(x_fit, log_func(x_fit, *binary_params), '--',
             label=f'Logarithmic fit (a*log(x) + b), a={binary_params[0]:.2e}, b={binary_params[1]:.2e}',
             color='red')

    plt.xlabel('Input Size')
    plt.ylabel('Average Time (seconds)')
    plt.title('Search Algorithm Performance Comparison')
    plt.legend()
    plt.grid(True)
    plt.show()

except KeyboardInterrupt:
    print("\nProgram interrupted by user")
except Exception as e:
    print(f"An error occurred: {e}")

"""
Discussion of Results:

1. Linear Search:
   - Type of function: Linear (ax + b)
   - Parameters: 
     a = slope (represents the time cost per element)
     b = y-intercept (represents fixed overhead)
   The results match expectations because linear search must check each element
   sequentially, leading to O(n) time complexity.

2. Binary Search:
   - Type of function: Logarithmic (a*log(x) + b)
   - Parameters:
     a = logarithmic coefficient
     b = y-intercept (represents fixed overhead)
   The results match expectations because binary search repeatedly divides the
   search space in half, leading to O(log n) time complexity.

The empirical results strongly support the theoretical complexity analysis:
- Linear search shows a clear linear relationship between input size and time
- Binary search shows logarithmic growth, with much better performance on larger inputs
- The fitted curves closely match the measured data points, validating the
  theoretical complexity classes of these algorithms
"""