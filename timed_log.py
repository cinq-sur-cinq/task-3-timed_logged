from functools import wraps 
import time

def timed_logged (func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        try:
            result = func(*args,**kwargs)
        except Exception as error: 
            end_time= time.perf_counter()
            elapsed_ms = (end_time- start_time) * 1000
            #logging the erro like this?
            
            print(f"function: {func.__name__}")
            print(f"docs: {func.__doc__}") #adding docs
            print(f"args: args={args}, kwargs={kwargs}")
            print(f"exception type: {type(error).__name__}")
            print(f"exception message:  {error}")
            print(f"execution time: {elapsed_ms:.3f} ms")
            raise
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000

        print(f"function: {func.__name__}")
        print(f"docs: {func.__doc__}") #adding docs
        print(f"args: args={args}, kwargs={kwargs}")
        print(f"result: {result}")
        print(f"execution time: {elapsed_ms:.3f} ms")
        return result
    return wrapper

#test 1
@timed_logged
def slow_sum(a, b, delay=0.5):
    """add two nums after a delay."""
    import time
    time.sleep(delay)
    return a + b


answer = slow_sum(1, 2, delay=0.2)

print("Answer:", answer)
print("Name:", slow_sum.__name__)
print("Documentation:", slow_sum.__doc__)

#test2
@timed_logged
def divide(a, b):
    """ testing doc """
    return a / b


try:
    divide(10, 0)
except ZeroDivisionError:
    print("exception was logged.")