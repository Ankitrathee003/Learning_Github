# un-ordered collection of unique items
# no indexing 
# we can not store list or dictionary in our set

s={1,1.0,2,3,3,4,'string' }
# print(len(s))

#to remove duplicate
# l=[1,1,1,2,2,2,3,3,3,3,4,4,4,4]
# print(l)
# l=list(set(l))
# print(l)



# add Method
# s1={0,1,2,3,4,5,6,7}
# s1.add(8)
# s1.add(9)
# print(s1,type(s1))

#remove method   # discard method 
# s2={0,1,2,3,4,5,6,7}
# s2.remove(6)  # Remove method can show error if input element is not present in set.
# s2.discard(8) # Discard method will not show error even if input element is not present in set.
# s2.discard(2)
# print(s2)

# clear method  
s3={0,1,2,3,4,5,6,7,8,9}
# s3.clear()
# print(s3)


# copy method
s4=s3.copy
# print(s4)
# if id(s4)==id(s3):
#     print(True)
# else:
#     print(False)



# if s3 is s4: 
#     print(True)
# else:
#     print(False)


print(ord("{"))
print("hello")