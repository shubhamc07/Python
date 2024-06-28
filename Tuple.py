# tuples are  ordered, unchangeable, and allow duplicate values
tuple1 =("apple", "banana", "cherry", "orange", "kiwi", "melon", "mango")
# print(type(tuple1))

# accessing specific index
# print(tuple1[1])
# print(tuple1[-1])

# slicing in tuple
# print(tuple1[2:5])

# to check item is present in tuple
# if "apple" in tuple1:
#   print("Yes, 'apple' is in the fruits tuple")

# Convert the tuple into a list to be able to change it
# li_tuple = list(tuple1)
# li_tuple[0]="coconut"
# tuple1 = tuple(li_tuple)
# print(tuple1)

#  Adding tuple to a tuple
# tuple2 = ("apple", "banana", "cherry")
# y = ("orange",)
# tuple2 += y
# print(tuple2)

# The del keyword can delete the tuple completely:
# tuple2 = ("apple", "banana", "cherry")
# del tuple2
# print(tuple2)

# unpacking tuples

# When we create a tuple, we normally assign values to it. This is called "packing" a tuple:
# But, in Python, we are also allowed to extract the values back into variables. This is called "unpacking"
# fruits = ("apple", "banana", "cherry")
# (green, yellow, red) = fruits
# print(green)
# print(yellow)
# print(red)

# Using Asterisk*
# Assign the rest of the values as a list called "red"
# the apple will assign to green and banana will assign to yellow and rest will assign to *red and it will return list in red
# fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
# (green, yellow, *red) = fruits
# print(green)
# print(yellow)
# print(red)

# the loops and joining to tuple is same as list 

