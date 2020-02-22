# Given an unsorted linked list, write a function to remove all the duplicates.
# For example, dedup(1 -> 2 -> 3 -> 2 -> 1) = 1 -> 2 -> 3

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def print_list(head):
    node = head
    out_list = []
    print("HEAD->", end='')
    while node is not None:
        out_list.append(str(node.val) + "->")
        node = node.next
    out_list.append("NULL")
    print(''.join(out_list))

def isEqual(n1, n2):
    l1, l2 = [], []
    c1, c2 = n1, n2

    while c1 is not None:
        l1.append(c1.val)
        c1 = c1.next

    while c2 is not None:
        l2.append(c2.val)
        c2 = c2.next

    return l1 == l2

def add_node(head, obj):
        node = head
        while node.next is not None:
            node = node.next
        node.next = obj

def dedup(head):
    '''
    Time complexity: O(n)
    Space complexity: O(n)
    '''
    seen = set()

    current = head
    seen.add(current.val)
    while current.next is not None:
        if current.next.val not in seen:
            seen.add(current.next.val)
            current = current.next
        else:
            duplicate = current.next
            current.next = current.next.next
            del duplicate

    return head

def main():
    nums = [1,2,3,2,1]
    input_list = Node(nums[0])
    for num in nums[1:]:
        add_node(input_list, Node(num))

    unique_nums = [1,2,3]
    out_list = Node(unique_nums[0])
    for num in unique_nums[1:]:
        add_node(out_list, Node(num))

    assert isEqual(dedup(input_list), out_list) == True, "Test case failure"

    print("All test cases passed.")

if __name__ == "__main__":
    main()