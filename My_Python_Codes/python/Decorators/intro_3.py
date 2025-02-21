
# def decorator_function(any_function):
#     def wrapper_function(x,y):
#         """this is wrapper function"""
#         print('this is awsome function')
#         any_function(x,y)
#     return(wrapper_function)

# @decorator_function  # it will automatically call decorator function before func1
# def multiply(a,b):
#     return(a*b)
# print(multiply(2,5))
# it will return doc string of wrapper function  which is a problem
 #will return NONE instead of 10 
                        #because multiply is going as any function in decorater_function 
                        # and we are just calling any function instead of printing.
# print(multiply.__name__)  # again will return wrapper function i.e misleading to new user
# to over come this imports wraps from functools

from functools import wraps

def decorator_function(any_function):
    @ wraps(any_function)
    def wrapper_function(x,y):
        """this is wrapper function"""
        print('this is awsome function')
        print(any_function(x,y))
    return(wrapper_function)

@decorator_function  # it will automatically call decorator function before func1
def multiply(a,b):
    """this is multiply function"""
    return(a*b)
multiply(2,5)
print(multiply.__doc__)