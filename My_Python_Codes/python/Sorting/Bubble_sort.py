def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False  # Initialize the swapped flag to False
        for j in range(0, n-i-1):  
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True  # Set the swapped flag to True if a swap occurs   
        if not swapped:
            break  # If no swaps occur in a pass, the array is already sorted  ## This improves the Best case compllexity to O(n)
# Example usage:
my_array = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(my_array)

print( my_array)

