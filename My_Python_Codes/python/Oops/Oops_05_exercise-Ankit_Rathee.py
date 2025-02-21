
class Employee:
    count=0  # count is a class variable/class attribute
    def __init__(self,name,salery):
        Employee.count+=1
        Employee.name=name
        Employee.salery=salery
e1=Employee('x',100000)  
e2=Employee('y',200000)   # each time when we make the object init method is called
print(Employee.count)   # it will give the no. of instances as it is calculating the no of times init method is called 
print(e2.salery)


