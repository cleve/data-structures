from tree_core import btree

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

class AVL (btree.Structure):
    def right_rotation(self, parent_node):
        b_node = parent_node.left_child
        parent_node.left_child = b_node.right_child
        b_node.right_child = parent_node
        return b_node

    def left_rotation(self, parent_node):
        a_node = parent_node.right_child
        parent_node.right_child = a_node.left_child
        a_node.left_child = parent_node
        return a_node

    def rotation(self, r_type, parent_node):
        if r_type == 'R':
            return self.right_rotation(parent_node)
        elif r_type == 'L':
            return self.left_rotation(parent_node)