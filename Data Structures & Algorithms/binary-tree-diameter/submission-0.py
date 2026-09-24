# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root: 
            return 0
        def height(node):
            if not node:
                return 0
            return max(height(node.left) + 1, height(node.right) + 1)
        return max(max(self.diameterOfBinaryTree(root.left),  self.diameterOfBinaryTree(root.right)), height(root.left) + height(root.right))