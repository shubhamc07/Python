# ex 1
# duck typing

# class Duck:
#     def swim(self):
#         print("Duck can swim")
#     def speaks(self):
#         print("Quack")

# class Dog:
#     def swim(self):
#         print("Dog can swim")
#     def speaks(self):
#         print("woof")

# def display(para):
#     para.swim()
#     para.speaks()
#     print("Info displayed")

# d= Duck()
# dog = Dog()
# display(dog)

# ex 2
# operator overloading
# print( 1 + 2)
# print( 1.5 + 2.5)
# print( "1" + "2")
# print("shubham" + "chavan")

# class Person:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def __gt__(self,other):
#         if self.age > other.age :
#             return True
#         else:
#             return False

# p1 =Person("shubham",23)
# p2 = Person("Aditya",33)
# if p1>p2:
#     print(f"{p1.name} will pay the bill")
# else:
#     print(f"{p2.name} will pay the bill")

# Method Overloading
# python by default does not support method overloading but we achive this by default method
class Demo:
    # using default argument
    # def add(self,a,b,c=0):
    #     return a+b+c

    # def add(self,a,b,c):
    #     return a + b + c

    # using *args
    def add(self,*args):
        total = 0
        for i in args:
            total =  total + i
        return total

# d = Demo()
# print(d.add(5,6))
# print(d.add(5,6,7))

# method overriding
class Father:
    def sleep(self):
        print("sleeps from 10.00 pm to 5.00 am")
    def eat(self):
        print("eating")

class Son(Father):
    def sleep(self):
        print("sleeps from 2.00 am to 10.00 pm")

s1= Son()
s1.sleep()
