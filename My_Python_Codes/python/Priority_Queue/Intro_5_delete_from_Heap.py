## delete from heap

## DELETING FROM A MIN HEAP

## we have to take care of CBT properties as well as Heap order property while deleting
# So we are deleting the smallest element from heap for that top most node will be deleted in case of Min heap 
## Now Position of top most Node is Blank it will be taken by lowest lying Node in Heap
## After that We will start comparing from top 
## First Top 3 members(Top Node +2 childs)  will be compared and Min of these three will take the Top most node
## and this comparsion and swapping will continue untill we reach bottom of Heap


##                     MIN HEAP


#                       10                                              
#                    /     \
#                   /       \
#                  /         \
#                 20          30
#                /  \         / \
#               /    \       /   \
#              40     60    35    50
#             / 
#            /
#           45



#    REMOVE TOP MOST ELEMENT FROM TOP AS IT IS MINIMUM AND PUT THE LAST ELEMENT OF NODE AT TOP WHICH IS 45
#                       45                          
#                    /      \
#                   /        \
#                  /          \
#                 20           30
#                /  \         /  \
#               /    \       /    \
#              40     60    35     50




#  START Swapping the elements first compare top 3 elements(45,20,30) and than swap min(20) with top most (45)

#                       20                          
#                    /     \
#                   /       \
#                  /         \
#                 45          30
#                /  \         /  \
#               /    \       /    \
#              40     60    35     50


## AS WE HAVE SWAPED TO LEFT SO WILL NOW COMPARE THE 3 ELEMENTS FROM LEFT NODE(45,40,60) AND WILL MAKE MIN(40) OF THESE THREE A PARENT NODE OF REMAINING TWO

#                       20                          
#                    /     \
#                   /       \
#                  /         \
#                 40          30
#                /  \         /  \
#               /    \       /    \
#              45     60    35     50


#     NOW THE COMPLETE BINARY TREE PROPERTIES AS WELL AS HEAP ORDER PROPERTIES ARE SATISFIED 
##    MEANS SMALLEST IS AT TOP MOST AND TREE IS BALANCED AT LEAST UP TO DEPTH OF N-1 AND THAN REMAINING NODES AT NTH DEPTH ARE FILLED FROM  LEFT TO RIGHT


###   SAME CAN BE DONE WITH MAX HEAP



