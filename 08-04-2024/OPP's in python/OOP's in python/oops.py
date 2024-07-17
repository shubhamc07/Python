# ex 1 class and objects
class Car:
    total_car = 0 # class variable

    def __init__(self,brand,model):
        self.__brand = brand #private 
        self.__model = model
        Car.total_car += 1

    def get_brand(self): # Encapsulation
        return self.__brand + " !"
    
    def full_name(self):
        return f"{self.__brand} {self.__model}"
    
    def fuel_type(self): # polymorphism
        return "Petrol or Diesel"
    
    @staticmethod
    def _general_desc():
        return "Cars are means of transport"
    
    @property
    def model(self):
        return self.__model

my_car = Car("Tata","Nexon")
# print(my_car.brand)
# print(my_car.model)
# print(my_car.full_name())

my_new_car = Car("Tata","Safari")
# print(my_new_car.model)
# print(my_new_car.full_name())

# inheritance
class ElectricCar(Car):
    def __init__(self, brand, model,battery_size):
        super().__init__(brand, model)
        self.battery_size = battery_size
    
    def full_name(self):
        return f"{super().full_name()} {self.battery_size}"
    
    def fuel_type(self): # polymorphism
        return "Electric charge"

new_nexonev = ElectricCar("Tata","Nexon.ev","75kwh")
# print(new_nexonev.model)
# print(new_nexonev.full_name())


 # Encapsulation
 # print(my_car.__brand)
 # print(my_car.get_brand())
 # print(new_nexonev.__brand)
# print(new_nexonev.get_brand())

# polymorphism
# print(my_new_car.fuel_type())
# print(new_nexonev.fuel_type())

# class variable
# print(Car.total_car)

# static method
# print(my_car._general_desc())
# print(Car._general_desc())

# property decorators
# print(my_car.model)

# class inheritance and isinstance() function
# print(isinstance(new_nexonev,Car))
# print(isinstance(new_nexonev,ElectricCar))

# multiple inheritance
class Battery:
    def battery_info(self):
        return "this is battery info"

class Engine:
    def engine_info(self):
        return "this is engine info"

class ElectricCarTwo(Battery,Engine,Car):
    pass

new_tesla = ElectricCarTwo("Tesla","Model y")
# print(new_tesla.engine_info())
# print(new_tesla.battery_info())


def hello(name):
    print(f"{name}")
print(hello("shubham"))