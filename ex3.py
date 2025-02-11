import timeit
import cProfile

def sub_function(n):
    # sub function that calculates the factorial of n
    if n == 0:
        return 1
    else:
        return n * sub_function(n-1)
    
def test_function():
    data = []
    for i in range(10):
        data.append(sub_function(i))
    return data

def third_function():
    # third function that calculates the square of the number from 0 to 999
    return[i**2 for i in range(100000000)]

cProfile.run('test_function()')
cProfile.run('third_function()')

# 1. A profiler is a tool that analyzes how long various parts of the program take to execute. It measures the time it takes for different parts to complete.

# 2. Profiling measures the times of each part of the code as well as how many calls were made, total time, total time per call, cumulative time, and cumulative time per primitive call. Benchmarking measures the time for the entire code without extra details.

# 4. Execution time is displayed next to the total amount of calls.
# 
# This was our output:
#          69 function calls (24 primitive calls) in 0.000 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 ex3.py:11(test_function)
#     55/10    0.000    0.000    0.000    0.000 ex3.py:4(sub_function)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#        10    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 


#          4 function calls in 18.741 seconds

#    Ordered by: standard name

#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    1.666    1.666   18.740   18.740 <string>:1(<module>)
#         1   17.074   17.074   17.074   17.074 ex3.py:17(third_function)
#         1    0.000    0.000   18.741   18.741 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects} 
