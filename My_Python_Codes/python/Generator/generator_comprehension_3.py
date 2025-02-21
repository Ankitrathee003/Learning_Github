# list comprehensions
square=[i**2 for i in range(1,6)]
# print(square)


#Generator comprehension
sq=(i**2 for i in range(1,11)) #for gener. comprehension just use round brackets ().
print(sq)  #will print generator location
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
print(next(sq))
