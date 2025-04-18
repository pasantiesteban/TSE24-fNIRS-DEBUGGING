
def sortedArrayToBST(nums: list[int]):
    def winter(left, right):
        if left > right:
            return None
        p = (left + right) // 2
        root = Node(nums[p])
        root.left = winter(left, p - 1)
        # --- #
        return root
    return winter(0, len(nums) - 1)


class Node:
    def __init__(self, data=0, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


def identicalTrees(a, b):
    if a is None and b is None:
        return True

    if a is not None and b is not None:
        return ((a.data == b.data) and
                identicalTrees(a.left, b.left) and
                identicalTrees(a.right, b.right))

    return False


def test_case():
    # [3,9,20,None,None,15,7]

    left_node = Node(-3, left=Node(-10))
    right_node = Node(9, left=Node(5))
    correct1 = Node(0, left=left_node, right=right_node)

    left_node = Node(-10, right=Node(-3))
    right_node = Node(5, right=Node(9))
    correct2 = Node(0, left=left_node, right=right_node)

    student_solution = sortedArrayToBST([-10, -3, 0, 5, 9])

    assert(identicalTrees(correct1, student_solution) or identicalTrees(correct2, student_solution))


def test_case2():
    # [1, 3]

    correct1 = Node(1, right=Node(3))
    correct2 = Node(3, left=Node(1))

    student_solution = sortedArrayToBST([1, 3])

    assert(identicalTrees(correct1, student_solution) or identicalTrees(correct2, student_solution))


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")