from re import S
import numpy as np
m1=np.array([[1,2,3],[4,5,6],[7,8,9]])
def mean(a):
    sum=0
    for i in range(len(a)):
        for j in range (len(a[0])):
            sum+=a[i,j]
    mean=sum/((len(a[0]))*len(a))
    return(mean)
m=mean(m1)
print(m)
def sd(a):
    sum=0
    for i in range(len(a)):
        for j in range (len(a[0])):
            sum+=(a[i,j]-m)**2
    SD=sum/((len(a[0]))*len(a))
    return(SD)
s=sd(m1)
print(s)