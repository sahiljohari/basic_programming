def gridTraveler(m, n):
    table = [[0 for _ in range(n + 1)] for _ in range(m + 1)]
    table[1][1] = 1

    for row in range(m + 1):
        for col in range(n + 1):
            if row < m:
                table[row + 1][col] += table[row][col]
            if col < n:
                table[row][col + 1] += table[row][col]

    return table[m][n]


def main():
    assert gridTraveler(3, 2) == 3
    assert gridTraveler(3, 3) == 6
    assert gridTraveler(7, 3) == 28
    assert gridTraveler(18, 18) == 2333606220

    print("All test cases passed!")


if __name__ == "__main__":
    main()