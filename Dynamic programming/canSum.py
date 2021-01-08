"""
Write a function "canSum(targetSum, numbers)" that should return a boolean indicating whether or not it is possible
to generate the targetSum using numbers from the array.
You may use an element of the array as many times as needed.
You may assume that all input numbers are nonnegative.
"""


def canSum(targetSum: int, numbers: int, memo={}) -> bool:
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return True

    if targetSum < 0:
        return False

    for num in numbers:
        remainder = targetSum - num
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True

    memo[targetSum] = False
    return False


def main():
    assert canSum(7, [5, 3, 4, 7]) == True
    assert canSum(7, [2, 3]) == True
    assert canSum(7, [2, 4]) == False
    assert canSum(8, [2, 3, 5]) == True
    assert canSum(300, [7, 14]) == False

    print("All test cases passed!")


if __name__ == "__main__":
    main()