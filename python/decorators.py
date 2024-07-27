import time

def time_it(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Record the start time
        result = func(*args, **kwargs)  # Call the original function
        print(result)
        end_time = time.time()  # Record the end time
        duration = end_time - start_time  # Calculate the duration
        print(f"Function '{func.__name__}' executed in {duration:.4f} seconds")
        return result  # Return the result of the original function
    return wrapper  # Return the wrapper function

@time_it
def slow_function(seconds):
    time.sleep(seconds)  # Simulate a slow operation
    return "Done!"

# Call the decorated function
result = slow_function(2)

