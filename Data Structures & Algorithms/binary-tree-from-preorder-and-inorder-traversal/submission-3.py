# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        pos_in_inorder = {val: ind for (ind, val) in enumerate(inorder)}
        def build(low, upper, p):
            if low > upper or p >= len(preorder):
                return None
            while pos_in_inorder[preorder[p]] > upper or pos_in_inorder[preorder[p]] < low:
                p += 1
            root = TreeNode(preorder[p])
            root.left = build(low, pos_in_inorder[preorder[p]] - 1, p + 1)
            root.right = build(pos_in_inorder[preorder[p]] + 1, upper, p + 1)
            return root
        return build(0, len(preorder) - 1, 0)