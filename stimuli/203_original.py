class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def listtoLinked(lst):
    cur = dummy = ListNode(0)
    for e in lst:
        cur.next = ListNode(e)
        cur = cur.next
    return dummy.next

def linkedtoList(linkedLst :ListNode):
    l = []
    n = linkedLst
    while n is not None:
        l.append(n.val)
        n = n.next

    return l


def removeElements(head: ListNode, val: int) -> ListNode:
    # -- #
    sentinel.next = head
    prevNd, currNd = sentinel, head
    while currNd:
        if currNd.val == val:
            prevNd.next = currNd.next
        else:
            prevNd = currNd
        currNd = currNd.next
    return sentinel.next


def test_case():
    head = listtoLinked([1,2,6,3,4,5,6])
    assert(linkedtoList(removeElements(head,6)) == [1,2,3,4,5])

def test_case2():
    head = listtoLinked([])
    assert(linkedtoList(removeElements(head, 1)) == [])


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")