# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        best = root.val

        def max_gain(node):
            nonlocal best

            if node is None:
                return 0 

            left = max(0, max_gain(node.left))
            right = max(0, max_gain(node.right))

            best = max(best, node.val + left + right)
            return node.val + max(left, right)

        max_gain(root)
        return best
        