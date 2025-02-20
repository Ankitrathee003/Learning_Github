# def add_all(*args):
#     total=0
#     for i in args:
#         total+=i
#     return(total)
# # print(add_all(1,2,3,4))
# print(add_all(1,2,3,4,*[5,6,7,8,9,10]))




# this will show error due to unpacking of list
# print(add_all(1,2,3,4,[5,6,7,8,9,10]))
# we can use decorator here

from functools import wraps
def only_int_allow(function):
    @ wraps(function)
    def wrapper(*args,**kwargs): #using * operator allows to take any no. of inputs
       data_types=[]
       for i in args:
        data_types.append(type(i)==int)
       if all(data_types):  # will run only if all are TRUE in it
            return function(*args,**kwargs)
       else:
            return('Invalid arguments')
    return wrapper


@only_int_allow
def add_all(*args):
    total=0
    for i in args:
        total+=i
    return(total)

print(add_all(1,2,3,4,5))


