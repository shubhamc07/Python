dict1={
    "name":"shubham",
    "age" : 23,
    "id":1
}

l1 = list(dict1.items())

l2 = [{"a":1,"b":2},{"c":3,"d":4}]
set_list= set(l2[0].items())
# print(set_list)
# print(l2)


my_dict = {'a': 1, 'b': 2, 'c': 3}

# Convert dictionary to list of tuples
my_list = list(my_dict.items())

# print(my_list)

list_dict = [{"id":1,"name":"shubham","lname":"chavan"},{"id":2,"name":"raj","lname":"mohite"}]
# adding new element
list_dict[0]["marks"]=95
list_dict[1]["marks"]=90
# removing element
del list_dict[0]["marks"]
del list_dict[1]["marks"]
# appending new dict
list_dict.append({"id":3,"name":"vansh","lname":"mohite"})
# changing the datatype of specific index
dict_set = set(list_dict[2].items())
# print(list_dict)
# print(dict_set)

list3=[{"id":1,"name":"shubham","lname":"chavan"}]
dict5 = dict(list3[0])
print(dict5)
# list3_set = set(list3)
# print(list3_set)

dict3 ={
    "id1":{
        "id":1,
    "name":"shubham"
    },
    "id2":{
        "id":2,
    "name":"shubham"
    }
}

# print(dict3)
# set_dict = set(dict3.items())
# print(set_dict)\
a = ("name",)
print(type(a))
name="shubham"
age=23
# print(f"my name is {name} and my age is {age} ")
