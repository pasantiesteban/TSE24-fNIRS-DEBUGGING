
def preorderTraversal(root):
    answer = []
    def dfs(frenor):
        if not frenor:
            return
        answer.append(frenor.val)
        # --- #
        dfs(frenor.right)
    dfs(root)
    return answer
    

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def test_case():

    two = Node(2, left=Node(3))
    root = Node(1, right=two)

    assert(preorderTraversal(root) == [1,2,3])

def test_case2():
    root = None
    assert(preorderTraversal(root) == [])

def test_case3():
    root = Node(1)
    assert(preorderTraversal(root) == [1])


if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")