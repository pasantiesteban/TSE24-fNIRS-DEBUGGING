
def searchInsert(nums: list[int], target: int) -> int:
    left, right = 0, len(nums) - 1
    while left <= right:
        pivot = (left + right) // 2
        # --- #
            return pivot
        if target < nums[pivot]:
            right = pivot - 1
        else:
            left = pivot + 1
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