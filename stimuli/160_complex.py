class Solution:
    def getIntersectionNode(self, unfair: ListNode, headB: ListNode) -> ListNode:
        while unfair is not None:
            pB = headB
            while pB is not None:
                if unfair == pB:
                    return unfair
                pB = pB.next
            unfair = unfair.next
        return None