# ex1
# age group categorization
age = int(input("Enter Your Age: "))
if age < 13:
    print("The user is child")
elif age < 20:
    print("The user is teenager")
elif age < 60 :
    print("The user ia adult")
else:
    print("The user is senior citizen")

# ex2
# to find which no is greater
# num1=55
# num2=88

# if  num1 > num2:
#     print("num1 is grater")
# else:
#     print("num2 is grater")


# ex3
# movie ticket pricing
# age = 18
# day = "Wednesday"

# price = 100 if age >= 18 else 50
# # print(price)

# if day == "Wednesday":
#     price =  price - 20
# print("Movie Ticket Price is Rs.",price)

# ex4
# Grade Calculator
# student_marks = int(input("Enter Student Marks: "))
# if student_marks >= 101:
#     print("Enter Your Marks Correctly")
#     exit()

# if student_marks >= 90 :
#     grade = "A"
# elif student_marks>=80:
#     grade = "B"
# elif student_marks>=70:
#     grade = "C"
# elif student_marks>=60:
#     grade = "D"
# else:
#     grade = "F"

# print("Grade: ",grade)

# ex 5
# fruit ripeness checker

# fruit = "Banana"
# color = "Green"

# if fruit == "Banana":
#     if color == "Green":
#         print("Unripe")
#     elif color == "Yellow":
#         print("Ripe")
#     elif color == "Brown":
#         print("Overripe")

# ex 6
# weather activity suggestion
# weather = input("Enter weather in your area: ")
# lower_weather = weather.lower()

# if lower_weather == "sunny":
#     print("Go for walk")
# elif lower_weather == "rainy":
#     print("Read a book")
# elif lower_weather == "windy":
#     print("Take a nap")

# ex 7
# transportation mode selection
# distance = int(input("Enter Distance you want to travel: "))

# if distance < 3 :
#     mode = "walk"
# elif distance <= 15:
#     mode = "bike"
# else:
#     mode = "car"
# print("Your mode of transportation is",mode)

# ex 8
# coffee customization
# coffee_size = input("Enter the size of coffee you want to order large/small/medium: ")
# extra_sugar = input("Enter if you want extra sugar y/n: ")

# if extra_sugar == "y":
#     coffee = coffee_size + " coffee with extra sugar"
# else:
#     coffee = coffee_size + " coffee"

# print("You have ordered",coffee)

# ex 9
# password strength checker

# password = input("Enter your password: ")
# password_length = len(password)
# # print(password_length)
# if password_length < 6 :
#     strength = "Weak"
# elif password_length <=10:
#     strength ="Medium"
# else:
#     strength="Strong"

# print("your password strength is",strength)

# ex 10
# leap year checker
# year = int(input("Enter year: "))

# if (year % 400 == 0) or (year % 4 == 0 and year % 100 != 0):
#     print("Its a leap year")
# else:
#     print("Its not a leap year")


