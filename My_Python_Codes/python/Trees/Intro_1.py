# Trees can be of many types 
# Binary Trees are those which can have at max 2 child nodes 

# leafs are nodes without childern
   
class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

    def printTree(root):
        if root==None:
            return
        print(root.data)          # PreOrder Traversal  1.Root 2.Left 3.Right
        BinaryTreeNode.printTree(root.left)
        BinaryTreeNode.printTree(root.right)

    def printTreeDetailed(root):
        if root==None:
            return
        if root.left or root.right:
            print(root.data,end=":  ")
        if root.left:
            print("L",root.left.data,end=",  ")
        if root.right:
            print("R" ,root.right.data)
        BinaryTreeNode.printTreeDetailed(root.left)
        BinaryTreeNode.printTreeDetailed(root.right)
        
btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(4)
btn3=BinaryTreeNode(5)
bt4=BinaryTreeNode(9)
bt5=BinaryTreeNode(10)
bt6=BinaryTreeNode(15)
    
    
btn1.left=btn2                             
btn1.right=btn3    
btn2.left=bt4
btn2.right=bt5   
bt4.right=bt6                

# BinaryTreeNode.printTreeDetailed(btn1)
BinaryTreeNode.printTree(btn1)
BinaryTreeNode.printTreeDetailed(btn1)
    


