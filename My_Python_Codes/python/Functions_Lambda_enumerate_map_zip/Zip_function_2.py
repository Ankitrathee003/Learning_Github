# Zip_function
# we can seprate out elements of tuples present in a list.
# like collection of 1st element of every tuple,collection of second element of tuple
l1=[1,3,5,7,9]
l2=[2,4,6,8,10]

# to convert given list in different lists/tuples or unpack
l=[(1,2,9),(3,4,9),(5,6,9),(7,8,9),(9,10,9)] 

#   *operator with zip
# print(list(zip(*l)))

l3,l4,l5=(list(zip(*l)))
# print(list(l3))
# print(list(l4))


a,b,c=[("first"),("second"),("third")]
# print(a)
# print(b)


# new_list=[]
# for pair in zip(l1,l2):
#     new_list.append(max(pair))
# print(new_list)

m=[[1,2,3],[4,5,6],[7,8,9]]
l3=list(map(lambda a,b,c:(a+b+c)/3,*m))
# print(l3)


l1=[1,2,3,4]
l2=[4,2,9,2]
# print(sum((map(lambda i,j:i+j,l1,l2)))/len(l1))

# print(sum(l2))
print(l2.index(max(l2)))