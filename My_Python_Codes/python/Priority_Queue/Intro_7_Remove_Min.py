### IMPLEMENTATION OF MIN HEAP ###
#### VERY VERY IMPORTANT  ###

class PriorityQueueNode:
    def __init__(self,value,priority):
        self.value=value
        self.priority=priority

class PriorityQueue:
    def __init__(self):
        self.pq=[]

    def getSize(self):
        return len(self.pq)
    
    def isEmpty(self):
        return self.getSize()==0
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolaeUp(self): 
        childIndex=self.getSize()-1
        while childIndex>0:   ## we will keep moving the element in Min heap up side untill either we reach top node or condition where parent is smaller than its child
            parentIndex=(childIndex-1)//2
            if self.pq[childIndex].priority<self.pq[parentIndex].priority:
                self.pq[childIndex],self.pq[parentIndex]=self.pq[parentIndex],self.pq[childIndex]
                childIndex=parentIndex
            else:
                break
    
    def insert(self,value,priority):
        pqNode=PriorityQueueNode(value,priority)
        self.pq.append(pqNode)
        self.__percolaeUp()


    def percolateDown(self):
        parentIndex = 0
        leftChildIndex = 2 * parentIndex + 1  # Calculate the index of the left child
        rightChildIndex = 2 * parentIndex + 2  # Calculate the index of the right child

        while leftChildIndex < self.getSize():  # Loop while the left child exists
            minIndex = parentIndex  # Assume the parent has the minimum value

            # Compare the parent with the left child
            if self.pq[minIndex].priority > self.pq[leftChildIndex].priority:
                minIndex = leftChildIndex  # Update the minimum index if left child is smaller

            # Check if the right child exists and compare with the current minimum
            if rightChildIndex < self.getSize() and self.pq[minIndex].priority > self.pq[rightChildIndex].priority:
                minIndex = rightChildIndex  # Update the minimum index if right child is smaller

            # If the minimum is still the parent, the heap property is satisfied, exit loop
            if minIndex == parentIndex:
                break

            # Swap the parent and the minimum element, then update indices
            self.pq[parentIndex], self.pq[minIndex] = self.pq[minIndex], self.pq[parentIndex]
            parentIndex = minIndex  # Move down the tree
            leftChildIndex = 2 * parentIndex + 1
            rightChildIndex = 2 * parentIndex + 2

            
    def removeMin(self):
        if self.isEmpty():
            return None
        ele=self.pq[0].value
        self.pq[0] = self.pq[-1]
        self.pq.pop()
        self.percolateDown()
        return ele
        
pq=PriorityQueue()
pq.insert('A',10)
pq.insert('C',5)
pq.insert('B',19)
pq.insert('D',4)
for i in range (4):
    print(pq.removeMin())  ## Elements will be removed according to their Priority

    

