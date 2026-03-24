# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        if not root:
            return 0
        return self.dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum)
    def dfs(self, node, target):
        if not node:
            return 0
        count = 1 if node.val == target else 0
        count += self.dfs(node.left, target - node.val)
        count += self.dfs(node.right, target - node.val)
        return count