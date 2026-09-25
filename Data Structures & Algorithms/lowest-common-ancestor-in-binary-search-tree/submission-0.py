# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        path = [] 
        best_ind = 0
        def find(root, p):
            path.append(root)
            if root is p:
                return
            if p.val < root.val:
                find(root.left, p)
            else:
                find(root.right, p)
        def track(root, q):
            nonlocal best_ind
            if root in path:
                best_ind = max(best_ind, path.index(root))
            if root is q:
                return
            if q.val < root.val:
                track(root.left, q)
            else:
                track(root.right, q)
        find(root, p)
        print([x.val for x in path])
        track(root, q)
        return path[best_ind]


            
                