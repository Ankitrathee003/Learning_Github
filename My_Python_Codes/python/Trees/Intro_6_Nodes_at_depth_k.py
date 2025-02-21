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
    
    def numLeafNodes(root):
        if root==None: # to take care of empty tree and returning  0 to numLeafLeft,numLeafright when they are at End  so that in numLeafleft or numLeafright it do not show none.left  type error
            return 0
        if root.left==None and root.right==None:
            return 1
        numLeafLeft=BinaryTreeNode.numLeafNodes(root.left)
        numLeafright=BinaryTreeNode.numLeafNodes(root.right)
        return numLeafLeft+numLeafright
    
    # printing by continuouusly reducing the K value
    def printDepthK(root,k):
        if root==None:
            return
        if k==0:
            print(root.data)
            return
        BinaryTreeNode.printDepthK(root.left,k-1)  # taking root node as 0
        BinaryTreeNode.printDepthK(root.right,k-1)

    # printing by taking care of k and current depth :
    def printDepthKV2(root,k,d=0):
        if root==None:
            return
        if k==d:
            print(root.data)
            return
        BinaryTreeNode.printDepthKV2(root.left,k,d+1)  # k is the depth at which we want to print d is the depth where we are currently,eachh timme we are going one step down
        BinaryTreeNode.printDepthKV2(root.right,k,d+1)


        
        

root=BinaryTreeNode.treeInput()
BinaryTreeNode.printTreeDetailed(root)
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
print(f"height of tree is : {BinaryTreeNode.height_of_tree(root)}")
print (f"Number of Leaf Nodes are {BinaryTreeNode.numLeafNodes(root)}")
BinaryTreeNode.printDepthK(root,2)
BinaryTreeNode.printDepthKV2(root,2)  # we need not to pass initial depth which is initialise 0 in function