## checking whether both dict are ame or not


d1={"a":1,"b":2,"c":3}
d2={"a":1,"c":3,"b":2}      
def IsDictSame(d1,d2):
    for i,j in d1.items():
        if i not in d2 or d2[i]!=j:
            return (False)
    return(True)
# print(IsDictSame(d1,d2))
nums=[1,2,3,4,5]
t=[]
# t.append(f"{nums[3]}")
# print(t)

del nums[3]
# print (nums)
for j in range(1,1):
    print(j)