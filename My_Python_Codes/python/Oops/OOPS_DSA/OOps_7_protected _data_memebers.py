## protected data members are denoted by _XXXXXX they can be changed or accessed even outside the class, this connvention is made for us only.
## it assumes that user itself has sense of all these keywords


class Vehicle:
    def __init__(self,color,maxspeed):
        self.color=color
        self._maxspeed=maxspeed  # now max speed can be accessed from outside the class means from car class
    # def getmaxspeed(self):        
    #     return self._maxspeed
    # def setmaxspeed(self,maxspeed): # set class using this we can change the speeed value
    #     self._maxspeed=maxspeed
    def print(self):
        print("color :",self.color)
        print("maxspeed :",self._maxspeed)
class car(Vehicle):
    def __init__(self,color,maxspeed,numGears,isconvertible):
        super().__init__(color,maxspeed)  # here we are inheriting the properties of Vehicle class (2 properties color and maxspeed)
        self.numGears=numGears
        self.isconvertible=isconvertible
    def print(self):
        # super().print()    
        print("color :",self.color)
        print("maxspeed:" ,self._maxspeed)
        print("numGears:",self.numGears)
        print("isconvertible:",self.isconvertible)
c=car("red",150,3,False)
c.print() 

v=Vehicle("blue",120) # we can assign or change names even outside the class
v.print()



