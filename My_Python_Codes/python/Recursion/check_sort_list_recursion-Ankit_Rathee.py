         #METHOD_1

l=[2,3,4,24,98,45,98]
# # print(l,id(l))
# # del l[2]
# # print(l,id(l))

def check_sorted(l):
    if len(l)==0 or len(l)==1:
        return (True)
    else:
        if l[0]<=l[1]:
            del l[0]     #to remove first element of  list we can also use l.pop(0)
            return(check_sorted(l))
            
        else:
            return(False)
print(check_sorted(l))



        #METHOD_2
# l=[3]     #is_sorted(l,i) will reach to base case only when 
#                                   # all cases are found to be true.
# def is_sorted(l,i):               # i i index from where we want to start checking the sorted fun.
#     if len(l)==i or len(l)-1==i:  #len(l)==i means list is emptied &  
#                                   #len(l)-1==i means we have reached last element.
#         return(True)
#     else:
#         if l[i]>l[i+1]:           # will come out of function even a single case found to be wrong.
#             return(False)
#         else:
#             return(is_sorted(l,i+1))
# print(is_sorted(l,0))                           