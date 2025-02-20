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
    
    def LargestNumIterativily(root):     ## Using Queue similar to Level Order traversal we are checking for max instead of adding root.data to result
        if root ==None:
            return
        q=queue.Queue()
        q.put(root)
        maximum=0
        while not q.empty():
            root=q.get()
            maximum=max(maximum,root.data)
            if root.left: 
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return(maximum)
    
    def sumOfLeftLeaves(root):
        if root == None:
            return 0

        # Check if the left child is a leaf node
        if root.left != None and root.left.left == None and root.left.right == None:
            leftSum = root.left.data
        else:
            leftSum = BinaryTreeNode.sumOfLeftLeaves(root.left)
        rightSum = BinaryTreeNode.sumOfLeftLeaves(root.right)

        return leftSum + rightSum
    
    def sumLeftNodes(root):
        if root == None:
            return 0
        sum = 0    # as we move down sum will go to stack and when we reach to bottom it will start adding (LIFO)
        if(root.left):
            sum = root.left.data
        left = BinaryTreeNode.sumLeftNodes(root.left)
        right = BinaryTreeNode.sumLeftNodes(root.right)
        return left+right+sum







# By Inputing without functioon
btn1=BinaryTreeNode(1)
btn2=BinaryTreeNode(4)
btn3=BinaryTreeNode(5)
bt4=BinaryTreeNode(9)
bt5=BinaryTreeNode(10)
bt6=BinaryTreeNode(15)
bt7=BinaryTreeNode(11)
bt8=BinaryTreeNode(7)
    
    
btn1.left=btn2                             
btn1.right=btn3    
btn2.left=bt4
btn2.right=bt5   
bt4.right=bt6   
bt4.left=bt7    
btn3.left=bt8         

root=btn1
# BinaryTreeNode.printTreeDetailed(btn1)
# BinaryTreeNode.printTreeDetailed(btn1)




print(BinaryTreeNode.sumLeftNodes(root))
# BinaryTreeNode.printTreeDetailed(root)
# print(f"sum of Left Leaves is {BinaryTreeNode.sumOfLeftLeaves(root)}")
# print(sum)
# print(BinaryTreeNode.LargestNumIterativily(root))
# print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
# print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")
