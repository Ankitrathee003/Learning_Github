#map_function
# map(name of function,input)   #syntex
a=[i**2 for i in range (1,8)]

def square(i):
    return(i**2)

# print(list(map(square,a)))
print(list(map(lambda i:i**2,a)))
 


# we can use lambda expression at place of square function
a=[i for i in range (1,11)]
# print(list(map(lambda a:a**2,a))) 




# above example can also be solved using list comprehension 
# print(list(i**2 for i in range(1,7)))



#
# names=['ankit','rathee','vinod']
# length=map(len,names)
# for i in length:
#     print(i)
# for j in length:  # map function output is not iterable repeatedly
#     print(j*4)    #  we can iterate only once


# to overcome we can convert map to list
# length=list(map(len,names))
# for i in length:
#     print(i)
# for j in length:
#     print(j*4)

# l=[[1,2,3],[1,5,9]]
# count=0
# for i in [k[0] for k in l]:
#     if i==1:
#         count+=1
        
# print(count)




