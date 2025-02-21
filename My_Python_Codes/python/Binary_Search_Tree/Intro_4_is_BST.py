import math
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def printTree(root):
        if root==None:
            return
        print(root.data)
        BinaryTreeNode.printTree(root.left)
        BinaryTreeNode.printTree(root.right)

    def printTreeDetailed(root):
        if root==None:
            return
        # we are doing with pre order strategy  where Root Node will be printed first than its childs 
        if root.left or root.right:
            print(root.data,end=":  ")
        if root.left:
            print("L",root.left.data,end=",  ")
        if root.right:
            print("R" ,root.right.data)
        BinaryTreeNode.printTreeDetailed(root.left)
        BinaryTreeNode.printTreeDetailed(root.right)

    def treeInput():
        rootData=int(input())
        if rootData==-1:  # put -1 to terminate the node
            return None
        root=BinaryTreeNode(rootData)
        leftTree=BinaryTreeNode.treeInput()
        rightTree=BinaryTreeNode.treeInput()
        root.left=leftTree
        root.right=rightTree
        return root
    
    def numNodes(root):
        if root==None:
            return 0
        leftCount=BinaryTreeNode.numNodes(root.left)
        rightCount=BinaryTreeNode.numNodes(root.right)
        return 1+leftCount+rightCount

    def largestNum(root):
        if root ==None:
            return -1  # ideally we should return -inf
        leftLargest=BinaryTreeNode.largestNum(root.left)
        rightLargest=BinaryTreeNode.largestNum(root.right)
        return(max(leftLargest,rightLargest,root.data))
    def height_of_tree(root):
        if root==None:
            return 0
        leftheight=BinaryTreeNode. height_of_tree(root.left)
        rightheight=BinaryTreeNode. height_of_tree(root.right)
        return 1+max(leftheight,rightheight)
    #######################################################################################################################
    #######################################################################################################################
    #################################################  BST BST BST BST BST BST  ###########################################

    def search(root,x):
        if root==None:
            return False
        if root.data==x:
            return True
        elif root.data>x:
            return BinaryTreeNode.search(root.left,x)
        else:
            return(BinaryTreeNode.search(root.right,x))
        
    ## we have to return all elements equal or in between x,y
    def searchInBetween(root,x,y):  
        if root==None:
            return
        if root.data>y: # if root value is even greater than our last value of interval it means we have to search in smaller values than root i.e Left side
            BinaryTreeNode.searchInBetween(root.left,x,y)
        elif root.data<x:
            BinaryTreeNode.searchInBetween(root.right,x,y)
        else:
            print(root.data)
            BinaryTreeNode.searchInBetween(root.left,x,y)
            BinaryTreeNode.searchInBetween(root.right,x,y)

    def findMin(root):   ### ITERATIVELY   we know that farthest left node will be smallest
        if root==None:
            return None
        smallest=root.data
        while root.left:
            smallest=root.left.data
            root=root.left
        return smallest
    
    def findMax(root):   
        if root==None:
            return None
        maximum=root.data
        while root.right:
            maximum=root.right.data
            root=root.right
        return maximum


    
    def CreateBST(nums):  ## we are giving nums to be strictly sorted here
        mid=math.floor(len(nums)/2)
        root=BinaryTreeNode(nums[mid])
        leftarray=nums[0:mid]
        rightarray=nums[mid+1:]
        if leftarray:
            root.left=BinaryTreeNode.CreateBST(leftarray)
        if rightarray:
            root.right=BinaryTreeNode.CreateBST(rightarray)
        return root
    

    ############ WRONG CODE##################
    # because here we are just checking for immediate left and immediate right  
    # while we need to check for absolute max in left which should be smaller than root.data and absolute Minimum on right side should be greater than root.data.
    def IsBstWrong(root):  #  WE will keep equal elements on right side
        if root==None:
            return True   ###  WRONG CODE  ###
        if root.left:
            if root.left.data>=root.data:
                return False
        if root.right:
            if root.right.data<root.data:
                return False
        left=BinaryTreeNode.IsBstWrong(root.left)    ###  WRONG CODE  ###
        right=BinaryTreeNode.IsBstWrong(root.right)  ###  WRONG CODE  ###
        return (left and right)
    

    def IsBstCorrect(root):  #This has the order of T(n)=2*O(n)+2*T(n-1) it means over all complexity is O(n^2)
        if root==None:
            return True
        if root.left:
            if root.data<=BinaryTreeNode.findMax(root.left):
                return False
        if root.right:
            if root.data>BinaryTreeNode.findMin(root.right):
                return False
        left=BinaryTreeNode.IsBstWrong(root.left)   
        right=BinaryTreeNode.IsBstWrong(root.right) 
        return (left and right)
        
    def isBST2(root):   ### recrence relation is T(n)=k+2*T(n/2)  which has overall complexity of O(n)
        if root==None:
            return 100000,-100000,True
        leftMin,leftMax,isLeftBST=BinaryTreeNode.isBST2(root.left)
        rightMin,rightMax,isRightBST=BinaryTreeNode.isBST2(root.right)
        minimum=min(leftMin, rightMin, root.data)
        maximum=max(leftMax,rightMax,root.data)
        isTreeBST=True
        if root.data <=leftMax or root.data>rightMin:
            isTreeBST=False
        if not(isLeftBST) or not(isRightBST):
            isTreeBST=False
        return (minimum,maximum,isTreeBST)
    
    ## now wee will check each node for to be in range for Left and Right depending upon root.data
    def isBST3(root,min_range,max_range): 
        if root==None:
            return True
        if root.data<min_range or root.data>max_range:
            return False
        isleftwithinconstraints=BinaryTreeNode.isBST3(root.left,min_range,root.data-1)
        isrightwithinconstraints=BinaryTreeNode.isBST3(root.right,root.data, max_range)
        return( isleftwithinconstraints and isrightwithinconstraints )
        
        


            

            
        
            


            




        
        

root=BinaryTreeNode.treeInput()
# BinaryTreeNode.printTreeDetailed(root)
# print("Elements in between function output: ")
# BinaryTreeNode.searchInBetween(root,2,9)

# nums=[i for i in range(8)]
# root=BinaryTreeNode.CreateBST(nums)
BinaryTreeNode.printTreeDetailed(root)
# print(f"Checking Just Immediate Left And Right Just for practice : {BinaryTreeNode.IsBstWrong(root)}")
# print(f"Checking BST Coorrectly by taking max and min:{BinaryTreeNode.IsBstCorrect(root)}")

print(f"Checking BST2: {BinaryTreeNode.isBST2(root)}")
print(f"Checking BST3:{BinaryTreeNode.isBST3(root,-10000,10000)}")



print(f"smallest element in tree is :{BinaryTreeNode.findMin(root)}")
print(f"is Searched element in Tree: {BinaryTreeNode.search(root,9)}")
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
print(f"depth of tree is : {BinaryTreeNode.height_of_tree(root)}")