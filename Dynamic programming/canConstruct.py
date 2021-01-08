"""
Write a function `canConstruct(target, wordBank)` that accepts a target
string and an array of strings.
The function should return a boolean indicating whether or not the `target`
can be constructed by concatenating elements of the `wordBank` array.
You may reuse elements of `wordBank` as many times as needed.
"""


def canConstruct(target, wordBank, memo={}):
    if target in memo:
        return memo[target]

    if target == "":
        return True

    for word in wordBank:
        if target.startswith(word):
            suffix = target[len(word) :]
            if canConstruct(suffix, wordBank, memo) == True:
                memo[target] = True
                return True

    memo[target] = False
    return False


def main():

    assert canConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd"]) == True
    assert (
        canConstruct("skateboard", ["bo", "rd", "ate", "t", "ska", "sk", "boar"])
        == False
    )
    assert (
        canConstruct("enterapotentpot", ["a", "p", "ent", "enter", "ot", "o", "t"])
        == True
    )
    assert (
        canConstruct(
            "eeeeeeeeeeeeeeeeeeeeeeeeef", ["e", "ee", "eee", "eeee", "eeeee", "eeeeee"]
        )
        == False
    )

    print("All test cases passed!")


if __name__ == "__main__":
    main()