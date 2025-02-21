# id is corresponding to the value not to the variable
# instead variables are bind to the values
# Python variables are references to objects(valus) located in the memory
# Use the id() function to get the memory address of the object referenced by a variable.
# link :https://www.pythontutorial.net/advanced-python/python-references/

x=100
y=(100,34)
z=100
print(id(x))
print(id(100))
print(id(z))
print(id(y[0]))
print(id(y))


# import ctypes
# def ref_count(address):
#     return ctypes.c_long.from_address(address).value
# numbers = [1, 2, 3]
# numbers_id = id(numbers)
# print(ref_count(numbers_id))  # 1
# ranks = numbers
# print(ref_count(numbers_id))  # 2
# ranks = None
# print(ref_count(numbers_id))  # 1
# numbers = None
# print(ref_count(numbers_id))  # 0