import  numpy as np
import sys
import math
import pickle
a=np.array([1,2,3,4,5])
# print(a)
b1=np.array([(1,2,3,4),(5,6,7,8)],np.int64) #both b1 and b2 are same
                                            # np.int(64) is data type
b2=np.array([[1,2,3,4],[5,6,7,8],[9,10,11,12]])
# print(b1,b2)
# print(type(b1),type(b2))
# print(b1.ndim)
# print(b1.shape)
# print(b1.dtype)
# b1[0,3]=20
# print(b1)
# b3=[]


##  pickle  ##


# The pickle module implements binary protocols for serializing and de-serializing a Python object structure.
# “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation,
# whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy. 
# Pickling (and unpickling) is alternatively known as “serialization”, “marshalling,” 1 or “flattening”; however, to avoid confusion, the terms used here are “pickling” and “unpickling”.


# b3=(pickle.dumps(b2))
# print(b3)















b3=(np.arange(10))
# for i in b3:
#     print(i)
print(sys.getsizeof(b3))
print(b3.size)
print(b3.itemsize)

b4=np.arange(11,21)
print((b3*b4))