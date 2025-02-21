# import numpy as np
# m1=np.array([[1,1],[2,3]])
# m2=np.array([[6,7],[9,2]])
# sum=np.array([[0,0],[0,0]])
# for i in range (0,len(m1)):
#     for j in range (0,len(m2)):
#         sum[i,j]=m1[i,j]+m2[i,j]+sum[i,j]
# print(sum)        


l=[1,2,3,4,5,67,"j",45,"jp"]
x="jp"
def elementINlist(l,x):
    if len(l)==1 and l[0]==x:
        return(True)
    elif len(l)==1 and l[0]!=x:
        return(False)
    else:
        if l[0]==x:
            return(True)
        else:
            l.pop(0)
            return(elementINlist(l,x))
print(elementINlist(l,x))