# working of for Loop

# first iter function is called and our list/string/tuple is passed in it
# after that function named next is called and output of iter function goes in it
n=[1,2,3,4,5]
number_iter=iter(n) # list has been converted to iterator
# print(number_iter)        # <list_iterator object at 0x000001FA325E1A20>
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))
# print(next(number_iter))  # iteration has completed

numbers=[1,2,3,4,5,6]   # iterables
# for i in numbers:
#     print(i)
# print(next(numbers)) # it will show error as number is not Iterator




squares =map(lambda a:a**2,numbers)  #iterator
print(type(squares))  #<class 'map'>#
print(squares)
# for i in squares:
#     print(i) 


# square is already a iterator 

# print(next(squares))
# print(next(squares))
# print(next(squares))
# print(next(squares))

 