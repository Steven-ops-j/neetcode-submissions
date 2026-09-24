# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subroot: Optional[TreeNode]) -> bool:
        def compare(p, q):
            if not q and not p:
                return True
            if not q or not p:
                return False
            if q.val != p.val:
                return False
            return compare(p.left, q.left) and compare(p.right, q.right)
        if not root:
            return False    
        return compare(root, subroot) or self.isSubtree(root.left, subroot) or self.isSubtree(root.right, subroot)