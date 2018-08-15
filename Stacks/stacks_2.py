# Implement a queue with two stacks
from stacks import stack

class my_queue(stack):
    def __init__(self):
        self.s1 = stack()
        self.s2 = stack()

    def size(self):
        return self.s1.size() + self.s2.size()

    def add(self, val):
        self.s1.push(val)

    def shift_stacks(self):
        if self.s2.is_empty():
            while not self.s1.is_empty():
                self.s2.push(self.s1.pop())

    def remove(self):
        self.shift_stacks()
        return self.s2.pop()

if __name__=="__main__":
    q = my_queue()
    q.add(1)
    q.add(2)
    q.add(3)
    q.add(4)
    q.add(5)
    print("Number of elements in queue:", q.size())
    print("Element removed:", q.remove())
    print("Number of elements in queue after remove():", q.size())