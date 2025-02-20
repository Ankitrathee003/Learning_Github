## Methods of object class

# __new__    To create new objects


# __init__


# __str__
# The __str__() function controls what should be returned when the class object is represented as a string.
# If the __str__() function is not set, the string representation of the object is returned:


class Circle(object):
    def __init__(self,radius):
        self.__radius=radius
    def __str__(self):
        return "This is a circle class which takes radius as an argument"


c=Circle(5)
print(c)   #if we do not use __str__ method  it will print object address  # <__main__.Circle object at 0x000001AAE9EFC510>

