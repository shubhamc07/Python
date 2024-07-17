import re

# ex1
# pattern = re.compile("[a-z]+")
# print(pattern.search("hello"))
# print(pattern.search("Hello"))
# print(pattern.search("HELLO"))

# re.match
# pattern = re.compile("[a-z]+")
# print(pattern.match("hello"))
# print(pattern.match("hEllo"))
# print(pattern.match("HELLO"))



# methods for searching 
# findall - return a list containing all matches
# search - return a match object in it anywhere in the string
# split - 	Returns a list where the string has been split at each match
# sub - Replaces one or many matches with a string
# start - give the starting index
# end - ending index of first match
# span - start and end 
# string - give the data 

text = "The quick brown fox jumps over the lazy dog."
# ex2
# pattern =  r"dog"
# matches = re.findall(pattern,text)
# print(matches)

# ex 3
# pattern  = r'[aeiou]'
# matches = re.findall(pattern,text)
# print(matches)

# ex 4
# pattern  = r"^The.*dog.$"
# matches = re.search(pattern,text)
# print(matches)

# ex 5
# pattern = '^a...s$'
# test_str = 'abyss'
# result = re.match(pattern, test_str)

# if result:
#   print("Search successful.")
# else:
#   print("Search unsuccessful.")

# ex6
# to find how many times o is there in str
# res = len(re.findall("o+",text))
# print(res)

# ex 7
# res = re.split("fox",text)
# print(res)

# ex 8
# there is also a third parameter in sub which is count in which we can give the count of how many matches we want to replace
# res = re.sub("fox","tiger",text)
# print(res)

# ex 9
# with file handling
with open("11-04-2024/text.txt","r+") as file:
    data = file.read()
    # res = re.split("\.",data)
    # data = file.readline()
    # res = re.search("^As.*quietude.$",data)
    # data = file.read()
    # res = re.findall("the",data)
    res = re.sub("sun","moon",data)
    # res = re.match("sun",data)
    print(res)