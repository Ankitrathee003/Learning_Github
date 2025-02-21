
# to facilitate import command
import sys
sys.path.insert(1,'C:\\Users\\ankit\\OneDrive\\Desktop\\rathee\\python\\Stack\\Intro_4_insertion_element.py')

from Intro_4_insertion_element import Node 

# using Linked List code  which has been imported
class stack:
    def __init__(self):
        self.__head=None   #(we can take it as whenever we want Head we will write self.__head)
        self.__count=0
        
    def isEmpty(self):
        return self.__head is None
    
    def push(self,element):
        newnode=Node(element)     # to create a new node
        newnode.next=self.__head  # connect new node to top element (whose address is in head)  (# BOTTOM ELEMENT IS TAIL OF LINKED LIST)
        self.__head=newnode       # now moving the head to new node for further usage.
        self.__count=self.__count+1

    def pop(self):
        if self.isEmpty():
            print('stack is empty')
            return
        data=self.__head.data  #(self.__head has gone to node while inserting this element so here we can use .data method of Node class)
        self.__head=self.__head.next
        self.__count=self.__count-1
        return data
