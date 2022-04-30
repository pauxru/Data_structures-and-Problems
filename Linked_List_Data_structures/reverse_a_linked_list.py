
# class Node:
#     def __init__(self, data=0, next=None):
#         self.data = data
#         self.next = next

# 1 -> 2 -> 3 -> 4 -> Null


def reverse_linked_list(head):
    """
    Take the head of a linked list and reverse the pointers
    NB: No reversing of the values but just the pointer
    :param head: The head node
    :return: the head of the reversed linked list
    """
    prev, curr = None, head  # previous set to none and current set to head first
    while curr:  # While current is not null
        nxt_val = curr.next  # Temp store for the current's next variable
        curr.next = prev  # current's next variable now points to the previous value
        prev = curr  # previous value made the current value
        curr = nxt_val  # The current value takes the value of the previously next value
    return prev  # return the last previous value which is the head node of the reversed list
