"""
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list
"""


"""
Time: O(n+m)
Space: O(1)
** It is constant space since we're not creating new Node instances on each iteration, 
just rearranging the links between the existing objects, thus the only memory overhead
are the new references for manipulating the lists
"""
class Node:
    def __init__(self, val, next):
        self.val = val
        self.next = next

def mergeTwoLists(L1, L2):
    # initialize a dummy node to handle edge cases such as inserting into an empty list
    dummy = Node()
    tail = dummy
    # while list 1 and list 2 are not empty
    while L1 and L2:
        # if the val in list 1 is less than the val in list 2, 
        # insert the val of list 1 into the new list
        if L1.val < L2.val:
            tail.next = L1
            L1 = L1.next
        # else the val of list 2 is less, then insert it into the new list
        else:
            tail.next = L2
            L2 = L2.next
        # traverse down the list
        tail = tail.next
    # edge case: if one of the lists are empty, or one list has more elements than the other
    # we will just append the values from the non-empty list/lesser element having list into the new list
    if L1:
        tail.next = L1
    elif L2:
        tail.next = L2

    return dummy.next