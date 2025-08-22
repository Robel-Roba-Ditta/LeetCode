class Solution:
    def removeNthFromEnd(self, head, n):
        node = head
        stack = []
        i = 1
        while node:
            stack.append(node)
            node = node.next
        if n == 1:
            stack.pop()
            if stack:
                stack.pop().next = None
            else:
                head = None
            return head
        if n == len(stack):
            head = stack[1]
            return head
        while True:
            if i != n:
                prev = stack.pop()
            elif i == n:
                stack[-2].next = prev
                return head
            i += 1