# improvement over complexity
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
def takeInput():
    x=input("Enter the list element seprated by comma  ")
    inputList=[i for i in x.split(",")]
    print(len(inputList),inputList)

    head =None
    for currentData in inputList:
        if currentData ==-1:
            break
        newNode=Node(currentData)
        if head is None:
            head =newNode
            tail=newNode
        else:
            tail.next=newNode   # Now we need not to traverse complete linked list for assigning address of next node
            tail=newNode
    return(head)