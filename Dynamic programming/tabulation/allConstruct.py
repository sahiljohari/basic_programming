def allConstruct(target, wordBank):
    N = len(target)
    table = [[] for _ in range(N + 1)]
    table[0] = [[]]

    for i in range(0, (N + 1)):
        for word in wordBank:
            if target[i : i + len(word)] == word:
                newCombination = [ways + [word] for ways in table[i]]
                for combination in newCombination:
                    table[i + len(word)] += [combination]

    return table[N]


def main():
    assert allConstruct("purple", ["purp", "p", "ur", "le", "purpl"]) == [
        ["purp", "le"],
        ["p", "ur", "p", "le"],
    ]
    assert allConstruct("abcdef", ["ab", "abc", "cd", "def", "abcd", "ef", "c"]) == [
        ["abc", "def"],
        ["ab", "c", "def"],
        ["abcd", "ef"],
        ["ab", "cd", "ef"],
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