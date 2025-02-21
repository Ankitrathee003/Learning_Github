# Input for linked list
# [1,2,3,4,5,-1] actually  we have only 5 elements [1,2,3,4,5]
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
        print(currentData)
        if head is None:
            head =newNode
        else:
            current=head                    # current is an address
            while current.next is not None: # will continue till a fresh node is not reached
                current=current.next
            current.next=newNode            # storing the address of forward node to next of previous node 

    return(head)
takeInput()
  
# Time complexity of above code is of order n^2 
# as we have to traverse for adding reference of 1st element 0 times in while loop
# for 2nd element traverse 1 time in while loop
# for 3rd element we have to traverse for 2 time in while loop



