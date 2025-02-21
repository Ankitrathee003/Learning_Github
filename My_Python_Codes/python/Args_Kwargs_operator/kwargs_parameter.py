# kwargs (keyword argument)
# **kwargs(double star operator)

#kwargs as a parameter
def fun(**kwargs):
    #kwargs as argument
    print(kwargs,type(kwargs))  # dictionary with name kwargs
# fun(name='Ankit', last_name='rathee')
# print(type(kwargs))

#
def fun(**kwargs):
    for i,j in kwargs.items():
        # print(f"i am {name}")
        print((f"{i}:{j}"))
        #kwargs as a parameter
# (fun(name='Ankit', last_name='rathee')) 



d={'apple':'5','banana':'12','grapes':'250'}
print(type(d))
fun(**d)  # unpacking dictionary