r=[1,2,6,3,4,5]
r1=r.copy()
x=int(input("enter the no.  "))
def greater_than_x(r):
    for i in range(len(r1)):
        if r1[i]<=x:
            print(i)
            r.remove(r1[i])
            print(r)
    return(r)
print(greater_than_x(r))

                          # CODE 2
# r1=[]
# for a in r:
#     if a>x:
#      r1.append(a)
# print(r1)
