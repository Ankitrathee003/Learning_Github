def cube(a):
    return(a**3)

def my_map(func,l):
    new_list=[]
    for i in l:
        new_list.append(func(i))
    return(new_list)
print(my_map(cube,[1,2,3,4])) #cube is a function which is argument to my_map function
print([i**3 for i in range(1,9)])