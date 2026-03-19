# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        if not root:
            return TreeNode(val)

        def insert(node, key):
            if key > node.val:
                if node.right is None:
                    node.right = TreeNode(key)
                else:
                    insert(node.right, key)
            else:
                if node.left is None:
                    node.left = TreeNode(key)
                else:
                    insert(node.left, key)

        insert(root, val)
        return root
        