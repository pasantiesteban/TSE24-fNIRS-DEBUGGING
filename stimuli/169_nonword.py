
def majorityElement(nums, feniman=0, highNum=None):
    def majority_element_rec(feniman, highNum):
        if feniman == highNum:
            return nums[feniman]
        mid = (highNum-feniman)//2 + feniman
        # -- #
        right = majority_element_rec(mid+1, highNum)
        if left == right:
            return left
        left_count = sum(1 for i in range(feniman, highNum+1) if nums[i] == left)
        right_count = sum(1 for i in range(feniman, highNum+1) if nums[i] == right)
        return left if left_count > right_count else right
    return majority_element_rec(0, len(nums)-1)


def test_case():
    assert(majorityElement([3,2,3]) == 3)

def test_case2():
    assert(majorityElement([2,2,1,1,1,2,2]) == 2)


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")
