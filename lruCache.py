from functools import lru_cache
import time

def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)

def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n - 1)


start_time = time.perf_counter()
print(factorial(30))
end_time = time.perf_counter()
print(f"The execution time: {end_time - start_time:.8f} seconds")