# Note using a list or stack at least one of the Enque or Deque will be of order n.


class QueueUsingTwoStacks:

    def __init__(self):
        self.__s1=[]
        self.__s2=[]
    def enqueue(self,data):  #O(n)

        while (len(self.__s1)!=0):
            self.__s2.append(self.__s1.pop())
        self.__s1.append(data)
        while (len(self.__s2)!=0):
            self.__s1.append(self.__s2.pop())
        return

    def dequeue(self):    #O(1)                               # we can also write such that deque become O(n) and Enque become O(1)
        if (len(self.__s1)==0):
            return -1
        return(self.__s1.pop())


    def front(self):     #O(1)  # we are keeping front pointer  to end of list since we are adding new element to start of list in Enque operation
        if (len(self.__s1)==0):
            return(-1)
        return(self.__s1[-1])
        

    def size(self):      #O(1)
        return len(self.__s1)
    
    def isEmpty(self):   #O(1)
        return (self.size()==0)
    
q=QueueUsingTwoStacks()
q.enqueue(1)      #front pointer but last element of list and last element of queue  [4,3,2,1(front pointer)]
q.enqueue(2)
q.enqueue(3)
q.enqueue(4)      # (last element for Queue as it  was added at last (using Enque operation by moving element from 1 to 3 to s2 and adding 4 to s1 and the add 3,2,1 to s1 again from s2)

while not q.isEmpty():
    print(q.dequeue())



