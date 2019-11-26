class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        # Pointers.
        self.root = None
        self.last_node = None

    def print_list(self):
        temporal_pointer = self.root
        while True:
            print('Value: ', temporal_pointer.value)
            # End of linked list.
            if temporal_pointer.next is None:
                break
            temporal_pointer = temporal_pointer.next
    
    def add_node(self, value):
        # Border case.
        if self.root is None:
            self.root = Node(value)
            self.last_node = self.root
            return

        self.last_node.next = Node(value)
        self.last_node = self.last_node.next

    
ll = LinkedList()
ll.add_node(99)
ll.add_node(1)
ll.add_node(22)
ll.add_node(24)
ll.add_node(29)

ll.print_list()

print(ll.root.value)
print(ll.last_node.value)