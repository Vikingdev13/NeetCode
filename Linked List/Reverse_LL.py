"""
Given the head of a singly linked list, reverse the list, and return the reversed list
"""
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
"""
Time: O(n)
Space: O(1)
"""
def reverseList(head):
    prev, curr = None, head

    while curr:
        tmp = curr.next
        curr.next = prev
        prev = curr
        curr = tmp
    return prev