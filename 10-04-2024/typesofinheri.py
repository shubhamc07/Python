# there are five types of inheritance in python 
# 1.single inheritance
# 2.multiple inheritance
# 3.multilevel inheritance
# 4.hierarchical inheritance
# 5.hybrid inheritance

# 1.single inheritance
# ex
# class Parent:
#     def func1(self):
#         print("parent class")

# class Child(Parent):
#     def func2(self):
#         print("child class")

# obj = Child()
# obj.func1()
# obj.func2()

# 2.multiple inheritance
# ex
# class Add:
#     def add(self,num1,num2):
#         return num1 + num2

# class Sub:
#     def sub(self,num1,num2):
#         return num1 - num2
    
# class Cal(Add,Sub):
#     def cal(self):
#         return f"the results:"
    
# obj1 = Cal()
# print(obj1.cal())
# print(obj1.add(5,5))
# print(obj1.sub(5,5))


# 3.multilevel inheritance
# ex

# class Grandfather:
#     def __init__(self,grandfathername):
#         self.grandfathername = grandfathername

# class Father(Grandfather):
#     def __init__(self,fathername,grandfathername):
#         self.fathername = fathername
#         Grandfather.__init__(self,grandfathername)

# class Son(Father):
#     def __init__(self, sonname , fathername, grandfathername):
#         self.sonname = sonname
#         Father.__init__(self,fathername, grandfathername)

#     def print_name(self):
#         print("Grandfather name :", self.grandfathername)
#         print("Father name :", self.fathername)
#         print("Son name :", self.sonname)

# names = Son("Shubham","Tuakaram","Paraji")
# print(names.grandfathername)
# names.print_name()

# 4.hierarchical inheritance
# ex
# class Parent:
#     def func1(self):
#         print("parent class")

# class Child1(Parent):
#     def func2(self):
#         print("child 1.")

# class Child2(Parent):
#     def func3(self):
#         print("child 2.")

# obj1 = Child1()
# obj2 = Child2()
# obj1.func1()
# obj1.func2()
# obj2.func1()
# obj2.func3()

# 5.hybrid inheritance
# ex
# class School:
#     def func1(self):
#         print("School")

# class Teacher(School):
#     def func2(self):
#         print("teacher")

# class Student1(School):
#     def func3(self):
#         print("student1")

# class Student2(Teacher , School):
#     def func4(self):
#         print("student2")

# obj = Student2()
# obj.func1()
# obj.func2()

class India:
    def cap(self):
        print("Delhi")
class Usa:
    def cap(self):
        print("wash")

obj1 = India()
obj2 = Usa()

for i in (obj1,obj2):
    i.cap()


 