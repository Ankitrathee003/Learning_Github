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
    
    def LevelWiseInput():       # we have to use queue here as the element which is coming first will be asked for its chilren in same order instead of asking Left first in recursion
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
    
    # For Given preorder and In order sequence steps:
    #    1. find the root
    #    2. find in order of left and right Subtree
    #    3. Find Pre order of left and right and subtree
    #    4. Use Recursion to build left and right subtree



    #     Pre means DLR 
    def buildTreeFromPreIn(pre, inorder):
        if len(pre)==0:
            return None
        rootData=pre[0]
        root=BinaryTreeNode(rootData)
        rootIndexInOrder=-1
        for i in range (0,len(inorder)):
            if inorder[i]==rootData:
                rootIndexInOrder=i
                break
        if rootIndexInOrder==-1:  # If still root index is -1 it means there is some problem
            return None

        leftInorder=inorder[0:rootIndexInOrder]
        rightInorder=inorder[rootIndexInOrder+1:]

        lenLeftsubtree=len(leftInorder)
        leftPreorder=pre[1:lenLeftsubtree+1]
        rightPreOrder=pre[lenLeftsubtree+1:]

        leftChild=BinaryTreeNode.buildTreeFromPreIn(leftPreorder,leftInorder)
        rightChild=BinaryTreeNode.buildTreeFromPreIn(rightPreOrder,rightInorder)

        root.left=leftChild
        root.right=rightChild
        return root
    
    def buildTreeFromPreIn2(self, preorder, inorder):  #### short code of above longer code
            if inorder:
                ind = inorder.index(preorder.pop(0))
                root = BinaryTreeNode(inorder[ind])
                root.left = self.buildTree(preorder, inorder[0:ind])
                root.right = self.buildTree(preorder, inorder[ind+1:])
            return root
        







# root=BinaryTreeNode.treeInput()
# root=BinaryTreeNode.LevelWiseInput()
pre=[1,2,4,5,3,6,7]
Inorder=[4,2,5,1,6,3,7]
root=BinaryTreeNode.buildTreeFromPreIn(pre,Inorder)
BinaryTreeNode.printTreeDetailed(root)
print(f"Number of Nodes are:  {BinaryTreeNode.numNodes(root)}")
