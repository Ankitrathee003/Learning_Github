# l=[]
# n=int(input("enter the no. of elements: "))
# for i in range (0,n):
#     i=int(input())
#     l.append(i)
# print(l) 
# def asa(l):
#     j=0
#     while len(l)>1:
#         a=[]
#         for i in range (1,len(l)):
#             if int(l[j])<int(l[i]):
#                 a.append(l[i])
#         if len(a)==0:
#             a.append(l[j])
#         l=a
#         print(l)
    
# asa(l)



#code  2
# l=[3,4,5,6,6,54,34,543,564,2]
# for a in l:
#     for b in l:
#         if a<b:  
#              # if a is smaller than any element than it can not be greatest in list
#             break # once the loop brake control goes to upper for (a in l) loop and a got changed 
#     else:
#         print(a)

       
       
# Code 3
l=[3,4,564,6,6,54,34,543,2]
result=l[0]
for i in range (1,len(l)):
    if l[i]>result:
        result=l[i]
        print(result)
# print(result)
   








