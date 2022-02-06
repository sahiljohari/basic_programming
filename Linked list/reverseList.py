# Reverse a linked list in-place

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# recursive
def reverse(head, prev = None):
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    if head is None:
        return prev

    next = head.next
    head.next = prev
    return reverse(next, head)

# iterative
def reverseList(head):
    '''
    Time complexity: O(n)
    Space complexity: O(1)
    '''
    prev, current = None, head

    while current:
        next = current.next
        current.next = prev
        prev = current
        current = next
    
    return prev

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
    input_list = createLinkedList([1, 4, 5, 3, 6])
    printLinkedList(reverse(input_list))  # [6, 3, 5, 4, 1]
    printLinkedList(reverseList(input_list))  # [6, 3, 5, 4, 1]

if __name__ == "__main__":
    main()