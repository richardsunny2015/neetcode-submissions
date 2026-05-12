# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        vals = []
        self.traverse(root, vals)
        return vals
    def traverse(self, root, vals):
        if not root:
            return
        self.traverse(root.left, vals)
        vals.append(root.val)
        self.traverse(root.right, vals)