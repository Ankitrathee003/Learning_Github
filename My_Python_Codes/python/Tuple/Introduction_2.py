# x=int(input("enter the length of tuple: "))
# n=()
# print(n, (type(n)))

m1=(1,2,3,4,5,1,2,1,21,11,1,1,16,7,8)
m2=([1,2,3,4,5,6,7,8,9])
m3=str([1,2,3,4,5,6,7,8,9]) # m3 is a string but output will remain same    
# print(m1,m2,m3,type(m1),type(m2),type(m3))
# print(m1.count(1))
# print(sum(m1))



elements = input('Enter the elements for the tuple (separated by spaces): ')
elements = elements.split()
tuple_ = tuple(int(i) for i in elements)
print(type(tuple_))
list_=list(tuple_)
s=[4,5]
for i in s:
    list_.append(i)
print(type(list_))
final=tuple(list_)
print(final)




