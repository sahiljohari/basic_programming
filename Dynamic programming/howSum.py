"""
Write a function "howSum(targetSum, numbers)" that should return an array containing any combination
of elements that add up to exactly the targetSum. If there is no combination that adds up to the 
targetSum, then return null.
If there are multiple combinations possible, you may return any single one.
"""
from typing import List


def howSum(targetSum: int, numbers: int, memo={}) -> List[int]:
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    for num in numbers:
        remainder = targetSum - num
        result = howSum(remainder, numbers, memo)
        if result is not None:
            memo[targetSum] = result + [num]
            return memo[targetSum]

    memo[targetSum] = None
    return memo[targetSum]


def main():
    assert howSum(7, [5, 3, 4, 7]) == [4, 3]
    assert howSum(7, [2, 3]) == [3, 2, 2]
    assert howSum(7, [2, 4]) == None
    assert howSum(8, [2, 3, 5]) == [2, 2, 2, 2]
    assert howSum(300, [7, 14]) == None

    print("All test cases passed!")


if __name__ == "__main__":
    main()