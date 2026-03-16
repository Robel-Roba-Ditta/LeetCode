class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        cur = head
        stack = []
        while cur:
            while stack and stack[-1].val < cur.val:
                stack.pop()
            stack.append(cur)
            cur = cur.next
        for i in range(len(stack) - 1):
            stack[i].next = stack[i+1]
        stack[-1].next = None
        return stack[0]

        