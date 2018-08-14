# Program to implement Stacks

# Create a stack class
class stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def is_empty(self):
        return self.size() == 0

    def pop(self):
        if self.is_empty():
            return None
        else:
            return self.stack.pop()

    def push(self, val):
        return self.stack.append(val)

    def peek(self):
        if self.is_empty():
            return None
        else:
            return self.stack[-1]

# Given a string of brackets, determine if the string is balanced
def string_balanced(strInput):
    st = stack()
    
    count = 1
    for chars in strInput:
        st.push(chars)

    popped = st.pop()
    while st.peek() == popped:
        count += 1
        popped = st.pop()

    if count == st.size():
        return True
    else:
        return False

if __name__=="__main__":
    strBrackets = "[[[[]]]"
    strText = "aaaAAA"
    for strings in [strBrackets, strText]:
        if string_balanced(strings):
            print("String is balanced..")
        else:
            print("Nope! Try again..")