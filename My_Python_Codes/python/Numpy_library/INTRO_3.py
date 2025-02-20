#NUMPY AXIS
# axis 0 is along vertical/column
#  axis 1 is along rows/horizontal 
import numpy as np
a=np.array([[1,2,3],[4,5,6],[7,8,9]])
# print(a.sum(axis=0)) 

# transpose of matrix #
print(a.T)

# for i in  a.flat:
#     print(i)


# print(a.nbytes)   #gives total no bytes

s=np.array([[253,45545,153,45,545,65]])
print(s.argmax())  # return the index of greatest element treating it as 1d array
print(s.argsort(axis=1))  #will return index to arrange in increasig order
# c=(np.argsort(s))
# print(s[c])     

# print(c)