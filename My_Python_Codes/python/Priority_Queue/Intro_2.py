## we will implement priority Queue using Heap as it is easy to implement
## Heap can be implemented using any data structure
### Remember that Heap has least complexity in all 3 operations in case of BST

#### Heap has all properties of complete Binary TREE
# In a complete Binary Tree all levels should be completetely Filled except the last level
##  Elements should be inserted from left to right


## for a complete Binary Tree height=h and let number of nodes=n
#                       Minimum        <= h <=     Maximum
# so:   2^0+2^1+2^2+2^3-------+2^(h-1) +1 <= n <=2^0+2^1+2^2+2^3-------+2^h
        # so after solving this 
        #   n=>(2^h-1)   and   n<=(2^(h+1)-1)
        ## so from here  h will be always in limits of log(n) order