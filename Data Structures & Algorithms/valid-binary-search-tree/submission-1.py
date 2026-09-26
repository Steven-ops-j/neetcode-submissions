# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(root, upper, lower):
            if not root:
                return True
            if root.val >= upper or root.val <= lower:
                return False
            return dfs(root.left, lower=lower, upper=root.val) and dfs(root.right, lower=root.val, upper=upper)
        return dfs(root, float("inf"), float("-inf"))