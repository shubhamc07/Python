# Q1 find min and max number from list

l1 = [22,33,4,66,77,99,100,101,1]

# def minmax(list):
#     max_num = max(list)
#     min_num = min(list)
#     return max_num,min_num

# max_num,min_num = minmax(l1)
# print(max_num)
# print(min_num)
# print(minmax(l1))


# Q2 create a function to add,sub,mul,div two numbers

# def cal(num1,num2,ops):
#     num1 = float(num1)
#     num2 = float(num2)
    
#     if ops == "add":
#         result = num1 + num2
#     elif ops == "sub":
#         result = num1 - num2
#     elif ops == "mul":
#         result = num1 * num2
#     elif ops == "div":
#         if num2 != 0:
#             result = num1 / num2
#         else:
#             result = "Cannot devide by zero"
#     return result

# print(cal(5,5,"div"))

#  Q3.Write a Python program to count the number of vowels in a given string.

# def count_vowels(str):
#     vowels = "aeiouAEIOU"
#     count = sum(1 for char in str if char in vowels)
#     return count

# print(count_vowels("shubham"))


# Q4.Write a Python program to read a text file and count the number of words in it.

# def count_words_in_file(filename):
#     with open(filename,'r') as file:
#         text = file.read()
#     words = text.split()
#     return len(words)

# filename = "youtube.txt"
# word_count = count_words_in_file(filename)
# print(word_count)

# Q5.Write a Python program to merge two dictionaries.

# def Merge(dict1, dict2):
#     marge_dict = {**dict1,**dict2}
#     return marge_dict

# dict1 = {'a': 1, 'b': 2}
# dict2 = {'b': 3, 'c': 4}
# dict3 = Merge(dict1,dict2)

# print(dict3)


# Q6.Write a Python program to print the Fibonacci sequence up to a given number.

# def fib_sequence(num):
#     sequence = []
#     a,b = 0,1
#     while a <= num:
#         sequence.append(a)
#         a,b = b,a+b
#     return sequence


# print(fib_sequence(15))
        
        
# Q7.Write a Python function to check if a number is prime.

# def prime_num(num):
#     if num > 1:
#         for i in range(2, (num//2)+1):
#             if (num%i)==0:
#                 res = num ,"Not a prime number"
#                 break
#         else:
#             res = num ,"Number is prime number"
#     else:
#         res = num ,"number is not prime"
#     return res

# print(prime_num(4))


# Q8.Write a Python program to handle division by zero using exception handling.

# def safe_div(num1,num2):
#     try:
#         res = num1/num2
#     except ZeroDivisionError as e:
#         res = e
#     return res

# num1 = 10
# num2 = 9

# print(safe_div(num1,num2))



# Q9.Write a Python function to calculate the factorial of a number.

# def fact(num):
#     if num == 0:
#         return 1
#     else:
#         return num*fact(num-1)
    
# print(fact(5))



# Q10.Write a Python program to check if a given string is a palindrome.
    
# def check_palindrome(str):
#     clean_str = ''.join(char.lower() for char in str if char.isalnum())
#     return clean_str == clean_str[::-1]

# print(check_palindrome("A man, a plan, a canal, Panama"))


# Q.11 Write a Python program using list comprehensions to find all the even numbers in a list.

list = [1,2,3,4,5,6,7,8,9,10]
# even_num = [num for num in list if num % 2 == 0]
# odd_num = [num for num in list if num % 2 != 0]
# print(even_num)
# print(odd_num)



def odd_even(nums):
    odd = []
    even =[]
    for num in nums:
        if num % 2== 0:
            even.append(num)
        else:
            odd.append(num)
    return even,odd

even,odd = odd_even([1,2,3,4,5,6,7,8,9,10])
print(odd)
print(even)
            
        

# Q12.Write a Python program using dictionary comprehensions to create a dictionary with keys as numbers from 1 to 5 and values as their squares.

# sqr = {num: num**2 for num in range(1,6)}
# print(sqr)


# Q13. Write a Python program to merge two lists and sort the resulting list.

# l1 = [1,3,5]
# l2 = [2,4,6]
# l3 = sorted(l1 + l2)
# print(l3)


# Q14.Write a Python program to reverse a string.

# def reverse_str(str):
#     return str[::-1]

# print(reverse_str('apple'))



# Q15. Write a Python program to count the number of each character in a string.

# def char_ouccrance(str):
#     char_count = {}
#     for char in str:
#         if char != ' ':
#             if char in char_count:
#                 char_count[char] += 1
#             else:
#                 char_count[char] = 1
#     return char_count

# print(char_ouccrance("A a A a"))


# Q16. Write a Python program to remove duplicates from a list.

# def remove_dups(nums):
#     return list(set(nums))

# l1=[1,2,2,1,3,4]
# print(remove_dups(l1))


# Q17.Write a Python program to calculate the sum of the digits of a number.

# def sum_of_digit(num):
#      return sum(int(digit) for digit in str(num))


# num = 12345
# print(sum_of_digit(num))


# Q18.Write a Python program to convert Celsius to Fahrenheit.

# def Celsius_to_Fahrenheit(Celsius):
#     return (Celsius * 9/5)+32


# celsius = 25
# fahrenheit = Celsius_to_Fahrenheit(celsius)
# print(f"{celsius}°C is {fahrenheit}°F")


