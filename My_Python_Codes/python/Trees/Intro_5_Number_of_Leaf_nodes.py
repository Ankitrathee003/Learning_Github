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
        if root==None: # to take care of empty tree so that in numLeafleft or numLeafright it do not show none.left   type error
            return 0
        if root.left==None and root.right==None:
            return 1
        numLeafLeft=BinaryTreeNode.numLeafNodes(root.left)
        numLeafright=BinaryTreeNode.numLeafNodes(root.right)
        return numLeafLeft+numLeafright

    def numLeafNodesIteratively(root):
        count=0
        if root==None:  # This condition is required only at starting of function whether there is any root  or Not
            return 
        q=queue.Queue()
        q.put(root)
        while not q.empty():
            root=q.get()
            if  root.left is None and  root.right is None:
                count+=1
            if root.left:
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return count
        
            
        
        

root=BinaryTreeNode.treeInput()
BinaryTreeNode.printTreeDetailed(root)
print(f"Number of Leaf Nodes calculated Iteratively using queue are:  {BinaryTreeNode.numLeafNodesIteratively(root)}")
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
print(f"height of tree is : {BinaryTreeNode.height_of_tree(root)}")
print (f"Number of Leaf Nodes are {BinaryTreeNode.numLeafNodes(root)}")