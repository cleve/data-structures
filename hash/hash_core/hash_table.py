# Bring packages to the current workspace.
import sys, os
sys.path.append(os.path.abspath(os.path.join('..', 'data-structures', 'linked-list')))

from list_core import linked_list  # noqa

class HashTable:
    def __init__(self):
        # Using a dictionary to mapping.
        self.hash_table = {}

    def hash_function(self, value):
        return len(value)

    def check_colision(self, value):
        if self.hash_function(value) in self.hash_table:
            return True
        return False
    
    def add_element(self, index, value):
        # check colision.
        if self.check_colision(value):
           return
        
        
        

        