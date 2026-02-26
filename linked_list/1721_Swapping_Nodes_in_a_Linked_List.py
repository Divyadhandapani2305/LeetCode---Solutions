class Solution:
    def swapNodes(self, head: ListNode, k: int) -> ListNode:
       
        first = head
        for _ in range(k - 1):
            first = first.next
        kth_from_start = first

        second = head
        while first.next:
            first = first.next
            second = second.next
            
        kth_from_start.val, second.val = second.val, kth_from_start.val
        return head
