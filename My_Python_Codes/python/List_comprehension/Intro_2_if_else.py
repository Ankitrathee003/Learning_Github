# reversing list elements
l=['abc','def','efg']
# l2=[]
# for i in l:
#     l2.append(i[::-1])
# print(l2)

#list comprehension
# l2=[i[::-1] for i in l]
# print(l2)


# a=[]
# for i in range (1,11):
#     if i%2==0:
#         a.append(i)
# print(a)


#List comprehension using IF
l=list(range(1,10))
n0=list(i for i in l if i%3==0)
n1=list(i for i in range(1,11) if i%2==0)
n2=list(i for i in range(1,11) if i%2!=0)
print(n0)
print(n1)
print(n2)


