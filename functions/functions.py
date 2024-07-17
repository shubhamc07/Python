# ex 1
# function to return square of num
# def square(num):
#     square_of_num = num ** 2
#     return square_of_num

# num = int(input("enter a number: "))
# result = square(num)
# print("The square of given number is",result)

# ex 2
# function to find sum of two numbers

# def add(num1,num2):
#     sum = num1 + num2
#     return sum

# num1 = int(input("Enter num1: "))
# num2 = int(input("Enter num2: "))

# result = add(num1,num2)
# print("sum of two numbers is",result)

# ex 3
# table of a number

# def table(num):
#     for i in range(1,11):
#         table = num * i
#         print(table)

# num = 5
# print(table(5))

# ex 4
# function with default parameter
# def greet(name="user"):
#     return "Hello " + name + "!"

# print(greet("shubham"))

# ex 5
# lambda function to find cube of number
# cube = lambda x : x ** 3
# print(cube(3))

# ex 6
# function with *args
# def sum_all(*args):
#     for i in args:
#         print(i * 2)
#     return sum(args)

# print(sum_all(2,5,6))
# print(sum_all(2,5,6,6,8,9))

# ex 7
# function with **kwargs
# def print_kwargs(**kwargs):
#     for key, value in kwargs.items():
#         print(f"{key}:{value}")

# print_kwargs(name="shubham" , id ="01")
# print_kwargs(name="raj" , id ="02")



#  function with multiple return values

# def hello():
#     return 2+4 , 5+6

# print(hello())