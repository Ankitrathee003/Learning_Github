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