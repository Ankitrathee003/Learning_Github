## SEARCHING THE KEY CORRESPONDING TO VALUE
dict={1:3,2:3,4:3,6:1}
# for key,value in dict.items():
#     if value==1:
#         # print(key)

# nums=[1,1,2,1]
# d={}
# for i in nums:
#     if i in d:
#         d[i]+=1
#     else:
#         d[i]=1
# for key,value in d.items():
#     if value==1:
#         # print(key)


d={(0,1):[1],(0,0):[3,4],(9,3):[9,22],(3,2):[10,11]}
d=dict(sorted(d))
print(type(d))
# for i,j in sorted(d):
#     print(i,j)



