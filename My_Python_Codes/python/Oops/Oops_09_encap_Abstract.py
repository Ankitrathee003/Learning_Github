# Encapsulation    
                    
            #Encapsulation is a mechanism of wrapping the data (variables) and code acting on the data (methods) together as a single unit
            #  data ke sath perform karne wale operations (methods in ooops ex. make_a_call) or data ko ek sath rakhna  


# Abstraction

# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user. 
# This is one of the core concepts of object-oriented programming (OOP) languages.

#some special naming convention
# name mangling  __name (not a convention)  it changes the name in format    _class__object



class Phone:
    def __init__(self,brand,model_name,price):
        self.brand = brand
        self.model_name=model_name
        self.__price = price

    def make_a_call(self,phone_number):
        print(f'calling {phone_number}...')

    def full_name(self):
        return f"{self.brand} {self.model_name}" 

p1=Phone("Nokia","1100",1000)
# print(p1._price)
# p1._price=2000       # ye h public hi private kuch nhi h  matlab hum change kar skte  h
# print(p1._price)     #   _name  # (convention of private name other user ko btana ki iske saath na ched chaad kre)
# print(p1.__price)      # we have the __price defined above still will show error as python has changed its name to _Phone__price
print(p1.__dict__)      # {'brand': 'Nokia', 'model_name': '1100', '_Phone__price': 1000}


#   _name  # (convention of private name other user ko btana ki iske saath na ched chaad kre)  # ye h public hi private kuch nhi h
#   __name__  #dunder or magic methods


#  ABSTRACTION
# Abstraction in python is defined as a process of handling complexity by hiding unnecessary information from the user.

l=[2,5,1,3,9]
# l=l.sort()    # Note: sort method returns none
l.sort()   # for example sort in python  uses TIM SORT which is combination of merge sort and insertion sort
print (l)  # but what is going behind the sort user does not have any glance means it is hidden or can be said ABSTRACTION.
