from tree_core import btree

class Node:
    def __init__(self, value):
        self.value = value
        self.left_child = None
        self.right_child = None

        self.height = 0
        self.l_height = 0
        self.r_height = 0
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

    def node_height(self, node):
        sum_left = 0
        sum_right = 0 
        # Edge case 1
        if node is None:
            return 0
        if node.left_child is not None:
            sum_left = self.node_height(node.left_child) + 1

        if node.right_child is not None:
            sum_right = self.node_height(node.right_child) + 1
        
        return sum_left if sum_left > sum_right else sum_right
    
    def get_factor(self, node):
        left_factor = 0
        right_factor = 0
        if node.left_child is not None:
            left_factor = node.left_child.l_height
        if node.right_child is not None:
            right_factor = node.right_child.r_height
        return right_factor - left_factor
    
    def _add_avl_node(self, node, new_node):
        # For left insertions
        if new_node.value < node.value:
            # Adding the node
            if node.left_child is None:
                node.left_child = new_node
                node.height = self.node_height(node)
                node.l_height = node.height + 1
                return None
            else:
                nr = self._add_avl_node(node.left_child, new_node)
                # if nr is not null, means that a rotation was made and we need to
                # update the parent node pointer.
                if nr is not None:
                    if self.DEBUG: print('Referencing parent: ', node.value)
                    node.left_child = nr
                    return
                node.height = self.node_height(node)
                node.l_height = node.height + 1
                if self.DEBUG: print('Height of ', node.value, ' is: ', node.height)
                # Self-balance
                if self.get_factor(node) > 1:
                    if self.DEBUG: print('Node ', node.value,' needs a left rotation')
                    return self.rotation('L', node)
                if self.get_factor(node) < -1:
                    if self.DEBUG: print('Node ', node.value,' needs a right rotation')
                    return self.rotation('R', node)
                
                return nr
        # For right insertions
        else:
            if node.right_child is None:
                # Adding the node
                node.right_child = new_node
                node.height = self.node_height(node)
                node.r_height = node.height + 1
                return None
            else:
                nr = self._add_avl_node(node.right_child, new_node)
                # if rn is not null, means that a rotation was made and we need to
                # update the parent node pointer.
                if nr is not None:
                    if self.DEBUG: print('Referencing parent: ', node.value)
                    node.right_child = nr
                    return
                node.height = self.node_height(node)
                node.r_height = node.height + 1
                # Self-balance
                if self.get_factor(node) > 1:
                    if self.DEBUG: print('Node ', node.value,' needs a left rotation...')
                    node_rotated = self.rotation('L', node)
                    node.height = self.node_height(node)
                    node.r_height = self.node_height(node.right_child) + 1
                    node.l_height = self.node_height(node.left_child) + 1
                    if self.root.value == node.value:
                        self.root = node_rotated 
                        return None
                    return node_rotated
                if self.get_factor(node) < -1:
                    if self.DEBUG: print('Node ', node.value,' needs a right rotation')
                    node_rotated = self.rotation('R', node)
                    node.height = self.node_height(node)
                    node.r_height = self.node_height(node.right_child) + 1
                    node.l_height = self.node_height(node.left_child) + 1
                    if self.root.value == node.value:
                        self.root = node_rotated 
                        return None
                    return node_rotated
                
                return nr
        return None

    def add_node(self, value):
        # Border case
        if self.root is None:
            self.root = Node(value)
            return
        root = self.root
        new_node = Node(value)
        self._add_avl_node(root, new_node)