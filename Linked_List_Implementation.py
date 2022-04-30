

class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        node = Node(data, self.head)
        self.head = node

    def print(self):
        if self.head is None:
            print("Linked List is empty")
            return
        itr = self.head  # iterator initialized as the head node
        llstr = ''  # Liked List String

        while itr:  # While true
            llstr += str(itr.data) + '-->'
            itr = itr.next
        print(llstr)

    def insert_at_end(self, data):
        if self.head is None:
            self.head = Node(data, None)

        itr = self.head
        while itr.next:
            itr = itr.next
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        # self.head = None  # wipe out everything before you append the list
        for data in data_list:
            self.insert_at_end(data)

    def get_length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next
        return count

    def remove_at(self, index):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.head = self.head.next
            return
        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def insert_at(self, index, data):
        if index < 0 or index >= self.get_length():
            raise Exception("Invalid index")
        if index == 0:
            self.insert_at_beginning(data)
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:
                node = Node(data, itr.next)
                itr.next = node
                break
            itr = itr.next
            count += 1

    # Exercise from: https://github.com/codebasics/data-structures-algorithms-python/blob/master/data_structures/
    # 3_LinkedList/3_linked_list_exercise.md
    def insert_after_value(self, data_after, data_to_insert):
        if self.head is None:  # if the linked list is empty
            return
        if self.head.data == data_after:  # inserting at second position
            self.head.next = Node(data_to_insert, self.head.next)
            return
        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break
            itr = itr.next

    def remove_by_value(self, data):
        if self.head is None:
            return

        if self.head.data == data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next

    def reverse_linked_list(self):
        prev, curr = None, self.head

        while curr.next:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        return prev


ll = LinkedList()
ll.insert_at_beginning(88)
ll.insert_at_beginning(75)
ll.insert_at_end(32)
ll.insert_values([63, 345, 74, 2, 12, 6, 'paul'])
# ll.remove_at(2)
# ll.insert_at(3, 'jj')
# ll.insert_after_value(2,"apple")
ll.print()
ll.reverse_linked_list()
ll.print()

