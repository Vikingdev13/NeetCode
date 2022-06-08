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
    # initalize a dummy node to handle edge cases like if the LL has only 1 node or empty and 2 pointers
    dummy = fast = slow = ListNode(0, next=head)

    # move the fast pointer to the len of n down the LL
    for _ in range(n):
        fast = fast.next
    
    # while the fast pointer hasnt reached a null
    while fast.next:
        # iterate both pointers at the same time, 
        # but fast will be n nodes away from slow pointer
        slow = slow.next
        fast = fast.next
    # now the slow pointer should be at the node just BEFORE the node that needs removed, 
    # so take that nodes next pointer and connect it to the node AFTER the node that is being removed
    slow.next = slow.next.next
    # return the new list
    return dummy.next

head = [1,2,3,4,5]
n = 2

print(removeNthFromEnd(head, n))