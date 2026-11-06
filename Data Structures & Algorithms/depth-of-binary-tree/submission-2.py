# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, node: Optional[TreeNode]) -> int:
        if node is None:
            return 0
        left = self.maxDepth(node.left) 
        right = self.maxDepth(node.right)

        if left > right:
            return 1+left
        else:
            return 1+right
        