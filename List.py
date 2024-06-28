fruits = ["mango","apple","watermelon","orange","coconut","kiwi"]

# indexing in list
# first_fruit = fruits[0]
# print(first_fruit)
# last_fruit = fruits[-1]
# print(last_fruit)

# slicing in list
# slice_fruit = fruits[0:4]
# slice_fruit = fruits[0:4:2]
# slice_fruit = fruits[0::2]
# slice_fruit = fruits[0:-2]
# print(slice_fruit)

# updating list on specific index
# fruits[4]="mango"
# print(fruits[4])

# updating list using slicing
# fruits[1:2]=["kiwi"]
# fruits[1:3]=["greps","chiku"]
# print(fruits)


# adding new items in list

# using insert method
# fruits.insert(2, "banana")

# using append method
# fruits.append("jamun")

# we can add list,tuple,set,dict to list using extend method
# tropical = ["mango", "pineapple", "papaya"]
# fruits.extend(tropical)


# removing items from list

# using remove method if their are same items in list remove method will remove first matching item
# fruits.remove("mango")

# using pop method 
# we can pass specific index to pop 
# if we do not pass any index the pop method will remove last item in list
# fruits.pop(1)
# fruits.pop()

# using The del keyword also removes the specified index
# del fruits[0]
# The del keyword can also delete the list completely.
# del fruits

# using clear() The clear() method empties the list.
# The list still remains, but it has no content.
# fruits.clear()
# print(fruits) 

# looping through list

# using for loop 
# for fruit in fruits:
#     print(fruit)
# shorthand for loop
# [print(x) for x in fruits]

# using range() and len() with for loop to loop through the index
# for i in range(len(fruits)):
#     print(fruits[i])

# using while loop and len()
# i= 0
# while i<len(fruits):
#     print(fruits[i])
#     i = i + 1

# List Comprehension

# newlist = []
# for x in fruits:
#   if "a" in x:
#     newlist.append(x)
# print(newlist)

# shorthand for loop
# newlist = [x.upper() for x in fruits]
# print(newlist)

# sorting the list
# List objects have a sort() method that will sort the list alphanumerically, ascending, by default
# By default the sort() method is case sensitive, resulting in all capital letters being sorted before lower case letters:

# fruits.sort()
# print(fruits)

num_list = [22,44,88,11,66,55,77]
# num_list.sort()

# o sort descending, use the keyword argument reverse = True
# num_list.sort(reverse=True)
# print(num_list)

# to reverse the list use reverse()
# num_list.reverse()
# print(num_list)

# copying a list
# You cannot copy a list simply by typing list2 = list1,
# because: list2 will only be a reference to list1, and changes made in list1 will automatically also be made in list2

# using copy() method
# nums = num_list.copy()

# using list() method
# nums = list(num_list)
# print(nums)

# Join Two Lists

# method 1
# list1 = ["a", "b", "c"]
# list2 = [1, 2, 3,4]
# list3 = list1 + list2

# list1 = list2

# method 2 using for loop
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# for x in list2:
#   list1.append(x)

# print(list1)

# method 3 using extend()
# list1 = ["a", "b" , "c"]
# list2 = [1, 2, 3]

# list1.extend(list2)
# print(list1)

