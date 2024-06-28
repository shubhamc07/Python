# Dictionaries are used to store data values in key:value pairs.
# A dictionary is a collection which is ordered*, changeable and do not allow duplicates.

# Dictionary items are ordered, changeable, and do not allow duplicates.
# Dictionary items are presented in key:value pairs, and can be referred to by using the key name.
# dict1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964
# }
# print(dict1["brand"])

# Dictionaries cannot have two items with the same key
# Duplicate values will overwrite existing values
# dict1 = {
#   "brand": "Ford",
#   "model": "Mustang",
#   "year": 1964,
#   "year": 2020
# }
# print(dict1)

# accessing Items in dict

# Get the value of the key
dict1 = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

# del dict1["brand"]
print(dict1)
# x = dict1["model"]
# print(x)

# There is also a method called get() that will give you the same result
# x = dict1.get("model")

# keys()
# The keys() method will return a list of all the keys in the dictionary
# x = dict1.keys()
# print(x)

# car = {
# "brand": "Ford",
# "model": "Mustang",
# "year": 1964
# }
# x = car.keys()
# print(x) #before the change
# car["color"] = "white"
# print(x) #after the change

# values()
# The values() method will return a list of all the values in the dictionary.
# x = dict1.values()
# print(x)

# items()
# The items() method will return each item in a dictionary, as tuples in a list.
# x = dict1.items()
# print(x)

