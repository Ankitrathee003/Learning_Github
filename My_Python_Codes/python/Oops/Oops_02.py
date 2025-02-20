# what is class
#how to create a class
# what is init method
# what are attributes, instance, variables
# how to create our object

#  __init__  is called constructor here

class Person:   # keep class first Alphabet capital
    def __init__(self,first_name,last_name,age): # self represents a object
        #instance variables          # we can use any other keyword for self but it is convention
        self.Aadmi_first_name=first_name
        self.Aadmi_last_name=last_name
        self.Aadmi_age=age
p1=Person('Harshit','vashistha',24)  # P1 (self) is object here
p2=Person('Mohit','rathee',38)

# print(p1.Aadmi_last_name)
# print(p2.Aadmi_first_name)



class Laptop:
    def __init__(self,brand,model_name,price):
        # instance variables  # we can create even more than no. of  input variables
        self.brand_name=brand
        self.Laptop_ka_model=model_name
        self.Laptop_ka_price=price
        self.Laptop_brand_model= brand + "  " + model_name

l1=Laptop('asus','A13',50000)   # l1 is object of class Laptop
print(l1.brand_name)
print(l1.Laptop_brand_model)






