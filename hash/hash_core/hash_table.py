# Bring packages to the current workspace
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'ds', 'linked_list')))

from list_core import linked_list

class HashTable:
    def __init__(self):
        # Using a dictionary to mapping
        self.hash_table = {}

        # Public hash function descriptions
        self.hash_doc = """Select the hash function to use:
        1. string to hascii code concatenated
        2. simple lenght of string\n
        """
        self.hash_selection = 1

    def hash_function(self, value):
        # Document in the variable self.hash_doc
        def str_to_ascii(value):
            return ''.join(str(ord(c)) for c in value)

        def get_len(value):
            return len(str(value))

        if self.hash_selection == 1:
            return get_len(value)

        if self.hash_selection == 2:
            return str_to_ascii(value)

    def check_colision(self, hash_of_value):
        if hash_of_value in self.hash_table:
            return True
        return False
    
    def linked_list_generator(self, value, hash_of_value):
        current_value = self.hash_table[hash_of_value]
        if isinstance(current_value, linked_list.LinkedList):
            # append value since the list was already created
            current_value.add_node(value)
            return current_value
        
        new_linked_list = linked_list.LinkedList()
        new_linked_list.add_node(current_value)
        new_linked_list.add_node(value)
        return new_linked_list

    def add_element(self, value):
        hash_of_value = self.hash_function(value)
        # check colision
        if not self.check_colision(hash_of_value):
           self.hash_table[hash_of_value] = value
        # Collision detected, adding a linked list
        else:
            self.hash_table[hash_of_value] = self.linked_list_generator(value, hash_of_value)

    def remove_element(self):
        pass

    def _count_elements(self):
        total_elements = 0
        for key in self.hash_table:
            if isinstance(self.hash_table[key], linked_list.LinkedList):
                total_elements += self.hash_table[key]._count_elements()
            else:
                total_elements += 1
        return total_elements

    def count_elements(self):
        pass

    def print_hash(self):
        for key in self.hash_table:
            if isinstance(self.hash_table[key], linked_list.LinkedList):
                self.hash_table[key].print_list()
            else:
                print('Value: ', self.hash_table[key])

    def find_element(self):
        pass
        
        
        

        