# Leetcode: Unique Paths
# A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).
# The robot can only move either down or right at any point in time.
# The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).
# How many possible unique paths are there?


def uniquePaths(m: int, n: int) -> int:
    def isValid(x, y):
        return 0 <= x < m and 0 <= y < n

    memo = {}

    def findPath(x, y):
        if isValid(x, y) == False:
            return 0
        if x == m - 1 and y == n - 1:
            return 1
        if (x, y) in memo:
            return memo[(x, y)]

        memo[(x, y)] = findPath(x + 1, y) + findPath(x, y + 1)
        return findPath(x + 1, y) + findPath(x, y + 1)

    return findPath(0, 0)


def main():
    assert uniquePaths(3, 2) == 3
    assert uniquePaths(7, 3) == 28

    print("All test cases passed!")


if __name__ == "__main__":
    main()

