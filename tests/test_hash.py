import unittest
import hash.hash_core.hash_table

class TestHashMethods(unittest.TestCase):

    def test_add_element(self):
        hash_object = hash.hash_core.hash_table.HashTable()
        elements = 7
        for element in range(elements):
            hash_object.add_element(element)
        self.assertEqual(elements, hash_object._count_elements())

    

if __name__ == '__main__':
    unittest.main()