

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None
        self.height = 0

        # For AVL rotations
        self.factor = 0

    def dispose(self):
        self.value = None
        self.left_child = None
        self.right_child = None

class Structure:
    def __init__(self):
        self.root = None
        self.is_avl = False

        # For DEV
        self.DEBUG = True

    def print_pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.print_pre_order(node.left_child)
        self.print_pre_order(node.right_child)

    def _search_node(self, node, node_to_search):
        if node is None:
            return None
        if node.value == node_to_search:
            return node
        if node_to_search < node.value:
            return self._search_node(node.left_child, node_to_search)
        elif node_to_search > node.value:
            return self._search_node(node.right_child, node_to_search)
        return None

    def _search_smallest_into_rigth(self, node):
        smallest_node = node.right_child
        copy_parent = smallest_node
        while smallest_node.left_child is not None:
            copy_parent = smallest_node
            smallest_node = smallest_node.left_child
        copy_parent.left_child = None 
        return smallest_node

    def _search_bigest_into_left(self, node):
        bigest_node = node.left_child
        copy_parent = bigest_node
        while bigest_node.right_child is not None:
            copy_parent = bigest_node
            bigest_node = bigest_node.right_child
        copy_parent.right_child = None
        return bigest_node

    def _remove_node(self, current_node, node_to_remove):
        # Inner function to reallocate pointers
        def new_pointers(parent_node, node_to_remove, direction):
            # Simple cases left.
            if direction == 'L' and node_to_remove.left_child is None and node_to_remove.right_child is not None:
                # Used only to remove root node
                if parent_node is None:
                    self.root = node_to_remove.right_child
                else:
                    parent_node.left_child = node_to_remove.right_child
                return True

            elif direction == 'L' and node_to_remove.left_child is not None and node_to_remove.right_child is None:
                # Used only to remove root node
                if parent_node is None:
                    self.root = node_to_remove.left_child
                else:
                    parent_node.left_child = node_to_remove.left_child
                return True

            # Both not nulls.
            elif direction == 'L' and node_to_remove.left_child is not None and node_to_remove.right_child is not None: 
                new_node = self._search_smallest_into_rigth(node_to_remove)
                # Used only to remove root node
                if parent_node is None:
                    self.root = new_node
                else:
                    parent_node.left_child = new_node
                new_node.left_child = node_to_remove.left_child
                if new_node.value == node_to_remove.right_child.value:
                    return True
                new_node.right_child = node_to_remove.right_child
                return True

            # Both nulls
            elif direction == 'L' and node_to_remove.left_child is None and node_to_remove.right_child is None:
                if parent_node is None:
                    self.root = None
                else:
                    parent_node.left_child = None
                return True
    
            # Simple cases right
            elif direction == 'R' and node_to_remove.left_child is None and node_to_remove.right_child is not None:
                parent_node.right_child = node_to_remove.right_child
                return True

            elif direction == 'R' and node_to_remove.left_child is not None and node_to_remove.right_child is None:
                parent_node.right_child = node_to_remove.left_child
                return True

            # Both not nulls
            elif direction == 'R' and node_to_remove.left_child is not None and node_to_remove.right_child is not None: 
                new_node = self._search_bigest_into_left(node_to_remove)
                parent_node.right_child = new_node
                new_node.right_child = node_to_remove.right_child
                if new_node.value == new_node.left_child.value:
                    return True
                new_node.left_child = node_to_remove.left_child
                return True

            # Both nulls
            elif direction == 'R' and node_to_remove.left_child is None and node_to_remove.right_child is None: 
                parent_node.right_child = None
                return True
            return False

        if node_to_remove.value < current_node.value:
            if self._remove_node(current_node.left_child, node_to_remove) == 'found':
                return new_pointers(current_node, current_node.left_child, 'L')
        
        elif node_to_remove.value > current_node.value:
            if self._remove_node(current_node.right_child, node_to_remove) == 'found':
                return new_pointers(current_node, current_node.right_child, 'R')

        elif node_to_remove.value == current_node.value:
            # Root node
            if node_to_remove == self.root:
                return new_pointers(None, self.root, 'L')
            return 'found'

        return True
    
    def _add_node(self, node, new_node):
        # Check if the value is already into the tree
        if self._search_node(self.root, new_node.value) is not None:
            return None
        if new_node.value < node.value:
            if node.left_child is None:
                node.left_child = new_node
                return new_node
            else:
                rn = self._add_node(node.left_child, new_node)
                return rn
        else:
            if node.right_child is None:
                node.right_child = new_node
                return new_node
            else:
                rn = self._add_node(node.right_child, new_node)
                return rn
        return node
    
    def search_node(self, value):
        root = self.root
        return self._search_node(root, value)

    def remove_node(self, value):
        root = self.root
        node_found = self.search_node(value)
        # Border case
        if node_found is None:
            return False
        if self._remove_node(root, node_found):
            node_found = None
            return

    def add_node(self, value):
        # Border case
        if self.root is None:
            self.root = Node(value)
            return self.root
        root = self.root
        new_node = Node(value)
        return self._add_node(root, new_node) is not None
