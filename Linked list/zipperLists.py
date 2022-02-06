'''
Write a function, zipper_lists, that takes in the head of two linked lists 
as arguments. The function should zipper the two lists together into single 
linked list by alternating nodes. If one of the linked lists is longer than 
the other, the resulting list should terminate with the remaining nodes. 
The function should return the head of the zippered linked list.

# Do this in-place, by mutating the original Nodes.
# You may assume that both input lists are non-empty.
''' 

# class Node:
#   def __init__(self, val):
#     self.val = val
#     self.next = None

# iterative
def zipper_lists(head_1, head_2):
  '''
  Time complexity: O(min(m,n))
  Space complexity: O(1)
  '''

  tail = head_1
  c1, c2 = head_1.next, head_2
  count = 0
  
  while c1 and c2:
    if count % 2 == 0:
      tail.next = c2
      c2 = c2.next
    else:
      tail.next = c1
      c1 = c1.next
      
    tail = tail.next
    count += 1
    
  if c1:
    tail.next = c1
  if c2:
    tail.next = c2
  
  return head_1

# recursive
def zipper_lists(head_1, head_2):
  '''
  Time complexity: O(min(m,n))
  Space complexity: O(min(m,n))
  '''

  if not head_1 and not head_2: return None
  if not head_1: return head_2
  if not head_2: return head_1

  next1, next2 = head_1.next, head_2.next
  head_1.next = head_2
  head_2.next = zipper_lists(next1, next2)
  
  return head_1
