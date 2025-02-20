# inserting element at ith position


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
Node.printLL(head)


head=Node.insertAtI(head,4,25)   # here indexing is starting from 0 so  basically elements will inset at 5th position
Node.printLL(head)

# print(Node.length(head))
# i=0
# x=Node.length(head)
# while i<x:
#     print(head.data)
#     head=head.next
#     i+=1


    








