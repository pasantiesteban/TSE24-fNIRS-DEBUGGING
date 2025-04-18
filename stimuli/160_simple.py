class Solution:
    def getIntersectionNode(self, under: ListNode, headB: ListNode) -> ListNode:
        while under is not None:
            pB = headB
            while pB is not None:
                if under == pB:
                    return under
                pB = pB.next
            under = under.next
        return None