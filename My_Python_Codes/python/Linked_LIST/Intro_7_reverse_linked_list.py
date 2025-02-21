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
    

    def reverselistitre(head):  # reversing linked list iterratively 
        # ahead=None
        previous=None
        ahead=head
        while (head.next)!=None:
            ahead=head.next
            head.next=previous 
            previous=head
            head=ahead
        head.next=previous   # after coming out of loop head and ahead  both are pointing to last node but previous is one step behind and link of previous to head has also break so now will connect head/ahead to previous
        return(ahead)          # in both lines we can use either head or ahead as both are pointing to same last node after coing out of loop
    

# reversing linked list recursively  of order =   O(n^2)
    def reversal(head):
        if head is None or head.next is None:   # head is none to written first as if it turns out to be false head.next will give error
            return head
        smallhead=Node.reversal(head.next)
        current=smallhead     
        # print(smallhead .data)             # here we can check by printing smallheadd which is pointing to last element of linked list      
        while current.next is not None:    # once we get the reverse linked list we are traversing to the end of reversed linked list where we have linked None at end
            current=current.next
        current.next=head                     
        head.next=None
        return smallhead
    


# reversing linked list of order = O(n)
# her we will not keep the small head at end of each iteration we will mpve that as well
    def reverse_linked_list_recursive(head):
        # Base case: if the list is empty or has only one node
        if head is None or head.next is None:
            return head

        # Recursive call to reverse the rest of the list
        reversed_list = Node.reverse_linked_list_recursive(head.next)

        # Adjust the pointers to reverse the current node
        head.next.next = head
        head.next = None

        return reversed_list





y=Node.takeInput()
# x=rll(y)


# x=Node.reverselistitre(y)
# Node.printLL(x)

z=Node.reversal(y)
Node.printLL(z)





