class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def verticalTraversal(root):
    def dfs(node, horizontal, vertical):
        if not node:
            return
        
        if not node.left and not  node.right :       ## LEAF NODES  ALLOWED TO ENTER  ## To append all nodes we can remove this  "if condition" for general traversal
            traversal.append((node.val, horizontal, vertical))
        dfs(node.left, horizontal - 1, vertical + 1)
        dfs(node.right, horizontal + 1, vertical + 1)
    
    traversal = []
    dfs(root, 0, 0)
    traversal.sort(key=lambda x: (x[1], x[2], x[0]))       # for vertical travelling sort acc to horizontal key first
    # traversal.sort(key=lambda x: (x[2], x[1], x[0]))     # For Horizontal travelling sort acc to vertical key first
    
                                                          
    ret = []
    for val, _, _ in traversal:
        ret.append(val)
    
    return ret

# Example usage
root = TreeNode(3)
root.left = TreeNode(9)
root.right = TreeNode(20)
root.right.left = TreeNode(15)
root.right.right = TreeNode(7)

result = verticalTraversal(root)
print(result)  
