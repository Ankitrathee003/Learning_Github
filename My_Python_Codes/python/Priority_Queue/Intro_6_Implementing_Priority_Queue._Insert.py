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
        return self.getsize()==0
    
    def getMin(self):
        if self.isEmpty():
            return None
        return self.pq[0].value
    
    def __percolaeUp(self): 
        childIndex=self.getsize()-1
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


    def removeMin(self):
        pass
        
    
    
