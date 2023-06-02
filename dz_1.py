import concurrent.futures
import math
import time

def factorial(n):
    return math.factorial(n)

def calculate_factorial_with_threadpool(n):
    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = [executor.submit(factorial, i) for i in range(1, n+1)]
        return [result.result() for result in results]

def calculate_factorial_with_processpool(n):
    with concurrent.futures.ProcessPoolExecutor() as executor:
        results = [executor.submit(factorial, i) for i in range(1, n+1)]
        return [result.result() for result in results]

def main():
    n = 10


    start_time = time.time()
    results_threadpool = calculate_factorial_with_threadpool(n)
    end_time = time.time()
    execution_time_threadpool = end_time - start_time


    start_time = time.time()
    results_processpool = calculate_factorial_with_processpool(n)
    end_time = time.time()
    execution_time_processpool = end_time - start_time


    if execution_time_threadpool < execution_time_processpool:
        fastest_method = "ThreadPoolExecutor"
        fastest_time = execution_time_threadpool
    else:
        fastest_method = "ProcessPoolExecutor"
        fastest_time = execution_time_processpool


    print(f"Час виконання за допомогою ThreadPoolExecutor: {execution_time_threadpool} сек.")
    print(f"Час виконання за допомогою ProcessPoolExecutor: {execution_time_processpool} сек.")
    print(f"Найоптимальніший метод: {fastest_method} (Час: {fastest_time} сек.)")

if __name__ == '__main__':
    main()
