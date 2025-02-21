def add(a,b):
    return(a+b)
# print(add(1,3))

# Above function can be simply defined using lambda expression
# # # # syntex lambda input:output #  #  # #
addition=lambda a,b : a+b
# print(addition(12,3))
# print(type(addition))   # <class 'function'>


x=(lambda x,y:x**y*x)(3,2)  #input can be given by just writing at the end
# print(x)

#lambda expressions are anonymous they do not have any name ex.
# print(addition) #it will return the memory position

d={1:100,2:99,3:94}
print(max(d,key=lambda i:d[i]))