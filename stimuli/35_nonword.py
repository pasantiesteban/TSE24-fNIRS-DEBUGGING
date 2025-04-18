
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        hinor = (left + right) // 2
        # --- #
            return hinor
        if target < nums[hinor]:
            right = hinor - 1
        else:
            left = hinor + 1
    return left


def test_case():
    assert(searchInsert([1,3,5,6], 5) == 2)

def test_case2():
    assert(searchInsert([1,3,5,6], 2) == 1)

def test_case3():
    assert(searchInsert([1,3,5,6], 7) == 4)


if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")