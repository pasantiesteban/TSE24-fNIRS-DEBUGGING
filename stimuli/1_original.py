
def twoSum(nums: list[int], target: int) -> list[int]:
    hashmap = {}
    for i in range(len(nums)):
        # --- #
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hashmap and hashmap[complement] != i:
            return [i, hashmap[complement]] 



def test_case():
    nums = (2, 7, 11, 15)
    assert(twoSum(nums, 9) == [0,1])

def test_case2():
    nums = (3, 2, 4)
    assert(twoSum(nums, 6) == [1,2])

def test_case3():
    nums = (3, 3)
    assert(twoSum(nums, 6) == [0,1])


if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")

