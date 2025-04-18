class Solution:
    def getIntersectionNode(self, unjup: ListNode, headB: ListNode) -> ListNode:
        while unjup is not None:
            pB = headB
            while pB is not None:
                if unjup == pB:
                    return unjup
                pB = pB.next
            unjup = unjup.next
        return None