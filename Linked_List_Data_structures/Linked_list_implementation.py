# Linked List implementation
class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


lst = ['A', 'B', 'C', 'D', 'E']
ll = Node()
for i in range(len(lst) - 1):
    ll.data = lst[i]
    ll.next = lst[i + 1]
    print(f"{ll.data} --> {ll.next}")
