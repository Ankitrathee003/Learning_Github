# # Variables and methods defined with the private keyword may be accessed only by other methods within the class and cannot be accessed by derived classes.

# Public and Private methods

##### Public variABLE

class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollnumber=rollno
    def printstudent(x):
        print('my name is',x.name )

    
s1=Student("Ankush",12)
print(s1.__dict__)
# s1.printstudent()  # TypeError: student.printstudent() takes 0 positional arguments but 1 was given
                   # because s1 object is going as argument in printstudent
s1.name="rathee" 
print(s1.name)
print(s1.__dict__)



#### Private variable

class Student:
    def __init__(self,name,rollno):
        self.__name=name
        self.rollnumber=rollno
    def printstudent(x):
        print('my name is',x.__name )  # it is correct statement as we are using private variables within a class

    
s1=Student("Ankush",12)
print(s1.__dict__)
# print(s1.__name)    # AttributeError: 'Student' object has no attribute '__name'
s1.printstudent()     # this will work
print(s1.__dict__)   # NAME MANGLING   #{'_Student__name': 'Ankush', 'rollnumber': 12} # 