import time

def my_decorator(func):
    def wrapper(arg):
        print("Start")
        start_time = time.perf_counter_ns()
        print('Log init value:', arg)
        res = func(arg)
        middle_time = time.perf_counter_ns() - start_time
        print(f"Time: {middle_time} наносекунд")
        print(f"Log result = {res}")
        print("End")
        print(f'\nСон на 1 секунду\n')
        time.sleep(1)
        print(f"Time: {time.perf_counter_ns() - middle_time} наносекунд")
        return res
    return wrapper

@my_decorator
def my_func(arg):
    return arg + 5

print(f"Result: {my_func(10)}")