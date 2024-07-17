# ex 1
# import time

# def timer(func):
#     def wrapper(*args,**kwargs):
#         start = time.time()
#         result = func(*args,**kwargs)
#         end = time.time()
#         print(f"{func.__name__} ran in  {end-start} time")
#         return result
#     return wrapper

# @timer
# def example_function(n):
#     time.sleep(n)

# example_function(2)

# ex 2
# def debug(func):
#     def wrapper(*args,**kwargs):
#         args_value = ', '.join(str(arg) for arg in args)
#         kwargs_value = ', '.join(f"{k}:{v}" for k, v in kwargs.items())
#         print(f"calling: {func.__name__} with args {args_value} with kwargs {kwargs_value}")
#         return func(*args,**kwargs)
#     return wrapper

# @debug
# def greet(name,greeting="Hello"):
#     print(f"{greeting}, {name}")

# greet('shubham',greeting="namste")

# ex 3
# import time

# def cache(func):
#     cache_value= {}
#     def wrapper(*args):
#         if args in cache_value:
#             return cache_value[args]
#         result = func(*args)
#         cache_value[args] =  result
#         return result
#     return wrapper

# @cache
# def long_running_function(a,b):
#     time.sleep(4)
#     return a + b

# print(long_running_function(5,5))
# print(long_running_function(5,5))
# print(long_running_function(5,3))

def greet(func):
    def func1():
        print("Good Morning")
        func()
    return func1()


@greet
def hello():
    print("Hello shubham")

    