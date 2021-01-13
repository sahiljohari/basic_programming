def countConstruct(target, wordBank):
    N = len(target)
    table = [0] * (N + 1)
    table[0] = 1

    for i in range(N + 1):
        if table[i] > 0:
            for word in wordBank:
                if target[i : i + len(word)] == word:
                    table[i + len(word)] += table[i]

    return table[N]


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