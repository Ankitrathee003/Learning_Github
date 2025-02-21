class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
        self.previous=None

    def takeinput():
        x=input("enter the elements of Doubly linked list seprated by comma ")
        inputList=[i for i in x.split(",")]
        head =None
        previous=None
        for currentData in inputList:

            if currentData == "-1":
                break
            newNode=Node(currentData)
            if head is None:
                head =newNode
                head.previous=None

            else:
                current=head   # current is an address
                while current.next is not None: # will continue till a fresh node is not reached
                    current=current.next
                current.next=newNode      # storing the address of forward node to next of previous node 
                newNode.previous=current
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
    
    def printLL_reverse(head):
        temp = head
        while temp.next is not None:
            temp=temp.next
        while temp!=head:       # for printing last element to second element
            print(temp.data)
            temp = temp.previous
        print(temp.data)        # for printing initial head value
    
    def insertAtI(head,i,data):
        if i<0 or i>Node.length (head):
            return head
        count=0
        prev=None
        current=head

        while count<i:
            prev=current
            current=current.next
            count+=1
        
        newNode=Node(data)   

        if prev is not None:   # agar hum while loop se aa rahe h to
            prev.next=newNode
            # print(prev.data)
            # print(current.data)
        else:                   # agar hum while loop ko skip karke aa rahe h to means wants to insert at starting of node
            head=newNode    
        newNode.next=current

        return head 

head=Node.takeinput()
# Node.printLL(head)
Node.printLL_reverse(head)