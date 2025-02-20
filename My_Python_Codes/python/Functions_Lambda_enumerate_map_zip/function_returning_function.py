# def outer_func():
#     def inner_func():
#         print('inside inner func')
#     return(inner_func)


# ans=outer_func() # this line will not return anything even after calling function
#                  # as inner_func is not being called like inner_func()
# ans()  #this will work as it will call inner func



# def outer_func_1():
#     def inner_func():
#         print('inside inner func')
#     return(inner_func())

# nasa=outer_func_1() # it will work as in our function return statement is calling inner _func()


# def outer_func3(msg):
#     def inner_func_3():
#         print(f'message if {msg}')
#     return(inner_func_3())
# wer=outer_func3("hi! there")


# generate a function 
def to_power(x):
    def num(n):
        return(n**x)
    return(num)
a=to_power(5)
print(list(map(a,[i for i in range(5)])))
