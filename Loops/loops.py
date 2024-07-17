# ex1
# count positive numbers

# numbers = [1,-2,3,-4,5,6,-7,-8,9,10]
# positive_number_count = 0

# for num in numbers:
#     if num > 0:
#         positive_number_count += 1
# print("The count of positive numbers in list is",positive_number_count)

# ex2
# count of all even number till given number
# number = int(input("Enter a number: "))
# even_numbers = 0

# for i in range(1,number+1):
#     if i%2 == 0:
#         even_numbers += 1

# print("even numbers till number:",even_numbers)

# ex3
# multiplication table of given number
# number = int(input("Enter a number: "))

# for i in range(1,11):
#     table = number * i
#     print(table)

# ex4
# reverse a string using loop 
# input_str = input("Enter a string: ")
# reversed_str =""

# for char in input_str:
#     reversed_str = char +  reversed_str

# print(reversed_str)

# ex5
# find first non repeated char in str
# sample_str = "abababacd"

# for char in sample_str:
#     if sample_str.count(char) == 1:
#         print("first non repeated char is",char)
#         break

# ex 6
# factorial using while loop
# num = int(input("Enter a number: "))
# fact = 1

# while num > 0:
#     fact *= num
#     num -= 1

# print("the factorial value of given number is:",fact)

# ex 7 
# take input from user until user enter number bet 1-10
# while True:
#     num = int(input("Enter value bet 1-10: "))
#     if 1<= num <= 10:
#         print("Thanks")
#         break
#     else:
#         print("invalid input,try again")

# ex 8
# prime number checker
# num = int(input("Enter a number to check: "))
# is_prime = True

# if num > 1:
#     for i in range(2,num):
#         if (num%i) == 0:
#             is_prime = False
#             break
# print(is_prime)

# ex 9
# find duplicate value in list

# fruits = ["apple","banana","orange","apple","mango"]

# unique_item = set()

# for fruit in fruits:
#     if fruit in unique_item:
#         print("Duplicate fruit is",fruit)
#         break
#     unique_item.add(fruit)


# pattern 1
# *****
# ***
# *
# *
# ***
# *****

# for i in range(0,6):
#     if i<3:
#         for j in range(0,5-(i+i)):
#             print("*",end="")
#         print()
#     else:
#         for j in range(0,(i+i)-5):
#             print("*",end="")
#         print()



#  pattern 2
# *****
# *   *
# *  *
# * *
# **

# for i in range(0,5):
#     for j in range(0,6-i):
#         if (i>0) & (j>0) & (j<(6-i)-1):
#             print(" ",end="")
#         else:
#             print("*",end="")
#     print()


