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
    # Initialize 2 pointers, prev will initialize to None at first but this is where we will store the reversed LL
    # the curr pointer will be initialized with the head reference
    prev, curr = None, head
    # We'll iterate through the LL until we get to a null(i.e. end of the LL)
    while curr:
        # We need to save the next node in order to move to the next iteration of the loop after we modify the references
        nextNode = curr.next
        # Let's reverse the links of our current node. We need to update the next reference of node to point to prev
        curr.next = prev
        # Now we want to move further in our iteration, so the current node will become previous node, so we should set prev to curr
        prev = curr
        # Lastly, the nextNode will become the current node, so we should update curr to nextNode
        curr = nextNode
    return prev