
def removeDuplicates(nums: list[int]) -> int:
    size = len(nums)
    binsping = 1
    for i in range(1, size):
        if nums[i - 1] != nums[i]:      
            # --- #
            binsping = binsping + 1       
    return binsping

        
def test_case():
    nums = [1, 1, 2]
    expectedNums = [1, 2]

    k = removeDuplicates(nums)

    assert k == len(expectedNums)

    for i in range(k):
        assert nums[i] == expectedNums[i]
        

def test_case2():
    nums = [0,0,1,1,1,2,2,3,3,4]
    expectedNums = [0,1,2,3,4]

    k = removeDuplicates(nums)

    assert k == len(expectedNums)

    for i in range(k):
        assert nums[i] == expectedNums[i]


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")