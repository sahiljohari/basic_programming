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
