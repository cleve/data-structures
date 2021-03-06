class Node:
    def __init__(self, value):
        self.next = None
        self.value = value

class LinkedList:
    def __init__(self):
        # Pointers.
        self.root = None
        self.last_node = None

    def _count_elements(self):
        temporal_pointer = self.root
        counter = 0
        # Border case
        if self.root is None:
            return 0
        
        while True:
            counter += 1
            if temporal_pointer.next is None:
                break
            temporal_pointer = temporal_pointer.next
        return counter

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

    def _find_node(self, value):
        temporal_pointer = self.root
        while True:
            if temporal_pointer.value == value:
                return temporal_pointer
            # End of linked list.
            if temporal_pointer.next is None:
                break
            temporal_pointer = temporal_pointer.next
        return None

    def count(self):
        print(self._count_elements())

    def find_node(self, value):
        """Return True if the element exists, False otherwise
        """
        return self._find_node(value) is not None

    def remove_node(self, value):
        node_to_remove = self._find_node(value)
        if node_to_remove is None:
            return
        # Removing it.
        temporal_pointer = self.root
        # Border.
        if temporal_pointer.value == value:
            self.root = None
        # General.
        while True:
            if temporal_pointer.next is not None and temporal_pointer.next.value == value:
                temporal_pointer.next = temporal_pointer.next.next
                break
            # End of linked list.
            if temporal_pointer.next is None:
                break
            temporal_pointer = temporal_pointer.next