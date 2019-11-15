

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

        self.height = 0
        self.factor = 0

    def dispose(self):
        self.value = None
        self.left_child = None
        self.right_child = None

class Structure:
    def __init__(self):
        self.root = None

    def print_pre_order(self, node):
        if node is None:
            return
        print(node.value)
        self.print_pre_order(node.left_child)
        self.print_pre_order(node.right_child)

    def node_height(self, node):
        sum_left = 0
        sum_right = 0 
        # Edge case 1.
        if node is None:
            return 0
        if node.left_child is not None:
            sum_left = self.node_height(node.left_child) + 1

        if node.right_child is not None:
            sum_right = self.node_height(node.right_child) + 1
        
        return sum_left if sum_left > sum_right else sum_right

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
        while smallest_node.left_child is not None:
            copy_parent = smallest_node
            smallest_node = smallest_node.left_child
        copy_parent.left_child = None 
        return smallest_node

    def _search_bigest_into_left(self, node):
        bigest_node = node.left_child
        while bigest_node.right_child is not None:
            copy_parent = bigest_node
            bigest_node = bigest_node.right_child
        copy_parent.right_child = None
        return bigest_node

    def _remove_node(self, parent_node, node_to_remove):
        left_child = parent_node.left_child
        right_child = parent_node.right_child
        if left_child.value == node_to_remove.value:
            # Simple cases.
            if node_to_remove.left_child is None and node_to_remove.right_child is not None:
                parent_node.left_child = node_to_remove.right_child
                return True

            elif node_to_remove.left_child is not None and node_to_remove.right_child is None:
                parent_node.left_child = node_to_remove.left_child
                return True

            # Both nulls.
            elif node_to_remove.left_child is not None and node_to_remove.right_child is not None: 
                new_node = self._search_smallest_into_rigth(node_to_remove)
                parent_node.left_child = new_node
                new_node.left_child = node_to_remove.left_child
                new_node.right_child = node_to_remove.right_child
                return True
        
        elif right_child.value == node_to_remove.value:
            # Simple cases.
            if node_to_remove.left_child is None and node_to_remove.right_child is not None:
                parent_node.right_child = node_to_remove.right_child
                return True

            elif node_to_remove.left_child is not None and node_to_remove.right_child is None:
                parent_node.right_child = node_to_remove.left_child
                return True

            # Both nulls.
            elif node_to_remove.left_child is not None and node_to_remove.right_child is not None: 
                new_node = self._search_bigest_into_left(node_to_remove)
                parent_node.right_child = new_node
                new_node.left_child = node_to_remove.left_child
                new_node.right_child = node_to_remove.right_child
                return True

        if node_to_remove.value < parent_node.value:
            return self._remove_node(left_child, node_to_remove)
        else:
            return self._remove_node(right_child, node_to_remove)
        
        return False

    def _add_node(self, node, new_node):
        if new_node.value < node.value:
            if node.left_child is None:
                node.left_child = new_node
            else:
                self._add_node(node.left_child, new_node)
        else:
            if node.right_child is None:
                node.right_child = new_node
            else:
                self._add_node(node.right_child, new_node)
        return
    
    def search_node(self, value):
        root = self.root
        return self._search_node(root, value)

    def remove_node(self, value):
        root = self.root
        node_found = self.search_node(value)
        # Border case.
        if node_found is None:
            return False
        if self._remove_node(root, node_found):
            node_found = None
            print('Deleted!')
            return

    def add_node(self, value):
        # Border case.
        if self.root is None:
            self.root = Node(value)
            return
        root = self.root
        new_node = Node(value)
        self._add_node(root, new_node)
