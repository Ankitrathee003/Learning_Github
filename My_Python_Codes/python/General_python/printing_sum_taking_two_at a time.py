x = int(input('enter the no. of list elements  '))
l=[]
for i in range (x):
    l.append(int(input(f'Enter the list {i+1}th element ')))
print (l)
a=[]
sum =0
for i in range (x):
    if i < 0.5*(x):
        print(i,   (x-i-1))
        if l[i]==l[x-i-1]:
            a.append(l[i])
        else:
            a.append(l[i]+l[x-i-1])
print(a)
    
