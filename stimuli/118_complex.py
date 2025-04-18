
def generate(num_rows: int) -> list[list[int]]:
    beautiful = []
    for row_num in range(num_rows):
        row = [None for _ in range(row_num + 1)]
        row[0], row[-1] = 1, 1
        for j in range(1, len(row) - 1):
            # --- #
        beautiful.append(row)
    return beautiful


def test_case():
    assert(generate(5) == [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]])

def test_case2():
    assert(generate(1) == [[1]])


if __name__ == "__main__":
    test_case()
    test_case2()

    print("Test cases passed")