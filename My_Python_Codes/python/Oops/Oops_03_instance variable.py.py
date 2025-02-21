#Instance_methods####
class Person:    #__init__ is a also a method to construct objects
    def __init__(self,first_name,last_name,age):
        self.first_name=first_name
        self.last_name=last_name
        self.age=age
    def full_name(self): # function inside a class is method of that class
        return f"{self.first_name} {self.last_name}"
    def is_above_18(self):
            return self.age>18

p1=Person('Harshit','vashistha',24)

# print(p1.full_name())    # This is representing a method applied on object name p1. IT IS SAME AS WE APPLY l.APPEND() OR l.POP() on object l=[1,2,3] 

                                 #full_name is method of class Person
# print(Person.full_name(p1)) # both these lines are same
# print(p1.is_above_18())
l=[1,2,3]
l.append(4)

list.append(l,5)   # this will also append to list it is taking   # l as self/ object of class list
l1=[6,7,8,9]
list.append(l,l1) # l1 will remain packed
print(l)           


#SALE method to 
class Laptop:
    def __init__(self,brand,model_name,price):
        # instance variables  # we can create even more than no. of  input variables
        self.brand_name=brand
        self.Laptop_ka_model=model_name
        self.Laptop_ka_price=price
    def sale(self,p):   # p is the % off on laptop price
        return (self.Laptop_ka_price)*(1-p/100)
l1=Laptop('asus','A13',50000)
# print(l1.sale(40))



