def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    
    memo[n] = fib(n-1, memo) + fib(n-2, memo)
    return memo[n]


def main():
    assert fib(6) == 8
    assert fib(7) == 13
    assert fib(8) == 21
    assert fib(50) == 12586269025

    print("All test cases passed!")


if __name__ == "__main__":
    main()