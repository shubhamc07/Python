# r mode reading the file and r mode is default mode
# w mode for writing the file and can create a new file 
# a mode for appending at the end of the file without looseing the exisiting data in the file
# x mode create new and gives error the file is already present
# rt for text file 
# rb for binary file for img jpg pdf and etc
# r+ for and read and write the file
# w+ for write and read a file but it remove the existing 
# a+ To append and read data from the file

# reading a file
# f= open("file handling/hello.txt",'r')
# # print(f)
# text = f.read()
# print(text)
# f.close()

# writing to a file
# f= open("file handling/hello.txt",'w')
# f.write('Hello,Chavan')
# f.close()

# appending to the file
# f= open("file handling/hello.txt",'a')
# f.write('Hello,Chavan')
# f.close()

# when we use with statement the file will close automatically
# with open("file handling/hello.txt",'w') as f:
#     f.write("inside the file")

# with open("file handling/hello.txt",'r') as f:
#     i = 0
#     while True:
#         i += 1
#         line = f.readline()
#         if not line:
#             break
#         m1=line.split(",")[0]
#         m2=line.split(",")[1]
#         m3=line.split(",")[2]
#         print(f"Marks of student {i} in english is:{m1}")
#         print(f"Marks of student {i} in math is:{m2}")
#         print(f"Marks of student {i} in python is:{m3}")

# f = open("file handling/text.txt","w")
# lines = ['line 1\n','line 2\n','line 3\n']
# f.writelines(lines)
# f.close()

