# This problem was asked by Facebook.

# Given a string of round, curly, and square open and closing brackets, return whether the brackets are balanced (well-formed).

# For example, given the string "([])[]({})", you should return true.

# Given the string "([)]" or "((()", you should return false.

def isBalanced(input_str):
    open_brackets = "({["
    helper_stack = []

    for bracket in input_str:
        if bracket in open_brackets:
            helper_stack.append(bracket)

        else:
            if (bracket == ")" and helper_stack[-1] == "(") or (bracket == "}" and helper_stack[-1] == "{") or (bracket == "]" and helper_stack[-1] == "["):
                helper_stack.pop()
    
    if helper_stack:
        return False

    return True

    
def main():
    input_str = "((()"
    print(isBalanced(input_str)) # False

if __name__ == "__main__":
    main()