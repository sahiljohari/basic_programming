"""
This is a class implementation of Binary Heap data structure (Min-Heap)
"""


class MinHeap:
    def __init__(self, capacity) -> None:
        self.storage = [0] * capacity
        self.capacity = capacity
        self.size = 0

    def getParentIndex(self, index):
        """
        Returns the index of parent element
        """
        return (index - 1) // 2

    def getLeftChildIndex(self, index):
        """
        Returns the index of left child element
        """
        return (2 * index) + 1

    def getRightChildIndex(self, index):
        """
        Returns the index of right child element
        """
        return (2 * index) + 2

    def hasParent(self, index):
        """
        Returns True if the index of parent exists, otherwise False (-1)
        """
        return self.getParentIndex(index) >= 0

    def hasLeftChild(self, index):
        """
        Returns True if the index of left child is within the size of heap
        """
        return self.getLeftChildIndex(index) < self.size

    def hasRightChild(self, index):
        """
        Returns True if the index of right child is within the size of heap
        """
        return self.getRightChildIndex(index) < self.size

    def parent(self, index):
        """
        Returns the parent element of element at input index
        """
        return self.storage[self.getParentIndex(index)]

    def leftChild(self, index):
        """
        Returns the left element of element at input index
        """
        return self.storage[self.getLeftChildIndex(index)]

    def rightChild(self, index):
        """
        Returns the right element of element at input index
        """
        return self.storage[self.getRightChildIndex(index)]

    def isFull(self):
        """
        Returns True if the heap has reached the capacity
        """
        return self.size == self.capacity

    def swap(self, index1, index2):
        """
        Swaps two elements of the heap at given input indices
        """
        self.storage[index1], self.storage[index2] = (
            self.storage[index2],
            self.storage[index1],
        )

    def insert(self, data):
        """
        Inserts data into the heap and performs a heapify operation
        """
        if self.isFull():
            raise ("Heap is full")
        self.storage[self.size] = data
        self.size += 1
        # self.heapifyUp()
        self.heapifyUpRec(self.size - 1)

    def heapifyUp(self):
        """
        Performs a heapify operation in upward direction
        """
        index = self.size - 1

        while self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            index = self.getParentIndex(index)

    def heapifyUpRec(self, index):
        """
        Performs heapifyUp() operation recursively
        """
        if self.hasParent(index) and self.parent(index) > self.storage[index]:
            self.swap(self.getParentIndex(index), index)
            self.heapifyUpRec(self.getParentIndex(index))

    def removeMin(self):
        """
        Removes topmost element from the heap and performs a heapify operation
        """
        if self.size == 0:
            raise ("Heap is empty")

        data = self.storage[0]
        self.storage[0] = self.storage[self.size - 1]
        self.size -= 1
        # self.heapifyDown()
        self.heapifyDownRec(0)
        return data

    def heapifyDown(self):
        """
        Performs a heapify operation in downward direction
        """
        index = 0

        while self.hasLeftChild(index):
            smallerChildIndex = self.getLeftChildIndex(index)
            if self.hasRightChild(index) and self.rightChild(index) < self.leftChild(
                index
            ):
                smallerChildIndex = self.getRightChildIndex(index)

            if self.storage[index] < self.storage[smallerChildIndex]:
                break
            else:
                self.swap(index, smallerChildIndex)

            index = smallerChildIndex

    def heapifyDownRec(self, index):
        """
        Performs heapifyDown() operation recursively
        """
        smallest = index

        if self.hasLeftChild(index) and self.storage[smallest] > self.leftChild(index):
            smallest = self.getLeftChildIndex(index)

        if self.hasRightChild(index) and self.storage[smallest] > self.rightChild(
            index
        ):
            smallest = self.getRightChildIndex(index)

        if smallest != index:
            self.swap(index, smallest)
            self.heapifyDownRec(smallest)
