# Lambda Expression:
# Even odd find from list  numbers = [1,2,3,4,5,6,7,8,9,10]
#  square of this list
# Sorting tuples = [(1, 5), (2, 3), (3, 8), (4, 1)] Output: [(4, 1), (2, 3), (1, 5), (3, 8)]

# ex1
# find odd and even from the list
numbers = [1,2,3,4,5,6,7,8,9,10]
even =list(filter(lambda x: (x % 2 ==0),numbers))
odd =list(filter(lambda x: (x % 2 !=0),numbers))
print("Even numbers are:",even)
print("Odd numbers are:",odd)

# ex2
square = list(map(lambda x : x**2,numbers))
print("The square:",square)

# ex 3
tuples = [(1, 5), (2, 3), (3, 8), (4, 1)]
print(tuples)
sort = sorted(tuples,key=lambda x: x[1])
print(sort)

