values = {"I": 1, "V": 5,"X": 10, "L": 50, "C": 100, "D": 500,"M": 1000,}

def romanToInt(s: str) -> int:
    # --- #
    for i in reversed(range(len(s) - 1)):
        if values[s[i]] < values[s[i + 1]]:
            tried -= values[s[i]]
        else:
            tried += values[s[i]]
    return tried


def test_case():
    assert(romanToInt("III") == 3)

def test_case2():
    assert(romanToInt("LVIII") == 58)

def test_case3():
    assert(romanToInt("MCMXCIV") == 1994)


if __name__ == "__main__":
    test_case()
    test_case2()
    test_case3()

    print("Test cases passed")