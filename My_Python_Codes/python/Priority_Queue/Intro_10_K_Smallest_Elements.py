# Bottom-up heapify starts at the lowest level of the heap and works its way up to the root, 
# while top-down heapify starts at the root and works its way down to the lowest level of the heap. 
# Bottom-up heapify has a time complexity of O(n), while top-down heapify has a time complexity of O(log n). 
# Bottom-up heapify is typically faster for large heaps, 
# while top-down heapify is faster for small heaps.



l=[10,8,7,2,6,5,3,1,11]  # We are creating bottom up heapify so it take O(n) time to make MIN HEAP elements are inserted at bottom than travel above

k=4

import heapq

heapq.heapify(l)
# for i in range(k):
#     print(heapq.heappop(l))

# k_smallest = heapq.nsmallest(k, l)    #O(k(log(n)))
# print(k_smallest)


# So overall Complexity is O(n+klog(n))    means O(n)



# Here is code with time Complexity O(klog(n))

def k_smallest_elements(l, k):
    max_heap = [-num for num in l[:k]]  # Create a max heap with the first k elements (negate the numbers)
    heapq.heapify(max_heap)  # Convert the list into a max heap

    # For the rest of the elements, maintain a max heap of size k
    for num in l[k:]:
        if num < -max_heap[0]:  # If the current number is smaller than the largest element in the max heap
            heapq.heappop(max_heap)  # Remove the largest element from the max heap (negate of kth smallest)
            heapq.heappush(max_heap, -num)  # Push the new number into the max heap (negate it)

    return [-num for num in max_heap]  # Convert the negative numbers back to positive to get the k smallest elements


k_smallest = k_smallest_elements(l, k)
print(k_smallest)










# k_smallest = k_smallest_elements(l, k)
# print(k_smallest)




