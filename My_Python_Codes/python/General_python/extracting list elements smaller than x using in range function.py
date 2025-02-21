l=[]
a=[]
n=int(input("enter the no. of elements: "))
for i in range (0,n):
    i=int(input())
    l.append(i)
print(l)    
x=int(input("enter the no. you want less than that:  ")  )  
for i in l:
   if i<x:
    a.append(i)
print(a)
    