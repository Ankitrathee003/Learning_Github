#Array creation :converion from other python strructure
import numpy as np
b1=np.array([(1,2,3,4),(5,6,7,8)])
print(b1)
# print(b1.dtype)
# print(b1.size)
# print(b1.shape)
#print(b1.ndim) #no. of dimensions

x=np.arange(11,99,4)  # from 11 to 99 with gap = 4 # 99 not included
# print(x)


zeroes=np.zeros((2,3)) #it gives float data type
# print(zeroes,zeroes.dtype)


lspace=np.linspace(1,6,4)   #wil divide into 4 equally spaced numbers between 1,6
# print(lspace)               # (difference=(6-1)/(4-1))

emp=np.empty((2,4))
# print(emp)
# print(b1)
# print(emp+b1)


z=np.empty_like(b1) #make empty array of size same as defined before
# print(z)

# ide=np.identity(3) #to produce identity matrix
# print(ide)

# arr=np.arange(30)
# print(arr)
# a=(arr.reshape(3,10))
# print(a)
# print(a.ravel())  # ravel() method returns flatend array


