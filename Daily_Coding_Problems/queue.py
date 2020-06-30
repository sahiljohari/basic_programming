# Program to implement a Queue data structure

# is_empty
# enqueue
# dequeue
# size

class queue:
    def __init__(self):
        self.list = []

    def is_empty(self):
        return self.list == []

    def enqueue(self, val):
        self.list.insert(0, val)

    def dequeue(self):
        return self.list.pop()

    def size(self):
        return len(self.list)

if __name__=="__main__":
    q = queue()
    q.enqueue(4)
    q.enqueue('dog')
    q.enqueue(True)
    print(q.size())