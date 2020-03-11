import unittest
import linked_list.list_core.linked_list

class TestBtreeMethods(unittest.TestCase):

    def test_add_element(self):
        list_object = linked_list.list_core.linked_list.LinkedList()
        elements = 7
        for element in range(elements):
            list_object.add_node(element)
        self.assertEqual(elements, list_object._count_elements())

    def test_add_equals_elements(self):
        list_object = linked_list.list_core.linked_list.LinkedList()
        self.assertEqual(0, list_object._count_elements())
        list_object.add_node(1)
        list_object.add_node(2)
        list_object.add_node(3)
        self.assertEqual(3, list_object._count_elements())
        list_object.add_node(3)
        list_object.add_node(3)
        list_object.add_node(3)
        self.assertEqual(6, list_object._count_elements())

    def test_remove_elements(self):
        list_object = linked_list.list_core.linked_list.LinkedList()
        list_object.add_node(1)
        list_object.add_node(2)
        list_object.add_node(3)
        list_object.add_node(3)
        list_object.add_node(3)
        list_object.remove_node(3)
        self.assertEqual(4, list_object._count_elements())

if __name__ == '__main__':
    unittest.main()