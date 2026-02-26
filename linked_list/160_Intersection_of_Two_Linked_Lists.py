class Solution:
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        
        pA = headA
        pB = headB
        
        while pA != pB:
            
            if pA:
                pA = pA.next
            else:
                pA = headB
            
           
            if pB:
                pB = pB.next
            else:
                pB = headA
        
        return pA 
