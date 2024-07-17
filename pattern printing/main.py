# ex 1
#     *
#    **
#   ***
#  ****
# *****

# rows = 5

# for i in range(0, rows):
#     for j in range(0, rows - i - 1):
#         print(' ', end='')
#     for j in range(0, i + 1):
#         print('*', end='')
#     print()

# ex 2
#     1
#    22
#   333
#  4444
# 55555

# rows = 5

# for i in range(0, rows):

#     for j in range(0, rows - i - 1):
#         print(' ', end='')

#     for j in range(0, i + 1):
#         print(i + 1, end='')

#     print()

# ex 3
# *****
#  ****
#   ***
#    **
#     *

# rows = 5

# for i in range(rows, 0, -1):
#     for j in range(0, rows - i):
#         print(' ', end='')

#     for j in range(0, i):
#         print('*', end='')

#     print()

# ex 4
#           1 
#         1 2 
#       1 2 3 
#     1 2 3 4 
#   1 2 3 4 5

# rows = 6
# for i in range(1, rows):
#     num = 1
#     for j in range(rows, 0, -1):
#         if j > i:
#             print(" ", end=' ')
#         else:
#             print(num, end=' ')
#             num += 1
#     print("")

# ex 5
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

# rows = 5
# for i in range(rows + 1, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print(" ")

# ex 6
# * 
# * * 
# * * * 
# * * * * 
# * * * * * 
# * * * * 
# * * * 
# * * 
# * 

# rows = 5
# for i in range(0, rows):
#     for j in range(0, i + 1):
#         print("*", end=' ')
#     print("\r")

# for i in range(rows, 0, -1):
#     for j in range(0, i - 1):
#         print("*", end=' ')
#     print("\r")

# ex 7
# * * * * * 
#   * * * *
#     * * *
#       * *
#         *

# rows = 5
# i = rows
# while i >= 1:
#     j = rows
#     while j > i:
#         print(' ', end=' ')
#         j -= 1
#     k = 1
#     while k <= i:
#         print('*', end=' ')
#         k += 1
#     print()
    # i -= 1

 # ex 8
# rows = 10
# for i in range(1, rows + 1):
#     for j in range(i):
#         print("*", end=" ")
#     print()

# ex 9
# 1
# 3 2
# 6 5 4
# 10 9 8 7

# num = 1
# for i in range(1, 5):
#     if i % 2 != 0:
#         for j in range(1,i+1):
#             print(num,end=' ')
#             num += 1
#     else:
#         s = num + i - 1
#         for j in range(i):
#             print(s,end=" ")
#             s -= 1
#         num += i
#     print()

num=1
for i in range(4):
    line=''
    for j in range(i+1):
        line =f"{num} {line}"
        num+=1
    print(line);


