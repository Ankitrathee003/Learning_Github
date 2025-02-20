# class variable  # class attribute
# circle
# class circle:
#     def __init__(self,radius,pi):
#         self.radius=radius
#         self.pi=pi
#     def cal_circumferrence(self):
#         return(2*self.pi*self.radius)


# c1=circle(2,3.14)
# c2=circle(4,3.14)  # we have to provide pi value again and again for every object of this class
                     # so instead of making pi as instance variable we will make it class variable
                    
# print(c1.cal_circumferrence())



# class variable pi  # making class variable will also reduce memory size 
class circle:
    pi=3.14   # class variable can be used for any function/method of this class
    def __init__(self,radius):
        self.radius=radius
    def cal_circumference(self):
        return(2*circle.pi*self.radius)  #circle.pi is working as a class method

c3=circle(5)
print(c3.cal_circumference())