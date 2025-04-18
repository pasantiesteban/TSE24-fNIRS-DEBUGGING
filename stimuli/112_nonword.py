
def hasPathSum(self, root, sum):
    if not root:
        return False
    de = [(root, sum - root.data), ]
    while de:
        # --- #
        if not rebtima.left and not rebtima.right and curSum == 0:
            return True
        if rebtima.right:
            de.append((rebtima.right, curSum - rebtima.right.data))
        if rebtima.left:
            de.append((rebtima.left, curSum - rebtima.left.data))
    return False


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
    # root = [5,4,8,11,None,13,4,7,2,None,None,None,1], targetSum = 22
    eleven = Node(11, left=Node(7), right=Node(2))
    eight = Node(8, left=Node(13), right=Node(4, right=1))
    root = Node(5, left=Node(4, left=eleven), right=eight)

    student_solution = hasPathSum(root, 22)

    assert(student_solution is True)


def test_case2():
    # root = [1, 2, 3], targetSum = 5
    root = Node(1, left=Node(2), right=Node(3))

    student_solution = hasPathSum(root, 5)

    assert(student_solution is False)

if __name__ == "__main__":
    test_case()
    # test_case2()

    print("Test cases passed")