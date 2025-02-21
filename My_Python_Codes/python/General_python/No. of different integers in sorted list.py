l=[2,3,3,3,4,4,5,7,7,7]
j=1
for i in range (len(l)-1):
        if l[i]<l[i+1]:
            l[j]=l[i+1]
            j+=1
print(l)
print(j)

    
