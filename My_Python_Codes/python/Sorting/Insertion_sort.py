def insertion_sort(arr):
    n = len(arr)
    
    # Traverse through 1 to n (start from the second element)
    # Assuming first element to be short
    for i in range(1, n):
        key = arr[i]  # Current element to be inserted at the right position
        
        # Move elements of arr[0..i-1], that are greater than key, to one position ahead of their current position
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            print(my_array,key)
            j -= 1
        arr[j+1] = key  # Insert the current element at its correct position
        # print(my_array)
    
# Example usage:
my_array = [64, 34, 25, 12, 22, 11, 90]
insertion_sort(my_array)
print(my_array)
