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
    m=0
    def largestNum(root):
        # if root ==None:
        #     return float('-inf')
        # leftLargest=BinaryTreeNode.largestNum(root.left)
        # rightLargest=BinaryTreeNode.largestNum(root.right)
        # return(max(leftLargest,rightLargest,root.data))
        if not root:
            return 
        BinaryTreeNode.largestNum(root.left)
        BinaryTreeNode.largestNum(root.right)
        m=max(m,root.val)
        return m

        
        








    
    def LargestNumIterativily(root):     ## Using Queue similar to Level Order traversal we are checking for max instead of adding root.data to result
        if root ==None:
            return
        q=queue.Queue()
        q.put(root)
        maximum=float("-inf")
        while not q.empty():
            root=q.get()
            maximum=max(maximum,root.data)
            if root.left: 
                q.put(root.left)
            if root.right:
                q.put(root.right)
        return(maximum)
            
    
        





root=BinaryTreeNode.treeInput()
BinaryTreeNode.printTreeDetailed(root)
print(BinaryTreeNode.LargestNumIterativily(root))
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
# print(f"maximum of tree is : {BinaryTreeNode.largestNum(root)}")



# By Inputing without functioon
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
# BinaryTreeNode.printTreeDetailed(btn1)
