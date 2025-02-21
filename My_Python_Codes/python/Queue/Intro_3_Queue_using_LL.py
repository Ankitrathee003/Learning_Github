# While implementing Queue


# APPROACH 1 Keeping Head to new coming element
# Enque  O(1)
    # for ex we have queue =  8,7,6,5   [None <--8 <--7 <--6 <--5 (HEAD)] with  head =5 as it came at last ( and 8 as last element  8.next is None)
    # Now we want to add a new element say 4 so we will create a newnode with 4 
    # will make newnode.next=head  and head=new node
# Deque  O(n)
    # for deque we have to remove 8 being first element to enter the Queue
    # so to remove it we have to traverse complete linked list 


# APPROACH 2
# to come out of this we will simply use two pointer approach we will keep Head to first element entering queue and tail to recently entering element

# ENQUE
    # initially for 1 element Head and tail will point out to same
    # as an when new element will come tail.next=NewNode   tail=Newnode    (so recent element will be at tail)  Head will be at starting Node which come first
    #  [(head) 8-> 7-> 6-> 5 (tail)]
#DEQUE
    # for deque we will simply take from head and will move head to head.next

# we will take care that if during Deque operation Queue become empty than head is referring to None but tail is still referring to last element present:
# so while enquing we have to check that whether Head is None or Not (if head is None means we have finished our Queue will have to add from starting and now tail and head will again refer to same upcoming Node)



# to facilitate import command
import sys
sys.path.insert(1,'C:\\Users\\ankit\\OneDrive\\Desktop\\rathee\\python\\Queue\\Intro_4_insertion_element.py')
from Intro_4_insertion_element import Node 


# QUEUE USING LL
class Queue:
    def __init__(self):  # (head,tail,count are kept private variable)
        self.__head=None
        self.__tail=None
        self.__count=0

    def enque(self,element):
        newnode=Node(element)
        if self.__head:
            self. __tail.next=newnode
        else:
            self. __head=newnode
        self. __tail=newnode
        self.__count=self.__count+1
    
    def deque(self):
        if self.__head:
           element=self.__head.data
           self.__head = self.__head.next
           self.__count=self.__count-1
           return(element)
        else:
            print("queue is Empty")
            return
    def isEmpty(self):
        return self.size()==0

    def size(self):
        return self.__count

    def front (self):
        if self.__head:
           element=self.__head.data
           return(element)
        else:
            print("queue is Empty")
            return
        

q=Queue()
q.enque(9)
q.enque(8)
q.enque(7)

print(q.front())

while q.size()!=0:
    print(q.deque())
