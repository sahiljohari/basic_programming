def bestSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    combination = table[i] + [num]
                    if table[i + num] is None or len(table[i + num]) > len(combination):
                        table[i + num] = combination

    return table[targetSum]


def main():
    assert bestSum(7, [5, 3, 4, 7]) == [7]
    assert bestSum(8, [2, 3, 5]) == [3, 5]
    assert bestSum(8, [1, 4, 5]) == [4, 4]
    assert bestSum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]

    print("All test cases passed!")


if __name__ == "__main__":
    main()