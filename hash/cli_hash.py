from hash_core import hash_table

# Helpers
def is_numeric(order):
    if not order.isnumeric():
        print('A number is requested')
        return False
    return True

def input_to_numeric(msg):
    input_from_user = input(msg)
    if is_numeric(input_from_user):
        return int(input_from_user)
    return -1

def start():
    hash_object = hash_table.HashTable()
    hash_object.hash_selection = input_to_numeric(hash_object.hash_doc)
    if hash_object.hash_selection == -1:
            hash_object.hash_selection = 1
    while True:
        order = input_to_numeric("options:\n\n1) Add node\n2) Delete node\n3) Search node\n4) Print hash\n5) Quit\n\nOption selected? ")
        if order == 1:
            node_value = input_to_numeric("Insert value: ")
            hash_object.add_element(node_value)
        if order == 2:
            node_value = input_to_numeric("Delete value: ")
            hash_object.remove_element(node_value)
        if order == 3:
            node_value = input_to_numeric("\nSearch value: ")
            print('Found' if hash_object.find_element(node_value) is True else 'Not found')
        
        if order == 4:
            hash_object.print_hash()

        if order == 5:
            break

start()