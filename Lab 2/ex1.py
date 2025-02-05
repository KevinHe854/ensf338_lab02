# 1.The code implements the Fibonacci sequence
# 2.no, The code is not an example of divide and conquer
# 3. 0(n) is an expression of the time complexity in the program



#def func(n):
 #   if n == 0 or n == 1:
  #      return n
   # else:
    #    return func(n-1) + func(n-2)

import time
import matplotlib.pyplot as plt
import numpy as np

# Original recursive implementation
def fib_recursive(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib_recursive(n-1) + fib_recursive(n-2)

# Memoized implementation
def fib_memo(n, memo=None):
    if memo is None:
        memo = {}
    if n == 0 or n == 1:
        return n
    if n in memo:
        return memo[n]
    memo[n] = fib_memo(n-1, memo) + fib_memo(n-2, memo)
    return memo[n]

# Function to time execution
def time_function(func, n, *args):
    start_time = time.time()
    result = func(n, *args)
    end_time = time.time()
    return end_time - start_time

# Generate timing data
n_values = range(36)  # 0 to 35
recursive_times = []
memoized_times = []

for n in n_values:
    # Time recursive version
    recursive_time = time_function(fib_recursive, n)
    recursive_times.append(recursive_time)
    
    # Time memoized version
    memoized_time = time_function(fib_memo, n, {})
    memoized_times.append(memoized_time)
    
# Create linear plot
plt.figure(figsize=(10, 6))
plt.plot(n_values, recursive_times, 'b-', label='Recursive')
plt.plot(n_values, memoized_times, 'r-', label='Memoized')
plt.xlabel('n')
plt.ylabel('Time (seconds)')
plt.title('Fibonacci Calculation Time vs n (Linear Scale)')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.1.jpg')
plt.close()

# Create logarithmic plot
plt.figure(figsize=(10, 6))
plt.semilogy(n_values, recursive_times, 'b-', label='Recursive')
plt.semilogy(n_values, memoized_times, 'r-', label='Memoized')
plt.xlabel('n')
plt.ylabel('Time (seconds) - Log Scale')
plt.title('Fibonacci Calculation Time vs n (Logarithmic Scale)')
plt.legend()
plt.grid(True)
plt.savefig('ex1.6.2.jpg')
plt.close()

