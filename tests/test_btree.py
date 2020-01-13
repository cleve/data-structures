import unittest
import trees.tree_core.btree

class TestBtreeMethods(unittest.TestCase):

    def test_public_add_node(self):
        # Creating object
        tree = trees.tree_core.btree.Structure()
        # Adding nodes
        node_inserted = tree.add_node(20)
        self.assertTrue(node_inserted)

        node_inserted_r = tree.add_node(30)
        self.assertTrue(node_inserted_r)

        node_inserted_l = tree.add_node(10)
        self.assertTrue(node_inserted_l)

        node_inserted_eq = tree.add_node(10)
        self.assertFalse(node_inserted_eq)

    def test_public_remove_node(self):
        # Creating object
        tree = trees.tree_core.btree.Structure()

        # Removing in empty tree
        self.assertFalse(tree.remove_node(10))

        # Adding and removing
        tree.add_node(10)
        self.assertTrue(tree.remove_node(10))

        # Removing in none empty tree, element not in tree
        tree.add_node(10)
        tree.add_node(20)
        self.assertFalse(tree.remove_node(30))

        # Removing in none empty tree, element not in leaf
        tree.add_node(30)
        tree.add_node(50)
        self.assertTrue(tree.remove_node(10))

    def test_public_search_node(self):
        # Creating object
        tree = trees.tree_core.btree.Structure()
        tree.add_node(10)
        tree.add_node(20)
        tree.add_node(30)
        tree.add_node(5)

        # Existing node
        self.assertTrue(tree.search_node(10))
        self.assertTrue(tree.search_node(20))
        self.assertTrue(tree.search_node(30))
        self.assertTrue(tree.search_node(5))

        # None existing
        self.assertFalse(tree.search_node(1000))
        
if __name__ == '__main__':
    unittest.main()