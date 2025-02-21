# Reversing stack using recursion using given empty stack only

# For ex. we want to reverse stack       
    #  | (4)|      |     |
    #  | (3)|      |     |
    #  | (2)|      |     |
    #  | (1)|      |     |
    #  ------      -------
    #     S1         S2
#  move (n-1) elements frpm S1 to S2 and store bottom last element i.e (1) here
#   #  |    |      |     |
    #  |    |      | (2) |
    #  |    |      | (3) |      & store element last here (1)
    #  |    |      | (4) |
    #  ------      -------
    #     S1         S2

# now move these n-1 elements from S2 to S1 
    #  |    |      |     |
    #  | (4)|      |     |
    #  | (3)|      |     |
    #  | (2)|      |     |
    #  ------      -------
    #     S1         S2
# Now the problem is just redduced by one step now we have to again reverse S1 using empty S2 and will add recent last element (FIFO) to it.
#  using recursion we will reverse the S1 and will add (1)

    #  | (1)|      |     |
    #  | (2)|      |     |
    #  | (3)|      |     |
    #  | (4)|      |     |
    #  ------      -------
    #     S1         S2



s1=[1,2,3,4]
s2=[]
def reverseStack(s1,s2):  # means reversing S1 using S2

    if len(s1)==1:
        return
    
    while (len(s1)>1):
        element=s1.pop()
        s2.append(element)
    store=s1.pop()
    
    while s2:
        element=s2.pop()
        s1.append(element)


    # recursive call of reversing and pushing stored value    
    reverseStack(s1,s2)
    s1.append(store)

reverseStack(s1,s2)
print(s1,s2)







