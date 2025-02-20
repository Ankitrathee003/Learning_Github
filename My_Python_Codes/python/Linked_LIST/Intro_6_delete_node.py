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
            if head is None:
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
        

    


    def deletetAtI(head,i):
        if i<0 or i>Node.length (head):
            return head
        
        count=0
        prev=None
        current=head

        while count<i:
            prev=current
            current=current.next
            count+=1
        prev.next=current.next
        return head 
    

    # def delatirec(head,i):   
    #     if i==1:
    #         head.next=(head.next).next
    #         return(head)
    #     elif i==0:
    #         head=head.next
    #         return(head)
    #     else:
    #         delte=delattr(head.next,i-1)
    #         head.next=delte
    #         return(head)



            

head=Node.takeinput()
Node.delatereci(head,3)
Node.printLL(head)