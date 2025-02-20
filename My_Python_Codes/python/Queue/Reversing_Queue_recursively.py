import queue
q=queue.Queue()

for i in range (22,32):  ## create a queue from 22 to 31
    q.put(i)

def reverse_queue_recursion(q):
    if q.empty():
        return
    temp=q.get()
    reverse_queue_recursion(q)
    # print(q.qsize())
    q.put(temp)
    return q  #Ye hum jo q return kar rahe h it does not mean that agar nahi karenge to q update nhi hoga
              # wo tab bhi update ho raha h aap print(q.qsize()) chla ke dekh skte h 
              # #size continuously badh raha h par is return ka in between koi role nhi h

    

ans=reverse_queue_recursion(q)  #Queue is reversed now
while not ans.empty():
    print(ans.get()) 


    


