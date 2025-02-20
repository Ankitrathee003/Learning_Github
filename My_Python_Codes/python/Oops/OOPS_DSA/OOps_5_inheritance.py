## INHERITENCE
# Derived classes or child classes inherit properties from parent classes
# eg  shape =     (color,filled)  Parent class
    # Rectangle =(color,filed,length,breadth)
    # Circle =    (color,filled,radius)
# clearly shape is a parent class wheras Rectangle and circle are child classses 
# some attributes or properties can be directly inherited from shape by rectangle and circle say color, filled
# Inheritance reduces the repitation of code



###

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self.maxspeed=maxspeed
class car(Vehicle):
    def __init__(self,color,maxspeed,numGears,isconvertible):
        super().__init__(color,maxspeed)  # here we are inheriting the properties of Vehicle class (2 properties color and maxspeed)
        self.numGears=numGears
        self.isconvertible=isconvertible
    def printcar(self):
        print("Color :",self.color)
        print("Maxspeed :",self.maxspeed)
        print("numGears:",self.numGears)
        print("isconvertible:",self.isconvertible)
# c=car("red",150,3,False)
# c.printcar()



## private operator

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed  # now max speed can not be accessed from outside the class means from car class
    def getmaxspeed(self):        # to make it possible from outside we are making a class within this 
        return self.__maxspeed
    def setmaxspeed(self,maxspeed): # set class using this we can change the speeed value
        self.__maxspeed=maxspeed
class car(Vehicle):
    def __init__(self,color,maxspeed,numGears,isconvertible):
        super().__init__(color,maxspeed)  # here we are inheriting the properties of Vehicle class (2 properties color and maxspeed)
        self.numGears=numGears
        self.isconvertible=isconvertible
    def printcar(self):
        print("Color :",self.color)
        print("Maxspeed :",self.getmaxspeed())
        print("numGears:",self.numGears)
        print("isconvertible:",self.isconvertible)
# c=car("red",150,3,False)
# c.printcar()


# Inheritance_continue

class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self.__maxspeed=maxspeed  # now max speed can not be accessed from outside the class means from car class
    def getmaxspeed(self):        # to make it possible from outside we are making a class within this 
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
    def printcar(self):
        super().print()   # inheriting the vehicle class properties we can also use    self.print()
        print("numGears:",self.numGears)
        print("isconvertible:",self.isconvertible)
c=car("red",150,3,False)
c.printcar()
