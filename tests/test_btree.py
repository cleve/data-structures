import unittest
import trees.tree_core.btree

class TestBtreeMethods(unittest.TestCase):

    def test_public_add_node(self):
        tree = trees.tree_core.btree.Structure()

        node_inserted = tree.add_node(20)
        self.assertTrue(node_inserted)

        node_inserted_r = tree.add_node(30)
        self.assertTrue(node_inserted_r)

        node_inserted_l = tree.add_node(10)
        self.assertTrue(node_inserted_l)

        node_inserted_eq = tree.add_node(10)
        self.assertTrue(node_inserted_eq)

if __name__ == '__main__':
    unittest.main()