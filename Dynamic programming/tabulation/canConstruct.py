def canConstruct(target, wordBank):
    table = [False] * (len(target) + 1)
    table[0] = True

    for i in range(len(target) + 1):
        if table[i] == True:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] = True

    return table[len(target)]


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