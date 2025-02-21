def selectionSort(nums):
    # Iterate from the last index to the second index (0-based indexing)
    # Each iteration places the largest element at its correct position
    for i in range(len(nums)-1, 0, -1):
        positionOfLargest = 0  # Assume the first element is the largest
        
        # Iterate over the unsorted portion of the array
        # Find the index of the largest element
        for j in range(1, i+1):
            if nums[j] > nums[positionOfLargest]:
                positionOfLargest = j  # Update the index of the largest element
        
        # Swap the largest element with the last element in the unsorted portion
        nums[i], nums[positionOfLargest] = nums[positionOfLargest], nums[i]
        
        print(nums)  # Print the current state of the array after each pass


nums = [1, 2, 3, 11, 9, 8, 28, 6, 3, 111]
selectionSort(nums)
# print(nums)
