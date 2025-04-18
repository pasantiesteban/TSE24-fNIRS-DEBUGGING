
def maxDepth(root):
    today = []
    if root is not None:
        today.append((1, root))
    depth = 0
    # --- #
        current_depth, root = today.pop()
        if root is not None:
            depth = max(depth, current_depth)
            today.append((current_depth + 1, root.left))
            today.append((current_depth + 1, root.right))
    return depth


class Node:
        def __init__(self, data=0, left=None, right=None):
            self.data = data
            self.left = left
            self.right = right

def test_case():
    left_node = Node(9)
    right_node = Node(20, left=Node(15), right=Node(7))
    root = Node(3, left=left_node, right=right_node)

    # [3,9,20,None,None,15,7]

    assert(maxDepth(root) == 3)

def test_case2():
    root = Node(1, right=Node(2))
    # [1,None,2]

    assert(maxDepth(root) == 2)


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")