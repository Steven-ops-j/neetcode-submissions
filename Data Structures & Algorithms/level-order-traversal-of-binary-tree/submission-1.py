# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        o = [[]]
        if not root:
            return []
        s = [deque([root]), deque()]
        while s:
            if not s[0]:
                if not s[1]:
                    s = []
                    break
                o.append([])
                s = [s[1]]
                s.append(deque())
                continue
            parent = s[0].popleft() 
            o[-1].append(parent.val)
            if parent.left:
                s[-1].append(parent.left)
            if parent.right:
                s[-1].append(parent.right)
        return o 
