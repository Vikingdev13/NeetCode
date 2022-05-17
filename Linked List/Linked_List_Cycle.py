"""
Given head, the head of a linked list, determine if the linked list has a cycle in it.
"""

"""
Time: O(n) -since we may have to reach the end of the list before detecting a cycle 
or there is no cycle and we had to traverse the entire list to determine this

Space: O(1)
"""
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def hasCycle(head):
    # initialize two different pointers and set them to the beginning of the list, 
    # Im calling them 'fast' and 'slow' since one will move faster than the other
    slow = fast = head

    # while fast ptr is not null, bc if it is then there is no cycle
    while fast and fast.next:
        # increment the fast ptr by 2
        # increment the slow ptr by 1
        fast = fast.next.next
        slow = slow.next
        # if the fast ptr catches up to the slow ptr, there is a cycle
        if fast == slow:
            return True
    return False