# Generate all permutations of a given string


def permutations(S: str):
    str_list = list(S)
    output = []

    def permute(left, right):
        if left == right:
            output.append("".join(str_list))

        else:
            for i in range(left, right + 1):
                str_list[left], str_list[i] = str_list[i], str_list[left]
                permute(left + 1, right)
                str_list[left], str_list[i] = str_list[i], str_list[left]

    permute(0, len(S) - 1)
    return output


def main():
    assert permutations("ABC") == ["ABC", "ACB", "BAC", "BCA", "CBA", "CAB"]
    print("All test cases passed!")


if __name__ == "__main__":
    main()
