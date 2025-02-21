#     @ use for decorator
# this is called syntectic sugar
#In computer science, syntactic sugar is syntax within a programming language that is designed to make things easier 
# to read or to express. It makes the language "sweeter" for human use: things can be expressed more clearly, more concisely, 
# or in an alternative style that some may prefer.

# def decorator_function(any_function):
#     def wrapper_function():
#         print('this is awsome function')
#         any_function()
#     return(wrapper_function)

# @decorator_function  # it will automatically call decorator function before func1
# def func1(a):
#     print(f'this is func1 with argument {a}')

# func1(7) # this will return an error as argument 7 is going in wrapper function
        # to overcome this we need to wrapper function inputs

# this is because 
# fuckrey=decorator_function(func)     a new function say fukray is called
# fukray(7)    so input 7 is going in wrapper function thats why showing error
 




def decorator_function(any_function):
    def wrapper_function(x):
        print('this is awsome function')
        any_function(x)
    return(wrapper_function)

@decorator_function  # it will automatically call decorator function before func1
def func1(a):
    print(f'this is func1 with argument {a}')

func1(6) # input 6 is feed to wrapper and then feed to any function 
         # which will call func1()