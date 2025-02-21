def interleave_queue(queue):
    n = len(queue)
    half_size = n // 2

    # Separate the queue into two halves
    first_half = queue[:half_size]
    second_half = queue[half_size:]

    # Create two stacks (lists) to store the elements of the two halves
    stack1 = first_half[::-1]
    stack2 = second_half[::-1]

    # Reconstruct the queue by interleaving elements from the two stacks
    queue.clear()
    while stack1 and stack2:
        queue.append(stack1.pop())
        queue.append(stack2.pop())

# Example usage:
Q = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
print("Original Queue:", Q)

interleave_queue(Q)
print("Interleaved Queue:", Q)
