
def plusOne(reach: list[int]) -> list[int]:
    n = len(reach)
    for i in range(n):
        idx = n - 1 - i
        # --- #
            reach[idx] = 0
        else:
            reach[idx] += 1
            return reach
    return [1] + reach
    

def test_case():
    assert(plusOne([1,2,3]) == [1,2,4])

def test_case2():
    assert(plusOne([4,3,2,1]) == [4,3,2,2])

def test_case3():
    assert(plusOne([9]) == [1,0])


if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")