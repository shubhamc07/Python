# A set is a collection which is unordered, unchangeable*, and unindexed.
# note* :Set items are unchangeable, but you can remove items and add new items.
# Sets are written with curly brackets.
# Set items are unordered, unchangeable, and do not allow duplicate values.

# set1 = {"apple", "banana", "cherry"}
# print(set1)

# Duplicate values will be ignored:
# set1 = {"apple", "banana", "cherry", "apple"}
# print(set1)

# True and 1 and False and 0 is considered the same value
# set1 = {"apple", "banana", "cherry", 0,False,True, 1, 2}
# print(set1)


# add items to set 

# using add()
# set1 = {"apple", "banana", "cherry"}
# set1.add("orange")
# print(set1)

# using update()
# The object in the update() method does not have to be a set, it can be any iterable object (tuples, lists, dictionaries etc.).
# set1 = {"apple", "banana", "cherry"}
# tropical = {"pineapple", "mango", "papaya"}
# set1.update(tropical)
# print(set1)

# remove items from set

# using remove()
# If the item to remove does not exist, remove() will raise an error.
# set1 = {"apple", "banana", "cherry"}
# set1.remove("banana")
# print(set1)

# using discard()
# If the item to remove does not exist, discard() will NOT raise an error
# set1 = {"apple", "banana", "cherry"}
# set1.discard("banana")
# print(set1)

# we can also use pop() will remove random item,clear() clears the list and del() will delete the set completely

# looping through set using for loop
# set1 = {"apple", "banana", "cherry"}
# for x in set1:
#   print(x)

# joins in set

# There are several ways to join two or more sets in Python.
# The union() and update() methods joins all items from both sets.
# The intersection() method keeps ONLY the duplicates.
# The difference() method keeps the items from the first set that are not in the other set(s).
# The symmetric_difference() method keeps all items EXCEPT the duplicates.

# union()
# The union() method returns a new set with all items from both sets.will skip the duplicate values
# The union() method allows you to join a set with other data types, like lists or tuples.

# set1 = {"a", "b", "c",1}
# set2 = {1, 2, 3}
# set3 = set1.union(set2)
# print(set3)

# we can use the | operator instead of the union() method, and you will get the same result.
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = set1 | set2
# print(set3)

# joining multiple sets with the union() method
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1.union(set2, set3, set4)
# print(myset)

# When using the | operator, separate the sets with more | operators
# set1 = {"a", "b", "c"}
# set2 = {1, 2, 3}
# set3 = {"John", "Elena"}
# set4 = {"apple", "bananas", "cherry"}
# myset = set1 | set2 | set3 |set4
# print(myset)

# update()
# The update() method inserts all items from one set into another.
# The update() changes the original set, and does not return a new set.

# set1 = {"a", "b" , "c"}
# set2 = {1, 2, 3}
# set1.update(set2)
# print(set1)

# Intersection()
# Keep ONLY the duplicates
# The intersection() method will return a new set, that only contains the items that are present in both sets.

# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.intersection(set2)
# print(set3)

# we can use the & operator instead of the intersection() method, and you will get the same result.
# The & operator only allows you to join sets with sets, and not with other data types like you can with the intersecton() method.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 & set2
# print(set3)

# intersection_update()
# The intersection_update() method will also keep ONLY the duplicates, 
# but it will change the original set instead of returning a new set.

# difference()
# The difference() method will return a new set that will contain only the items from 
# the first set that are not present in the other set.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.difference(set2)
# print(set3)

# we can use the - operator instead of the difference() method, and you will get the same result.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 - set2
# print(set3)

# difference_update()
# The difference_update() method will also keep the items from the first set that are not in the other set, 
# but it will change the original set instead of returning a new set.

# symmetric_difference()
# The symmetric_difference() method will keep only the elements that are NOT present in both sets.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1.symmetric_difference(set2)
# print(set3)

# we can use the ^ operator instead of the symmetric_difference() method, and you will get the same result.
# set1 = {"apple", "banana", "cherry"}
# set2 = {"google", "microsoft", "apple"}
# set3 = set1 ^ set2
# print(set3)

