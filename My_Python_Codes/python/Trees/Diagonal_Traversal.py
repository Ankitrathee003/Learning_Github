class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def diagonalTraversal(root):
    def dfs(node, diagonal):
        if not node:
            return
        
        # Add the current node's value to the appropriate diagonal list
        if len(diagonals) <= diagonal:        # Jab tak ssaare leftest nodes khtam nhi ho jaati nai node add hoti rahegi because left me add 1 ho raha h # if len(diagonals) <= diagonal: 
            diagonals.append([node.val])
        else:
            diagonals[diagonal].append(node.val)
        
        dfs(node.left, diagonal+1)      # Traverse the left child with the next diagonal  pehle saare diagonals ka pehla element add hoga
        dfs(node.right, diagonal) # Traverse the right child with the same diagonal
    
    diagonals = []  # List of lists to store values for each diagonal
    dfs(root, 0)    # Start diagonal traversal from the root
    
    # ret = []                                           # List to store the final result with all diagonal values
    # for diagonal_values in diagonals:                   
    #     ret=ret+diagonal_values   ##adding two lists
    
    return diagonals       ## or return ret by implementing above 3 lines

# Example usage
root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.right.right = TreeNode(14)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right.left = TreeNode(13)

result = diagonalTraversal(root)
print(result)                                                     #   [[8, 10, 14], [3, 6, 7, 13], [1, 4]] for diagonals 
                                                                 #  for diagonal traversal if we return     ret    Output: [8, 10, 14, 3, 6, 13, 1, 4, 7]
