# BST =Binary Search Tree
# It is used for searching the elements in less time complexity
# in array it takes O(n) here we can reduce it to O(log(n)) or O(h) where h is height of tree
# if height of binary tree is h than nodes are 2^h-1=n from here h=log(n+1) with base 2 (so h and log(n) are nearly same here)
# In our case we will assume that Left tree has smaller elements and right tree has grater than or equal to root elements
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
        

root=BinaryTreeNode.treeInput()
BinaryTreeNode.printTreeDetailed(root)
print("Elements in between function output: ")
BinaryTreeNode.searchInBetween(root,2,9)
print(f"is Searched element in Tree: {BinaryTreeNode.search(root,9)}")
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
print(f"depth of tree is : {BinaryTreeNode.height_of_tree(root)}")