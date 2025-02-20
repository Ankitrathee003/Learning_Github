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
    

    def merge(left, right):
        dummy = Node(0)  #creating a dummy Node with data=0
        curr = dummy
        
        while left and right:         #(if both have some data)
            if left.data < right.data:
                curr.next = left
                left = left.next
            else:
                curr.next = right
                right = right.next
            curr = curr.next
        
        # Append the remaining nodes of left or right (if any)
        curr.next = left or right
        
        return dummy.next  # we are returning dummy.next as in starting we have added 0 to dummy linked list
    

    def merge_sort(head): 
        if not head or not head.next:   #(if at least one is empty will return head or head==none or head.next==none)
            return head
        
        # Find the middle of the linked list
        slow, fast = head, head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Split the linked list into two halves
        mid = slow.next
        slow.next = None
        
        # Recursively sort the two halves
        left = Node.merge_sort(head)
        right = Node.merge_sort(mid)
        
        # Merge the sorted halves
        return Node.merge(left, right)

# Example usage:
# Create a sample linked list: 4 -> 2 -> 1 -> 3
head=Node.takeInput()


# Sort the linked list using Merge Sort
sorted_head = Node.merge_sort(head)
Node.printLL(sorted_head)
    








