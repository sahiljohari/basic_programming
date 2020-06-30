# Program to implement Linked List

# Create a node class
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # Find length of linked list
    def length(self):
        length = 1
        node = self
        while node != None:
            node = node.next
            length += 1
        return length

    # Traverse a linked list
    def traverse(self):
        node = self # start from the head node
        out_list = []
        while node is not None:
            out_list.append(str(node.val) + "->")
            node = node.next
        out_list.append("NULL")
        print(out_list)

    # Add a node to the linked list
    def add_node(self, obj):
        node = self
        while node.next is not None:
            node = node.next
        node.next = obj

    # Delete a node from a linked list
    def delete_node(self, val):
        node = self
        while node.next is not None:
            if node.next.val == val:
                node.next = node.next.next
            node = node.next

    # Remove duplicates from a linked list
    def remove_dups(self):
        buffer = []
        node = self
        while node is not None:
            if node.val not in buffer:
                buffer.append(node.val)
            else:
                self.delete_node(node.val)
            node = node.next

    # Get the kth to last element from a linked list
    def sublist(self, k):
        node = self
        count = 0
        while node is not None:
            if count == k:
                node.traverse()
                break
            else:
                count += 1
            node = node.next

# Add two linked lists from left to right
#  e.g. 1->2->3 + 8->7 => 321+78 = 399
def add_list_lr(list1, list2):
    carry = 0
    head_0 = Node(0)
    pointer = head_0

    while list1 is not None and list2 is not None:
        sum_ = list1.val + list2.val + carry
        carry = int(sum_/10)
        pointer.add_node(Node(sum_%10))
        list1 = list1.next
        list2 = list2.next

    if list1 is None:
        while list2 is not None:
            sum_ = list2.val + carry
            carry = int(sum_/10)
            pointer.add_node(Node(sum_%10))
            list2 = list2.next
    if list2 is None:
        while list1 is not None:
            sum_ = list1.val + carry
            carry = int(sum_/10)
            pointer.add_node(Node(sum_%10))
            list1 = list1.next

    if carry > 0:
        pointer.add_node(Node(carry))

    return head_0.next

def pad_zeros(n,node):
    head = node
    for _ in range(n):
        node0 = Node(0)
        node0.next = head
        head = node0
    return head

# Add two linked lists from right to left
#  e.g. 1->2->3 + 8->7 => 123+87 = 210
def add_list_rl(p1,p2):
    p1_len = p1.length()
    p2_len = p2.length()
    if p1_len > p2_len:
        p2 = pad_zeros(p1_len - p2_len, p2)
    elif p2_len > p1_len:
        p1 = pad_zeros(p2_len - p1_len, p1)
    result,carry_over = add_list_rl_helper(p1,p2)
    if carry_over > 0:
        new_node = Node(carry_over)
        new_node.next = result
        return new_node
    return result

def add_list_rl_helper(p1,p2,):
    if p1 == None and p2 == None:
        return None,0
    else:
        result,carry_over = add_list_rl_helper(p1.next,p2.next)
        sum_ = p1.val + p2.val + carry_over
        new_node = Node(sum_%10)
        new_node.next = result
        return new_node, int(sum_/10)


if __name__=="__main__":
    head = Node(1)
    node_1 = Node(2)
    node_2 = Node(3)
    node_3 = Node(4)
    head.add_node(node_1)
    head.add_node(node_2)
    head.add_node(node_3)

    print("Adding nodes...")
    head.traverse()

    print("Deleting nodes...")
    head.delete_node(3)
    head.traverse()

    print("Adding a duplicate node...")
    node_4 = Node(4)
    head.add_node(node_4)
    head.traverse()

    print("After removing duplicate element...")
    head.remove_dups()
    head.traverse()

    print("Adding more nodes...")
    head.add_node(Node(5))
    head.add_node(Node(6))
    head.add_node(Node(7))
    head.traverse()

    print("Printing list from 3rd to last...")
    head.sublist(3)

    print("---------------------\n1->2->3 + 8->7 => 321+78 = 399")
    head_1 = Node(1)
    head_1.add_node(Node(2))
    head_1.add_node(Node(3))

    head_2 = Node(8)
    head_2.add_node(Node(7))

    sum_lr = add_list_lr(head_1, head_2)
    sum_lr.traverse()

    print("1->2->3 + 8->7 => 123+87 = 210")
    sum_rl = add_list_rl(head_1, head_2)
    sum_rl.traverse()