def howSum(targetSum, numbers):
    table = [None] * (targetSum + 1)
    table[0] = []

    for i in range(targetSum + 1):
        if table[i] is not None:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = table[i] + [num]

    return table[targetSum]


def main():
    assert howSum(7, [5, 3, 4, 7]) == [4, 3]
    assert howSum(7, [2, 3]) == [3, 2, 2]
    assert howSum(7, [2, 4]) == None
    assert howSum(8, [2, 3, 5]) == [2, 2, 2, 2]
    assert howSum(300, [7, 14]) == None

    print("All test cases passed!")


if __name__ == "__main__":
    main()