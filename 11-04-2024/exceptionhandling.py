# ex1

# try:
#     num = int(input("Enter a number: "))
#     l1 = [5,8,9]
#     print(l1[num])
# except ValueError:
#     print("Enter a valid number")
# except IndexError:
#     print("index error")

# ex2
# try:
#     num1 = int(input("Enter number1: "))
#     num2 = int(input("Enter number2: "))
#     res = num1 / num2
#     print(res)
# except ZeroDivisionError as e:
#     print(e)
# finally:
#     print(" i will work always")

# ex3
# try:
#     f = open("11-04-2024/text.txt","w")
#     try:
#         f.write("Shubham chavan")
#     except:
#         print("not able write in this file")
#     finally:
#         f.close()
# except:
#     print("unable to open file")

# ex4
# raise keyword
# num = int(input("Enter a number : "))

# if num < 10:
#     raise Exception("Cannot enter number below ten")

# s = "hello"
# if not type(s) is int:
#     raise TypeError("Enter a valid number")

# ex 5
# creating custom exceptions
# class AgeError(Exception):
#     "Raised when persons age is below 18"
#     pass

# try:
#     age = int(input("Enter your age: "))
#     if(age<18):
#         raise AgeError
# except AgeError:
#     print("you are not eligible to vote")
# else:
#     print("you are eligible to vote")
# finally:
#     print("Thank you")


# ex6
# try:
#     f  = open("file.txt","r")
#     data = f.read()
# except FileNotFoundError as e:
#     print("Error:",e)
