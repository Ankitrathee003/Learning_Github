# INPUT TO TREE
# In Post Order first childs will be printed or handled than the parent  node will be handled

 # we are doing with pre order strategy  where Root Node will be handled first than its childs 


# In Order  ==  1.Root.Left      2. Root          3.Root.Right
# Pre Order ==  1.Root           2. Root.Left     3.Root.right
# Post Order==  1.Root.left      2.Root.right     3.Root
import queue
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

    def printInorder(root):   # 1. left      2.Root      3.Right
        if root==None:
            return 
        BinaryTreeNode.printInorder(root.left)
        print(root.data)
        BinaryTreeNode.printInorder(root.right)
        # print(root.data)   # if we will activate this line instead of above it will become post order



    def printLevelOrder(root):
        q = queue.Queue()
        if root is None:
            return

        q.put(root)
        while not q.empty():
            current_node = q.get()
            print(current_node.data)

            if current_node.left:
                q.put(current_node.left)
            if current_node.right:
                q.put(current_node.right)



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
    
    def LevelWiseInput():
        q=queue.Queue()
        print("Enter Root ")
        rootData =int(input())
        if (rootData==-1):
            return None
        root=BinaryTreeNode(rootData)
        q.put(root)
        while (not (q.empty())):
            current_node=q.get()
            print("enter left child of " , current_node.data )
            leftchildData=int(input())
            if leftchildData!=-1:
                leftchild=BinaryTreeNode(leftchildData)
                current_node.left=leftchild
                q.put(leftchild)
                
            print("enter right child of " , current_node.data )
            rightchildData=int(input())    
            if rightchildData!=-1:
                rightchild=BinaryTreeNode(rightchildData)
                current_node.right=rightchild
                q.put(rightchild)
        return root
        






# root=BinaryTreeNode.treeInput()
root=BinaryTreeNode.treeInput()
BinaryTreeNode.printInorder(root)


# root=BinaryTreeNode.LevelWiseInput()
BinaryTreeNode.printTreeDetailed(root)
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")


# SAMPLE INPUT

# 1
# 2
# 3
# 5
# 7
# -1
# -1
# -1
# 6
# -1
# 4
# -1
# -1
# 9
# -1
# -1

# Corresponding Output

# 1:  L 2,  R 9
# 2:  L 3,  R 4
# 3:  L 5,  R 6
# 5:  L 7,  Number of Nodes are:  8
