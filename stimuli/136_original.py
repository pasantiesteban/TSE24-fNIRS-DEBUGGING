
def singleNumber(nums):
    lstDup = []
    for i in nums:
        # --- #
            lstDup.append(i)
        else:
            lstDup.remove(i)
    return lstDup.pop()


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