import numpy as np

s=np.array([[253,45545,153,45,545,65]])
# print(s.argmax())  # return the index of greatest element treating it as 1d array
# print(s.argsort(axis=0))
c=(np.argsort(s.T))
# print(s[c])     

d=np.array([[2,3,44,0,0,5,8,99,3,0,0,6]])
# print(s+d)
# print(np.sqrt(s))

# print(np.where(s>100))   #will return index of s
print(np.nonzero(d))