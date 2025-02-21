# we use enumerate function with for loop to track position of our item in iterable 
names=['abc','ankit','rathee']
# position=0
# for i in names:
#     print(f'{position} -----> {i}')
#     position+=1

#using enumerate function
# value of posn will keep updating automatically
m=[22,3,4,56,453,33213]
# for i in enumerate(m):
#     print(i)          #OUTPUT : (0, 22),(1, 3),(2, 4),(3, 56),(4, 453),(5, 33213)

# we can give variable  with name posn to indexing
for  i,posnh in enumerate(names):
    print(f'{posnh} -----> {i}') 



#returning index of element using enumerate function
# list=['a','ab','abc','abcd','abcde','abcdef']
# a="abcde"
# def in_list(a,list):
#     for i,v in enumerate(list):
#         if v==a:
#             return(i)
#     return(-1)                
# print(in_list(a,list)) 