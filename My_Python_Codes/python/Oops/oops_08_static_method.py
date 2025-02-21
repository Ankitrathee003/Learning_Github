# static method #
#static method has no relation with class or object but can have logical connection
# Static methods in Python are extremely similar to python class level methods, 
# the difference being that a static method is bound to a class rather than the objects for that class.
# This means that a static method can be called without an object for that class. 
# This also means that static methods cannot modify the state of an object as they are not bound to it.

from datetime import date
class Person:   # keep class first Alphabet capital
    def __init__(self,first_name,last_name,age): # self represents a object
        #instance variables          # we can use any other keyword for self but it is convention
        self.Aadmi_first_name=first_name
        self.Aadmi_last_name=last_name
        self.Aadmi_age=age
        
    @staticmethod    # static method is also called class method as it is not related to object  These are like the utility functions
    def hello():     #after defining @staticmethod we need not to pass any argument in hello method like self
        print('hello,static method called')

    @classmethod
    def Year_of_birth(cls,first_name,last_name,age):
        return cls(first_name,last_name,date.today().year-age)  # this data will go to init now

p1=Person('Harshit','vashistha',24)  # P1 (self) is object here
p2=Person('Mohit','rathee',38)

# Person.hello()
p3=Person.Year_of_birth("Ankit","Rathee",24)
print(p3.Aadmi_age)