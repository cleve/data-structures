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

    def node_height(self, node):
        sum_left = 0
        sum_right = 0 
        # Edge case 1.
        if node is None:
            return 1
        if node.left_child is not None:
            sum_left = self.node_height(node.left_child) + 1

        if node.right_child is not None:
            sum_right = self.node_height(node.right_child) + 1
        
        return sum_left if sum_left > sum_right else sum_right
    
    def get_factor(self, node):
        left_height = 0
        right_height = 0
        if node.left_child is not None:
            left_height = node.left_child.height
        if node.right_child is not None:
            right_height = node.right_child.height
        return right_height - left_height
    
    def _add_avl_node(self, node, new_node):
        if new_node.value < node.value:
            # Adding the node
            if node.left_child is None:
                node.left_child = new_node
                node.height = self.node_height(node)
                print('Height of ', node.value, ' is ', node.height)
                return new_node
            else:
                rn = self._add_avl_node(node.left_child, new_node)
                node.height = self.node_height(node)
                print('Height of ', node.value, ' is: ', node.height)
                # Self-balance
                if self.get_factor(node) > 1:
                    print('Node ', node.value,' needs a right rotation')
                if self.get_factor(node) < -1:
                    print('Node ', node.value,' needs a left rotation')
                
                return rn
        else:
            if node.right_child is None:
                # Adding the node
                node.right_child = new_node
                node.height = self.node_height(node)
                print('Height of ', node.value, ' is ', node.height)
                return new_node
            else:
                rn = self._add_avl_node(node.right_child, new_node)
                node.height = self.node_height(node)
                print('Height of ', node.value, ' is: ', node.height)
                # Self-balance
                if self.get_factor(node) > 1:
                    print('Node ', node.value,' needs a right rotation')
                if self.get_factor(node) < -1:
                    print('Node ', node.value,' needs a left rotation')
                
                return rn
        return node

    def add_node(self, value):
        # Border case.
        if self.root is None:
            self.root = Node(value)
            return
        root = self.root
        new_node = Node(value)
        self._add_avl_node(root, new_node)
        # Border Self-balance
        print('ROOT FACTOR: ', self.get_factor(root))
        if self.get_factor(root) > 1:
            print('Node ', root.value,' needs a right rotation')
        if self.get_factor(root) < -1:
            print('Node ', root.value,' needs a left rotation')