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

    def swapNodes(head, k):


        temp=head

        count=1
        while  temp.next:
            count+=1
            temp=temp.next
        n=count

        if k>n/2:
            k=n-k+1
        last=n-k+1



        if k== (1 or n):   # when 1st and last node are to be replaced
            temp=head
            s=head
            e=head
            ns=head.next
            count=1
            while count!=last:
                pe=e
                e=e.next
                count+=1
            
            print(temp.data,ns.data,pe.data,e.data)
            temp.next=None
            e.next=ns
            pe.next=head
        
            return(e)
        
        elif k==last :
            return(head)
        
        elif k==n/2 :
            count=1
            prev=head
            while count!=k-1:
                prev=prev.next
                count+=1
            s=prev.next
            # ne=e.next
            prev.next=s.next
            s.next=s.next.next
            prev.next.next=s
            return(head)
            
        
        else:
            temp=head
            s=head
            ps=None
            e=head
            pe=None

            count=1
            while count!=k:
                ps=s
                s=s.next
                count+=1
                
            if s.next:
                ns=s.next

            count=1
            while count!=last:
                pe=e
                e=e.next
                count+=1

            if e.next:
                ne=e.next

            # print(ps.data,s.data,pe.data,e.data)
            s.next=ne
            ps.next=e
            e.next=ns
            pe.next=s
            return head


head=Node.takeinput()
Node.printLL(head)

head=Node.swapNodes(head,4)
Node.printLL(head)
