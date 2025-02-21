# ## LINKED LIST ##

# # Every node will store two things one is data another is reference to next node.

# # reference to first Node is called Head
# # last node has reference to null
# # If we have the head of linked list it means we have the complete linked list as we can traverse the complete linked list

class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
a=Node(13)
b=Node(15)

# print(a.data)
# print(b.data)

# print(f'address of b is {b}')     # adress of b
# a.next=b                        # we are assigning Address of b to a.next

# print(a.next.data)              # a.next is address of b so here we are calling data of b 
# print(b.next.data)              # AttributeError: 'NoneType' object has no attribute 'data'
