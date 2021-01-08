"""
Write a function "bestSum(targetSum, numbers)" that should return an array containing the shortest combination
of elements that add up to exactly the targetSum. If there is no combination that adds up to the 
targetSum, then return null.
If there are multiple combinations possible, you may return one of the shortest.
"""
from typing import List


def bestSum(targetSum: int, numbers: int, memo: dict = {}) -> List[int]:
    if targetSum in memo:
        return memo[targetSum]

    if targetSum == 0:
        return []

    if targetSum < 0:
        return None

    shortestCombination = None

    for num in numbers:
        remainder = targetSum - num
        result = bestSum(remainder, numbers, memo)
        if result is not None:
            combination = result + [num]
            if shortestCombination is None or len(combination) < len(
                shortestCombination
            ):
                shortestCombination = combination

    memo[targetSum] = shortestCombination
    return shortestCombination


def main():
    assert bestSum(7, [5, 3, 4, 7]) == [7]
    assert bestSum(8, [2, 3, 5]) == [5, 3]
    assert bestSum(8, [1, 4, 5]) == [4, 4]
    assert bestSum(100, [1, 2, 5, 25]) == [25, 25, 25, 25]

    print("All test cases passed!")


if __name__ == "__main__":
    main()