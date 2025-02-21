# l=[2,23,43,54,89,34,968,9,23,87,67]
# x=23                                            # all cases are found to be not matching.
# def finding_position(l,i):                      # i  index from where we want to start checking the index ing function.
#     if len(l)==0:
#         return("list is empty")
#     if len(l)-1==i  and l[i]==x: 
#         return(f"{x} is at {i} index")  
#     if len(l)-1==i  and l[i]!=x:
#         return(-1) 
#     if l[i]==x:  
#         y=(finding_position(l,i+1))
#         if y==-1:
#             return(i)
#         else:
#             return()           
#     else:
#         return(((f"{x} is at {i}  index")))
            
# print(finding_position(l,0))



# print(math.floor(math.sqrt(4)))


 


# l=[1,2,5,6,7,43,339]
# x=6
# global count    
# count=0

# def index_of_element(l,x):
    
#     if len(l)==0:
#         return("list is emptied")
#     elif len(l)==1 and l[0]==x:
#         return(0)
#     elif len(l)==1 and l[0]!=x:
#         return(False)
#     else:
#         if l[0]==x:
#             count+=1
#             return(count)
#         else:
#             del l[0]
#             count+=1
#             return(index_of_element(l,x))
        
# print(index_of_element(l,x))   



















# s=['gh','ijjkji','aaaaa','y','hkhjh']
# print(max(s))



# counting no. of list in given list 
# n=[1,2,3,[1,5],[43]]
# def countLIST(n):
#     count=0
#     for i in range (len(n)):
#         if type(n[i])==list:
#             count+=1
#     return(count)
# print(countLIST(n))


# l=[4,4,3,7,5,9,1]
# l.append([19,34,543])
# l.extend([19,34,543])
# print(l)

# def fun(n):
#     if n==4:
#         return(n)
#     else:
#         return(2*fun(n+1))
# print(fun(-5)) 



print("complete")


