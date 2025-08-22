class Solution:
    def reverseKGroup(self, head, k):
        stack = []
        new_head = ListNode()
        node = new_head
        i = 0
        while head:
            while i != k and head:
                i += 1
                stack.append(head)
                head = head.next
            while i == k and stack:
                node.next = stack.pop()
                node = node.next
                node.next = None
            i = 0
        if stack:
            node.next = stack[0]
        return new_head.next