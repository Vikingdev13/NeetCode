"""
Given the head of a linked list, remove the nth node from the end of the list and return its head.
"""
"""
Time: O(n)
Space: O(1)
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

def removeNthFromEnd(head, n):    
    dummy = ListNode(0, head)
    left, right = dummy, head

    while n > 0 and right:
        right = right.next
        n -= 1
    
    while right:
        left = left.next
        right = right.next

    left.next = left.next.next
    return dummy.next

head = [1,2,3,4,5]
n = 2

print(removeNthFromEnd(head, n))