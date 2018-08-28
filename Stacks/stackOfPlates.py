'''
--------------------------------------------------------------------------------------------------
Imagine a (literal) stack of plates. If the stack gets too high, it might topple.
Therefore, in real life, we would likely start a new stack when the previous stack exceeds some
threshold. Implement a data structure SetOfStacks that mimics this. SetOfStacks should be
composed of several stacks and should create a new stack once the previous one exceeds capacity.
SetOfStacks.push () and SetOfStacks.pop () should behave identically to a single stack
(that is, pop () should return the same values as it would if there were just a single stack).
---------------------------------------------------------------------------------------------------
**FOLLOW UP**
Implement a function popAt(int index) which performs a pop operation on a specific sub-stack.
'''
class set_of_stacks:
    def __init__(self, threshold):
        self.stack = [[]]
        self.threshold = threshold

    # Prints the whole set of stacks
    def traverse(self):
        print(self.stack)

    # Returns the index of last stack in the set
    def last_stack_idx(self):
        return len(self.stack)-1

    # Check if the last sub-stack is empty
    def is_empty(self, idx):
        if idx == self.last_stack_idx():
            return self.stack[self.last_stack_idx()] == []
        else:
            return self.stack[idx] == []

    # Pushes an element to last sub-stack
    def push(self, val):
        if len(self.stack[self.last_stack_idx()]) >= self.threshold:
            self.stack.append([])            
        self.stack[self.last_stack_idx()].append(val)

    # Pops an element from the last sub-stack
    def pop(self):
        if self.is_empty(self.last_stack_idx()):
            self.stack.pop()
        if self.stack == []:
            return None
        else:
            return self.stack[self.last_stack_idx()].pop()

    # Pops an element from a specific sub-stack
    def pop_at(self, idx):
        if self.is_empty(idx):
            self.stack.pop()
        if self.stack == [] or self.stack[idx] is None:
            return None
        else:
            return self.stack[idx].pop()

if __name__=="__main__":
    stacks = set_of_stacks(5)
    for i in range(6):
        stacks.push(i*2)
    stacks.traverse()

    for i in range(7):
        stacks.push(i*3)
    stacks.traverse()

    for _ in range(4):
        stacks.pop()
        stacks.pop()
        stacks.pop()
        stacks.pop()
    stacks.traverse()

    stacks.pop_at(2)
    stacks.traverse()