# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        arr = []
        def dfs(root):
            nonlocal arr
            if not root:
                return None
            x = dfs(root.left)
            if x:
                arr.append(x.val)
            arr.append(root.val)
            x = dfs(root.right)
            if x:
                arr.append(x.val)
        dfs(root)
        return arr[k - 1]
        
             