def canSum(targetSum, numbers):
    table = [False] * (targetSum + 1)
    table[0] = True

    for i in range(targetSum + 1):
        if table[i] == True:
            for num in numbers:
                if i + num <= targetSum:
                    table[i + num] = True

    return table[targetSum]


def main():
    assert canSum(7, [5, 3, 4, 7]) == True
    assert canSum(7, [2, 3]) == True
    assert canSum(7, [2, 4]) == False
    assert canSum(8, [2, 3, 5]) == True
    assert canSum(300, [7, 14]) == False

    print("All test cases passed!")


if __name__ == "__main__":
    main()