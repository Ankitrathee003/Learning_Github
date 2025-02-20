## Abstract classes
# Who ever will inherit from these class will have to implement all these methods defined in the class

from abc import ABC,abstractmethod

class Polygon(ABC):
    @abstractmethod    # it means who will inherit the Polygon class will have to use noofsides method otherwise programme will show

    def noofsides(self):
        return "I have more than 2 sides "
class Triangle(Polygon):
 
    # overriding abstract method
    def noofsides(self):
        print("I have 3 sides")
 
class Pentagon(Polygon):
 
    # overriding abstract method
     
    def noofsides(self):
        print("I have 5 sides")
p=Pentagon()
p.noofsides()





# class Automobile(ABC):
#     def __init__(self,No_of_wheels):
#         self.No_of_wheels=No_of_wheels
#         print("Automobile created")
    
#     @abstractmethod
#     def start(self):
#         pass
#     @abstractmethod
#     def stop(self):
#         pass
#     @abstractmethod
#     def drive(self):
#         pass
#     @abstractmethod
#     def get_No_of_wheels(self):
#         print( "no. of wheels are ",self.No_of_wheels)


# class Car(Automobile):
#     def start(self):
#         super().start()
#         print("start of car called ")
#     def stop(self):
#         pass
#     def drive(self):
#         pass
#     def get_No_of_wheels(self):
#         return super().get_No_of_wheels()


# class Bus(Automobile):
#     def start(self):
#         pass
#     def stop(self):
#         pass
#     def drive(self):
#         pass
#     def get_No_of_wheels(self):
#         return super().get_No_of_wheels()
    
# c=Car(4)

# print(c.get_No_of_wheels())