"""
Write a function `countConstruct(target, wordBank)` that accepts a target
string and an array of strings.
The function should return the number of ways that the `target`
can be constructed by concatenating elements of the `wordBank` array.
You may reuse elements of `wordBank` as many times as needed.
"""


def countConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return 1

    totalCount = 0

    for word in wordBank:
        if target.startswith(word):
            totalCount += countConstruct(target[len(word) :], wordBank, memo)

    memo[target] = totalCount
    return totalCount


def main():

    assert countConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == 1
    assert countConstruct("purple", ["purp", "p", "ur", "le", "purpl"]) == 2
    assert (
        countConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"]) == 0
    )
    assert (
        countConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
        == 4
    )
    assert (
        countConstruct(
            "eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
        )
        == 0
    )

    print("All test cases passed!")


if __name__ == "__main__":
    main()