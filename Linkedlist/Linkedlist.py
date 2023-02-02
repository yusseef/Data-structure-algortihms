'''
A linked list is a linear data structure, in which the elements are not stored at contiguous memory locations.
The elements in a linked list are linked using pointers
'''

class Node:
    def __init__(self, data = None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_the_beginning(self, data):
        self.head = Node(data, self.head)

    def print(self):
        if self.head is None:
            print("This is empty linkedlist")
        
        itr = self.head

        llstr = ''

        while itr:
            llstr += str(itr.data) + '====>'
            itr = itr.next
        
        print(llstr)

    def insert_at_the_end(self, data):
        if self.head is None:
            node = Node(data, None)
        
        itr = self.head

        while itr.next:
            itr = itr.next
        
        itr.next = Node(data, None)

    def insert_values(self, data_list):
        for elem in data_list:
            self.insert_at_the_end(elem)



linked_list = LinkedList()
linked_list.insert_at_the_beginning(5)
linked_list.insert_at_the_beginning(7)
linked_list.insert_at_the_end(9)
linked_list.insert_values([10, 11, 12])



linked_list.print()