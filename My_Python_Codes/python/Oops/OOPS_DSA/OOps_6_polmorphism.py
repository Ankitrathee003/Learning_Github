##Polymorphism
## Ability to take multiple form
## method overwriting



# Code_1
# class Vehicle:
#     def __init__(self,color,maxspeed):
#         self.color=color
#         self.__maxspeed=maxspeed  # now max speed can not be accessed from outside the class means from car class
#     def getmaxspeed(self):        # to make it possible from outside we are making a class within this 
#         return self.__maxspeed
#     def setmaxspeed(self,maxspeed): # set class using this we can change the speeed value
#         self.__maxspeed=maxspeed
#     def print(self):
#         print("color :",self.color)
#         print("maxspeed :",self.__maxspeed)
# class car(Vehicle):
#     def __init__(self,color,maxspeed,numGears,isconvertible):
#         super().__init__(color,maxspeed)  # here we are inheriting the properties of Vehicle class (2 properties color and maxspeed)
#         self.numGears=numGears
#         self.isconvertible=isconvertible
#     def print(self):
#         super().print()     # if we write self.print() instead of super().print than recrsion depth will exceed
#         print("numGears:",self.numGears)
#         print("isconvertible:",self.isconvertible)
# c=car("red",150,3,False)
# c.print()   # car print is being called here


# code 2

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed  # now max speed can not be accessed from outside the class means from car class
    def getmaxspeed(self):        # to make it possible from outside wee are making a class within this 
        return self.__maxspeed
    def setmaxspeed(self,maxspeed): # set class using this we can change the speeed value
        self.__maxspeed=maxspeed
    def print(self):
        print("color :",self.color)
        print("maxspeed :",self.__maxspeed)
class car(Vehicle):
    def __init__(self,color,maxspeed,numGears,isconvertible):
        super().__init__(color,maxspeed)  # here we are inheriting the properties of Vehicle class (2 properties color and maxspeed)
        self.numGears=numGears
        self.isconvertible=isconvertible
c=car("red",150,3,False)
c.print()  # this print will first search print option in class car if not found than it will start searching in class vehicle 
            # here print is not present in car class so print of super class will be called if not found in super class than it will seearch in higher  super class and so on.
# v=Vehicle('blue',120)
# v.print()  # method over riding here as print of vehicle class is keep changing
