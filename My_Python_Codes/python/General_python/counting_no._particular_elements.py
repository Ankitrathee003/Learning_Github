#counting no. of 1 i sublist
a=[[91,5,1,1,23,1],[5,1,51,1],[23,1,23,1,10]]
l=[]
# print(type(a))
# print(len(a[2]))
for i in range (len(a)):
    count=0
    for j in range (len(a[i])):
        # print(a[i][j])
        if a[i][j]==1:
            count+=1
    l.append(count)
print(l)