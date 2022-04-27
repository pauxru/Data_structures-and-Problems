# Linked List implementation
class Node:
    """
    The data is what we're actually storing while
    next is the pointer to the next data. Stored as one package
    """
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


lst = ['A', 'B', 'C', 'D', 'E']
ll = Node()
for i in range(len(lst) - 1):
    ll.data = lst[i]
    ll.next = lst[i + 1]
    print(f"{ll.data} --> {ll.next}")

"""
A --> B
B --> C
C --> D
D --> E
"""