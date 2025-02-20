# class method as constructor


# class Person:   # keep class first Alphabet capital
#     def __init__(self,first_name,last_name,age): # self represents a object
#         #instance variables          # we can use any other keyword for self but it is convention
#         self.Aadmi_first_name=first_name
#         self.Aadmi_last_name=last_name
#         self.Aadmi_age=age
# p1=Person('Harshit','vashistha',24)  # P1 (self) is object here
# p2=Person('Mohit','rathee',38)

# we want to create object like
# p3=Person('Harshit,vashisth,23')
# then we have to make our constructor (constructor used for p1,p2 is inbuilt i.e __init__)


class Person:   # keep class first Alphabet capital
    def __init__(self,first_name,last_name,age): # self represents a object
        #instance variables          # we can use any other keyword for self but it is convention
        self.Aadmi_first_name=first_name
        self.Aadmi_last_name=last_name
        self.Aadmi_age=age

    @classmethod                # A class method takes cls as the first parameter while a static method needs no specific parameters.
    def from_string(cls,string):   # Class method is also called factory method as it will return an object of that class
        first,last,age=string.split(',')
        return cls(first,last,age)     # it will automatically refer  to  __init__  as it is a classmethod


p3=Person.from_string('Harshit,vashisth,23')
print(p3.Aadmi_last_name)