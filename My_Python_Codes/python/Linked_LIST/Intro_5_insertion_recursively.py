# inserting element at i th position


class Node:
    def __init__(self,data):
        self.data=data
        self.next=None




    def takeinput():
        x=input("Enter the elements of linked list seprated by comma: ")
        inputList=[i for i in x.split(",")]
        head =None


        # To create links in Linked List
        for currentData in inputList:
            
            if currentData ==-1:
                break
            newNode=Node(currentData)
            if head is None:                    # if means we want to insert at position greater then the length of linked list
                head =newNode 
            else:
                current=head                    # current is an address
                while current.next is not None: # will continue till a fresh node is not reached
                    current=current.next
                current.next=newNode            # storing the address of forward node to next of previous node 
        return(head)
    

# To find length of linked list
    
    def length(head):
        temp = head
        count = 0
        while temp.next is not None:
            count+=1
            temp=temp.next
        return count
    
    # to print LInked List
    def printLL(head):
        temp=head
        i=0
        while temp.next is not None:
            print(temp.data)
            temp=temp.next


    


    def insertAtIR(head,i,data):
        if i<0:
            return head
        
        if i==0:                     # to make link from end
            newNode=Node(data)        # in this line we are  creating a new node with the given data,
            newNode.next=head
            return newNode
        
        if head is None:
            return None
        

        smallHead = Node.insertAtIR(head.next,i-1,data)
        head.next=smallHead          # to make link from front side 
        return head
    

    # printing ith node
    def printInode(head,i):          # i starting from 0
        j=0
        temp=head
        while j<i:
            temp=temp.next
            j+=1
        print(temp.data)


    


head = Node.takeinput()
# print(Node.length(head))
# Node.printLL(head)

head=Node.insertAtIR(head,2,89)
# Node.printLL(head)
# print(Node.length(head))


# printing elements of linked list after inserting at ith position
for i in range(Node.length(head)+1):
    Node.printInode(head,i)








