# for stack in built we will use List
# Queue follow FIFO first in first out
# for queue we can use list but that will not be efficient in case of deleting as we have to shift each element one step ahead ie of order N
# but in Queue in case of append order will be still O(1).
# python 3 has inbuilt library queue
import queue


# INBUILT QUEUE

# put(item): Inserts an element to the queue.
# get(): Gets an element from the queue.
# empty(): Checks and returns true if the queue is empty.
# qsize: Returns queue's length.
# full(): Checks and returns true if the queue is full.
# maxsize(): Maximum elements allowed in a queue.

q=queue.Queue()  # importing Queue class from queue Library and making q object
q.put(1) #to insert
q.put(2)
q.put(3)


while not q.empty():
    print(q.get())    # Deque the element # FIFO



# WE CAN CHANGE THE FUNCTIONALITY OF QUEUE FROM FIFO TO LIFO
    # USING LifoQUEUE() method from queue class
q=queue.LifoQueue()   # Now it is a stack 
q.put(1)
q.put(2)
q.put(3)
q.put(4)

while q:  #  or  we can write    while not q.empty():
    print(q.get())  
print(not q.maxsize())




