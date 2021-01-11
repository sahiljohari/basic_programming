"""
Write a function `allConstruct(target, wordBank)` that accepts a
target string and an array of strings.

The function should return a 2D array containing all of the ways
that the `target` can be constructed by concatenating elements of
the `wordBank` array. Each element of the 2D array should represent
one combination that constructs the `target`.

You may reuse elements of `wordBank` as many times as needed.
"""


def allConstruct(target, wordBank, memo={}):

    if target in memo:
        return memo[target]

    if target == "":
        return [[]]

    result = []

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            suffixWays = allConstruct(suffix, wordBank, memo)
            targetWays = [[word] + way for way in suffixWays]
            result += targetWays

    memo[target] = result
    return result


def main():
    assert allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]) == [
        ["purp", "le"],
        ["p", "ur", "p", "le"],
    ]
    assert allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == [
        ["ab", "cd", "ef"],
        ["ab", "c", "def"],
        ["abc", "def"],
        ["abcd", "ef"],
    ]
    assert (
        allConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == []
    )

    assert (
        allConstruct(
            "aaaaaaaaaaaaaaaaaaaaaaaaaaaaz", ["a", "aa", "aaa", "aaaa", "aaaaa"]
        )
        == []
    )

    print("All test cases passed!")


if __name__ == "__main__":
    main()