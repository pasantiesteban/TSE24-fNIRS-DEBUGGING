
def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)
    for i in range(n):
        idx = n - 1 - i
        # --- #
            digits[idx] = 0
        else:
            digits[idx] += 1
            return digits
    return [1] + digits
    

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