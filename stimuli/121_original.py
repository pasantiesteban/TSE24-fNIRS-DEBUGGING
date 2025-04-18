
def maxProfit(prices: list[int]) -> int:
    minPrice = float('inf')
    maxProfit = 0
    for i in range(len(prices)):
        if prices[i] < minPrice:
            minPrice = prices[i]
        # --- #
            maxProfit = prices[i] - minPrice
    return maxProfit


def test_case():
    assert(maxProfit([7,1,5,3,6,4]) == 5)

def test_case2():
    assert(maxProfit([7,6,4,3,1]) == 0)


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")