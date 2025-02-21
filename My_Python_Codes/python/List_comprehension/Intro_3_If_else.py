# l=[1,2.3,[4,5],(2,3,4,4),'string',{1:2,2:3},{9,8,7,8}]

# using loops bring int & float valued in quotations
# a=[]
# for i in l:
#     if (type(i)==int) or(type(i)==float):
#         a.append(f'{i}')
# print(a)

#Using list comprehension
# l1=list(f'{i}' for i in l if type(i)==int or type(i)==float )
# l2=list(str(i) for i in l if type(i)==int or type(i)==float)
# print(l1)
# print(l2)



#Multipying odd with -1 and even with 2
 
# l=[1,2,3,4,5,6,7,8,9,10]
# print(l)
# x=[]
# for i in l:
#     if i%2==0:
#         x.append(i*2)
#     else:
#         x.append(-i)
# print(x)

# OR without using extra space
# l=[1,2,3,4,5,6,7,8,9,10]
# for j in range (len(l)):
#         if l[j]%2==0:
#             l[j]=2*(l[j])
#         else:
#             l[j]=-l[j]
# print(l)


#agar only if use kar rahe h to pehle for waali statement uske baad if wali statement
#agar if else dono h to pehle if else statement uske baad for statement


# Using List comprehension using (if+else)
# y=list(i*2 if i%2==0 else -i for i in  l)
# print(y)







