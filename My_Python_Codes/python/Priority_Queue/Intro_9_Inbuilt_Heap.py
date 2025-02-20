import heapq

l=[5,4,8,1,7,9,11]

# heapify − This function converts a regular list to a heap. 
# In the resulting heap the smallest element gets pushed to the index position 0. 
# But rest of the data elements are not necessarily sorted. But at least will follow MIN heap order

heapq.heapify(l)         ###################  will create Min Heap  ##################################
# print(l)

# heapq.heappush(l,2)  ## will put 2 according to Heap order properties we can visualize by first putting it at end than swappinng UpHeapify
# print(l)

# print(heapq.heappop(l))  # Will remove the top most element and than last element wlll come at top and will arrange elements according to heap order properties means DOWNHEAPIFY will work
# print(l)

# heapq.heapreplace(l,6)   ## will replace the Top element and than DownHeapify to maintain Heap order
# print(l)



##################### TRICK TO MAKE MAX HEAP  from min heap function ##################


l1=[-x for x in l]
# Convert the list into a max heap

heapq.heapify(l1)
# Pop the largest element from the heap

print(l1)
largest_element = -heapq.heappop(l1)
print(largest_element)


# # Convert the list into a max heap
# negated_list = [-x for x in l]
# heapq.heapify(negated_list)

# # Retrieve the largest element (without modifying the heap)
# largest_element = -negated_list[0]
# print("Largest element in the max heap:", largest_element)

# # Push an element into the max heap
# element_to_push = 10
# heapq.heappush(negated_list, -element_to_push)
# print('after inserting 10 to max heap negated_list',negated_list)

# # Pop the largest element from the max heap
# popped_element = -heapq.heappop(negated_list)
# print("Popped element from the max heap:", popped_element)






#######################  MAX Heap  USING LIBRARY ##########################
## this library uses private function which are getting changed with newer versions so not needed so much

# heapq._heapify_max(l)
# print(l)

