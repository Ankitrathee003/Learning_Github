## generic trees can have as many as Childrens as we want:

import queue
class TreeNode:
    def __init__(self,data):
        self.data=data
        self.children=list()

    def printTree(root):    ## ek baar jis Node me Ghuse ga fir Ghusta hi chla gayega Leaf Node tak Fir ulta AAega print karte hue
        ## Not a base case but an edge case
        if root==None:
            return 
        print(root.data)
        for child in root.children():  ## here in this code we will not get to know whose children is whom 
            TreeNode.printTree(child)   

    def printTreeDetailed(root):
        if root==None:
            return 
        print(root.data, ":" ,end="")
        for child in root.children:
            print(child.data,",",end="")
        print()  # just to put next root  in next line
        for child in root.children:
            TreeNode.printTreeDetailed(child)

    def takeTreeInput():
        print("Enter root Data")
        rootData=int(input())
        if rootData==-1:
            return None
        root=TreeNode(rootData)
        print("Enter number of children for ",rootData)
        childrenCount=int(input())
        for i in range(childrenCount):
            child=TreeNode.takeTreeInput()
            root.children.append(child)
        return root
      
    def takeTreeInputLevelWise():  ## Level order Tree input ITERATIVELY
        q=queue.Queue()
        print("Enter root")
        rootData=int(input())
        if rootData==-1:
            return None
        root=TreeNode(rootData)
        q.put(root)
        while not q.empty():
            current_node=q.get()
            print("Enter num of children for ", current_node.data)
            numchildren=int(input())
            for i in range(numchildren):
                print("Enter next child for ", current_node.data)
                childData=int(input())
                child=TreeNode(childData)
                current_node.children.append(child)
                q.put(child)
        return root

    def numNodes(root):
        if root==None:
            return 0
        count=1
        for child in root.children:
            count=count+TreeNode.numNodes(child)
        return count











# n1=TreeNode(5)
# n2=TreeNode(2)
# n3=TreeNode(9)
# n4=TreeNode(8)
# n5=TreeNode(7)
# n6=TreeNode(15)
# n7=TreeNode(1)
# n8=TreeNode(50)
# n1.children.append(n2)
# n1.children.append(n3)
# n1.children.append(n4)
# n1.children.append(n5)
# n1.children.append(n6)
# n1.children.append(n7)
# n2.children.append(n8)




# root_node = TreeNode(None)
# root = TreeNode.takeTreeInput()
# node_count = TreeNode.numNodes(root)
# print(node_count)
# TreeNode.printTreeDetailed(root)
# root=TreeNode.takeTreeInputLevelWise()
# TreeNode.printTreeDetailed(root)
