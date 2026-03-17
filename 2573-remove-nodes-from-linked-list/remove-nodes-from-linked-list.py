class Solution:
    def removeNodes(self, head: ListNode) -> ListNode:
        def helper(node: ListNode) -> ListNode:
            if not node:
                return None
            node.next = helper(node.next)
            if node.next and node.val < node.next.val:
                return node.next
            else:
                return node
        return helper(head)