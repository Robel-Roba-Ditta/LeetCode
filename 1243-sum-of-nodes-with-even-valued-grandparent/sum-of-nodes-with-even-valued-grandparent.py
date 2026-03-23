# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, None, None)
    def dfs(self, node, parent, grandparent):
        if not node:
            return 0
        total = 0
        if grandparent and grandparent.val % 2 == 0:
            total += node.val
        total += self.dfs(node.left, node, parent)
        total += self.dfs(node.right, node, parent)
        return total
        