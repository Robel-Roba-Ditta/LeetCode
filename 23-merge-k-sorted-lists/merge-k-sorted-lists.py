class Solution:
    def mergeKLists(self, lists):
        if not lists:
            return None
        
        head = ListNode()
        node = head
        nodes = []
        
        for l_list in lists:
            while l_list:
                nodes.append(l_list.val)
                l_list = l_list.next
        
        if not nodes:
            return None
        
        for val in sorted(nodes):
            node.next = ListNode(val)
            node = node.next
        
        return head.next