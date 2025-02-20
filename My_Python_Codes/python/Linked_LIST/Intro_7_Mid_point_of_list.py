class Node:

    def __init__(self,data):
        self.data=data
        self.next=None


    def takeInput():
        x=input("enter the elements seprated by comma ")
        inputList=[i for i in x.split(",")]

        head =None 
        for currentData in inputList:
            if currentData ==-1:
                break
            newNode=Node(currentData)

            if head is None:
                head =newNode
            else:
                current=head   # current is an address
                while current.next is not None: # will continue till a fresh node is not reached
                    current=current.next
                current.next=newNode      # storing the address of forward node to next of previous node 
        return(head)
    
        # to print LInked List
    def printLL(head):
        temp=head
        i=0
        while temp is not None:
            print(temp.data)
            temp=temp.next
    
    
    def mid_of_list(slow,fast):

        while (fast.next)!=None or (fast.next.next)!=None:
            slow=slow.next
            fast=fast.next.next

            if  (fast.next)==None or (fast.next.next)==None: 
                return(slow.data)  # for even no. of elements it will return first one out of of two middles.
      


        


head=Node.takeInput()
print(Node.mid_of_list(head,head))
            