# Given an array of k linked-lists lists, each linked-list is sorted in ascending order.
# Merge all the linked-lists into one sorted linked-list and return it.

from typing import List


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeKLists(lists: List[ListNode]) -> ListNode:
    """
    Time complexity : O(Nlogk)
    Space complexity: O(1)
    """
    if not lists:
        return

    if len(lists) == 1:
        return lists[0]

    mid = len(lists) // 2

    left = mergeKLists(lists[:mid])
    right = mergeKLists(lists[mid:])

    return merge(left, right)


def merge(l1, l2):
    current = head = ListNode()

    while l1 and l2:
        if l1.val <= l2.val:
            current.next = l1
            current = current.next
            l1 = l1.next
        else:
            current.next = l2
            current = current.next
            l2 = l2.next

    if l1:
        current.next = l1
    else:
        current.next = l2

    return head.next


def createLinkedList(list):
    if not list:
        return None

    head = current = ListNode(list[0])

    for i in range(1, len(list)):
        current.next = ListNode(list[i])
        current = current.next
    return head


def printLinkedList(head):
    if not head:
        return None

    while head:
        print(head.val)
        head = head.next


def main():
    input_lists = [createLinkedList(list) for list in [[1, 4, 5], [1, 3, 4], [2, 6]]]
    printLinkedList(mergeKLists(input_lists))  # [1, 1, 2, 3, 4, 4, 5, 6]


if __name__ == "__main__":
    main()