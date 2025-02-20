# class--> it is a templlate that will about data and tpes of functionality this class will have
# Object --> An instance of the class

# class student: # we can not leave the class empty if we do not want to write than we can write pass
#         pass
# s1=student()
# print(s1)
# print(type(s1))    #<class '__main__.student'>




# Adding attributes to individual objects without init function

class student: 
        pass
s1=student()
s2=student()
s3=student()
s1.name='ankit'
s1.Rollno =34
s3.name='Rahul'      # SYNTEX  of adding attribute same as dictionary # object.key=value
s3.Rollno=33
# print(s3.name)
# print(s3.__dict__)


# print(hasattr(s1,'name'))  # To check whether we are having the particular attribute for a object
# print(hasattr(s2,'name'))



# print(getattr(s1,'Rollno'))   # it will return the value of attribute here 34
# # print(getattr(s2,'Rollno'))  #In s2 there is no rollno attribute so it will give error to come out of this we can pass required argument at third place 
# print(getattr(s2,'Rollno','NOT FOUND')) #if s2 has no rollno than it will give third argument here "NOT FOUND"
# print(s1.name)  we can use object.attribute simply instead of getattr()


# deleting attribute for a object
# print(s1.__dict__)
# delattr(s1,'Rollno')
# print(s1.__dict__)