class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p==None and q==None:
            return True
        elif p==None or q==None:
            return False
        l=self.isSameTree(p.left,q.left)
        r=self.isSameTree(p.right,q.right)
        if p.val!=q.val:   ## while going upward if the nodes values are unequal return False if equal than return  Leftsubtree and Rightsubtree result
            return False
        return l and r
    




# better we check the unequal value condition before reaching the leaf nodes we move down untill the nodes are same instead of completely going at bottom than come back:
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        elif p.val != q.val:
            return False
        
        l = self.isSameTree(p.left, q.left)
        r = self.isSameTree(p.right, q.right)

        return l and r
