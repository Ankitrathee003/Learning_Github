#we will return  first index of a given element in the list 
# l=[7]
# x=67                                            # all cases are found to be not matching.
# def finding_position(l,i):               # i  index from where we want to start checking the indexing function.
#     if len(l)==0:
#         return("list is empty")

#     if len(l)-1==i  and l[i]!=x:         # agar check karte karte last element pe paunch jaye or fir bhi na mile
#          return(f"{x} not found in {l}") 
#     if l[i]==x:                
#             return(((f"{x} is at {i}  index")))
#     else:
#             return(finding_position(l,i+1))
# print(finding_position(l,0))

#we will return  index of a given element in the list checking from last
l=[23,43,54,89,34,968,9,24,87,67]
x=24                                        
def finding_position(l,x,i):               
    if len(l)==0:
        return("list is empty") 
    if -len(l)==i  and l[i]!=x:
        return(f"{x} not found in {l}") 
    if l[i]==x:                
            return(((f"{x} is at {len(l)+i}  index")))
    else:
            return(finding_position(l,x,i-1))
print(finding_position(l,x,-1))
