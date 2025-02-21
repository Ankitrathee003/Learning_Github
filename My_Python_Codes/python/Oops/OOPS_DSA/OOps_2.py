class Student:
    def __init__(self,name,rollno):
        self.name=name
        self.rollnumber=rollno
    def printstudent(self):
        print('my name is',self.name )
s1=Student("Ankush",12)
print(s1.__dict__)
s1.printstudent()  # TypeError: student.printstudent() takes 0 positional arguments but 1 was given
                   # because s1 object is going as argument in printstudent
s1.name="rathee"   # we can change the name as it is a public variable to make it pprivate  
print(s1.__dict__)