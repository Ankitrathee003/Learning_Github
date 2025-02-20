def last_index(l,x):
    if len(l)==0:
        return(-1)
    smallerLIST=l[1:]
    smallerLISToutput=last_index(smallerLIST,x)
    if smallerLISToutput!=-1:
        return(smallerLISToutput+1)
    else:
        if l[0]==x:
            print(0)
        else:
            return(-1)

l=[1,2,3,4,5,3,3,6]
x=3
print(last_index(l,x))


    
