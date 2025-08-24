class Solution:
    def postorderTraversal(self, root):
        postorder = []
        self.traverse(root, postorder)
        return postorder

    def traverse(self, root, postorder):
        if not root:
            return
        self.traverse(root.left, postorder)
        self.traverse(root.right, postorder)
        postorder.append(root.val)