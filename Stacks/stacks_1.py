# Given a string of brackets, determine if the string is balanced
from stacks import stack

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