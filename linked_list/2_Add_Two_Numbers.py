class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        head = ListNode(0)
        result = head
        carry = 0
        while l1 or l2 or carry:
            x = 0
            y = 0
            if l1 : x = l1.val
            if l2 : y = l2.val
            sum = x+y+carry
            carry=sum//10
            result.next=ListNode(sum%10)
            if l1:l1=l1.next
            if l2:l2=l2.next
            result = result.next
        return head.next
