def sum(l):
    if len(l)==0:
        return(0)
    elif len(l)==1:
        print(f"HEY {l}")    # to print last element remaining in list 
                            # as print in else statement will print upto 2 elements
        return(l[0])
    else:
        print(l)
        return(l.pop()+sum(l))    # pop method remove last element by default
                                  # untill we specify index 
l=[2,4,54,6,-6]
print(sum(l))
