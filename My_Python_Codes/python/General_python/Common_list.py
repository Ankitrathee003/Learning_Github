x=[1,2,3,4,5,6]
y=[3,4,5,6,7]
l=[]
def commonLIST(x,y):
    for i in x:
        for j in y:
            if i==j:
                l.append(i)
    return(l)
print(commonLIST(x,y))
        

