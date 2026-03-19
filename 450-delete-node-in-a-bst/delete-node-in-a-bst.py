# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return None
        
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        
        else:
            # ✅ Node found
            
            # Case 1: no left child
            if not root.left:
                return root.right
            
            # Case 2: no right child
            if not root.right:
                return root.left
            
            # Case 3: two children
            # find smallest in right subtree
            min_node = self.findMin(root.right)
            
            # replace value
            root.val = min_node.val
            
            # delete that node
            root.right = self.deleteNode(root.right, min_node.val)
        
        return root
    
    def findMin(self, node):
        while node.left:
            node = node.left
        return node