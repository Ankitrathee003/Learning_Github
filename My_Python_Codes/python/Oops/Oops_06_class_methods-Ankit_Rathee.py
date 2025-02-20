class Employee:
    counts=0  # count is a class variable/class attribute 
    def __init__(self,name,salery):  
        Employee.counts+=1                  # we can write either self or Employee while creating different instances 
        Employee.name=name                      # but Employee.salery will be static method while self.salery will be classmethod
        Employee.salery=salery              # so print(e1.salery) in static method will return salery of last member 
                                            # while print(e1.salery) in classsmethod will return salery of e1.

#     def count_instances():
#         return f' you have created {Employee.counts} instances of Employee class'

e1=Employee('x',100000)  
e2=Employee('y',200000)
# print(e1.salery)
# print(e2.salery)
print(Employee.salery)

class Employee:
    counts=0  # count is a class variable/class attribute
    def __init__(self,name,salery):
        Employee.counts+=1
        Employee.name=name
        Employee.salery=salery

    @classmethod          # we are calling decorator here named classmethod to create a class method Instead of static method
    def count_instances(xyz):   
        return f' you have created {xyz.counts} {xyz.salery} instances of Employee class'


 
# e1=Employee('y',2500000)
# e2=Employee('x',100000) 
# print(Employee.count_instances())   # we need NOT to pass any argument in class method 
# print(e1.count_instances())       # we can also use object of class here e2 is obj.but it is not recommended from understanding point of view
                                    # decorator used is helping us to make class method and class method do not require any argument




