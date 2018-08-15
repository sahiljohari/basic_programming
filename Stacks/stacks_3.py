# Program to sort a stack in ascending order (with biggest items on top). 
# Only use one additional stack.

from stacks import stack

def sort_stack(st):
    # Helper stack for sorting
    helper_st = stack()
    
    while not st.is_empty():
        # Insert each element in st into helper_st in sorted order
        buffer = st.pop()
        while not helper_st.is_empty() and helper_st.peek() > buffer:
            st.push(helper_st.pop())
        helper_st.push(buffer) 
    
    # Copy the elements back to st
    while not helper_st.is_empty():
        st.push(helper_st.pop())
   
    return st

if __name__=="__main__":
    st = stack()
    st.push(8)
    st.push(3)
    st.push(4)
    st.push(5)
    st.push(7)

    sort_stack(st).traverse()
