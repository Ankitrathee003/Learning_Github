class BinaryTreeNode:
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None

class BST:
    def __init__(self):
            self.root=None
            self.numNodes=0
    def printTreeDetailed(self,root):
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

## As we are not using the root we can not call on root.left and root.right we will use helper function 
    def isPresentHelper(self,root,data):        
        if root==None:
            return False
        if root.data==data:
                return True
        if root.data>data:## As we are not using the root we can not call on root.left and root.right
                return BST.isPresentHelper(root.left,data)
        else:
                return BST.isPresentHelper(root.right,data)
    
    def isPresent(self):
        return BST.isPresentHelper(self.root) 

    def isPresent(self,data):
        return BST.isPresentHelper(self.root,data) 
    
    def insertHelper(self,root,data):
        if root==None:
              node=BinaryTreeNode(data)
              return node
        if root.data>data:
              root.left=self.insertHelper(root.left,data)
              return root
        else:
              root.right=self.insertHelper(root.right,data)
              return root
        
          
                  

    def insert(self,data):
          self.numNodes+=1
          self.root = self.insertHelper(self.root,data)

    def min(self,root):
        if root==None:
            return 100000
        if root.left==None:
            return root.data
        return self.min(root.left)
         
         


    def deleteDataHelper(self,root,data):
        if root==None:
            return False,None
        if root.data<data:
            deleted,newRightNode=self.deleteDataHelper(root.right,data)
            root.right=newRightNode
            return deleted,root
        if root.data>data:
            deleted,newLeftNode=self.deleteDataHelper(self.root,data)
            root.left=newLeftNode
            return deleted,root
        
        ## root is leaf
        if root.left==None and root.right==None:
             return True,True
        
        ## root has one child
        if root.left==None:
             return True,root.right
        if root.right==None:
             return True,root.left
        
        ## root has two child
        replacement=min(root.right)
        root.data=replacement
        deleted,newRightNode=self.deleteDataHelper(root.right,replacement)
        root.right=newRightNode
        return True,root             


        
              
    def deletedata(self,data):
          deleted,newroot=self.deletedataHelper(self.root,data)
          if deleted:
            self.numNodes-=1
          self.root=newroot
          return deleted
b=BST()
b.insert(10)
b.insert(5)
b.insert(7)
b.insert(6)
b.insert(8)
b.insert(12)
b.insert(11)
b.insert(15)
b.printTreeDetailed()
print(b.count())


    
    
            
        



    
    