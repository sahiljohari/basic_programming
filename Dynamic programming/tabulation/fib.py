def fib(n):
    table = [0 for _ in range(n + 2)]
    table[1] = 1

    for i in range(0, n + 1):
        table[i + 1] += table[i]
        if i < n:
            table[i + 2] += table[i]

    return table[n]


def main():
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(50) == 12586269025

    print("All test cases passed!")


if __name__ == "__main__":
    main()