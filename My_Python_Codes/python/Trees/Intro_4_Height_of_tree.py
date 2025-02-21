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
    






root=BinaryTreeNode.treeInput()
BinaryTreeNode.printTreeDetailed(root)
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
print(f"depth of tree is : {BinaryTreeNode.height_of_tree(root)}")