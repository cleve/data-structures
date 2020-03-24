import unittest
import hash.hash_core.hash_table

class TestHashMethods(unittest.TestCase):

    def test_add_element(self):
        hash_object = hash.hash_core.hash_table.HashTable()
        elements = 7
        for element in range(elements):
            hash_object.add_element(element)
        self.assertEqual(elements, hash_object._count_elements())

    def test_hash_function(self):
        hash_object = hash.hash_core.hash_table.HashTable()
        # Len function""
        hash_object.hash_selection = 1
        string_1 = 'hello'
        string_2 = 'hello_world'
        string_3 = '#$%'
        self.assertEqual(hash_object.hash_function(string_1), 5)
        self.assertEqual(hash_object.hash_function(string_2), 11)
        self.assertEqual(hash_object.hash_function(string_3), 3)

        # ASCII function
        hash_object.hash_selection = 2
        self.assertEqual(hash_object.hash_function(string_1), '104101108108111')
        self.assertEqual(hash_object.hash_function(string_2), '10410110810811195119111114108100')
        
if __name__ == '__main__':
    unittest.main()