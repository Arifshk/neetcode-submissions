# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        cur = root 

        while cur:
            if p.val > cur.val and q.val > cur.val:
                cur = cur.right
            elif p.val < cur.val and q.val < cur.val:
                cur = cur.left
            else: 
                return cur
 
 ## lca, lowest node in the tree such that p and q are descendant or = to this node
 ## root is always LCA, if p or q is < root its in left subtree vv right
 ## if p and q are in diff subtrees, the split is the LCA/root
 ## if p and q are in the same subtree, split of those, is the LCA
 ## if either p and q is = root, then it is the LCA
 ## (o (logn)) cause not visiting every node only checking split
 
