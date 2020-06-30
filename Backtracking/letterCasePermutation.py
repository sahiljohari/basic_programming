# Leetcode: Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.  Return a list of all possible strings we could create.
def letterCasePermutation(S: str):
    output = []
    N = len(S)

    def backtrack(sub, i):
        if len(sub) == N:
            output.append(sub)
        else:
            if S[i].isalpha():
                backtrack(sub + S[i].swapcase(), i + 1)
            backtrack(sub + S[i], i + 1)

    backtrack("", 0)
    return output

def main():
  assert letterCasePermutation('a1b2') == ["A1B2","A1b2","a1B2","a1b2"]
  assert letterCasePermutation('3z4') == ["3Z4", "3z4"]
  assert letterCasePermutation('12345') == ["12345"]

  print("All test cases passed!")

if __name__ == "__main__":
  main()