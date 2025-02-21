# Operator Overloading means giving extended meaning beyond their predefined operational meaning. 
# For example operator + is used to add two integers as well as join two strings and merge two lists. 
# It is achievable because ‘+’ operator is overloaded by int class and str class.

## Operator Overloading
class Point:
    def __init__(self,x,y):
        self.__x=x
        self.__y=y
    def __str__(self):
         return "this point is at ("+str(self.__x)+","+str(self.__y)+")"
    def __add__(self,point_object):
        return Point(self.__x+point_object.__x,self.__y+point_object.__y)

p1=Point(1,2)
p2=Point(3,4)
p3=p1+p2    # we can also write p3=p1.__add__(p2) 

print(p3)
