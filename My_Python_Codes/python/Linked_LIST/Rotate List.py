class Node:
    def __init__(self,data):
        self.data=data
        self.next=None

    def takeinput():
        x=input("enter the elements seprated by comma ")
        inputList=[i for i in x.split(",")]
        head =None
        for currentData in inputList:

            if currentData == "-1":
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
    
    def length(head):
        temp = head
        count = 0
        while temp is not None:
            count+=1
            temp=temp.next
        return count
    
    def printLL(head):
        temp = head
        while temp is not None:
            print(temp.data)
            temp = temp.next



    def rotateRight(head , k) :
        count=0
        temp=head
        
        while temp and temp.next:
            temp=temp.next
            count+=1
        k=k%(count+1)
        if count!=0 and  k!=0:
            tail=temp
            counting=0
            while counting<=k:
                shift=head
                head=head.next
                tail.next=shift
                shift.next=None
                tail=shift
                
                counting+=1
        return(head)
    
head=Node.takeinput()

head=Node.rotateRight(head,1)
Node.printLL(head)
