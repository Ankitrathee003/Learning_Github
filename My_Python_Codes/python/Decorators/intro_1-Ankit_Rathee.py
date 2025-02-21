# # decorators enhance the functionality of other function

def decorator_function(any_function):
    def wrapper_function():
        print('this is awsome function')
        any_function()
    return(wrapper_function)


def func1():
    print('this is func1')


# z=decorator_function(func1) # simple example of decorator
# z()                         # for any function we want to print the line 
# #                           # this is awsome function we will pass it through decorator function


def decorator_function(any_function):
    def wrapper_function():
        print('this is awsome function')
        any_function()
    return(wrapper_function)

@decorator_function  # it will automatically call decorator function before func1
def func1():
    print('this is func1 ')

func1() 