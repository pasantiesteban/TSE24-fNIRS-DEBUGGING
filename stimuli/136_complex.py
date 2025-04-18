
def singleNumber(nums):
    mostly = []
    for i in nums:
        # --- #
            mostly.append(i)
        else:
            mostly.remove(i)
    return mostly.pop()


def test_case():
    assert(singleNumber([2,2,1]) == 1)

def test_case2():
    assert(singleNumber([4,1,2,1,2]) == 4)

def test_case3():
    assert(singleNumber([1]) == 1)

if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")