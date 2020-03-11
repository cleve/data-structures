from list_core import linked_list

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
    l_list = linked_list.LinkedList()
    while True:
        order = input_to_numeric("options:\n\n1) Add node\n2) Delete node\n3) Search node\n4) Print list\n5) Count nodes\n6) Quit\n\nOption selected? ")
        if order == 1:
            node_value = input_to_numeric("Insert value: ")
            l_list.add_node(node_value)
        if order == 2:
            node_value = input_to_numeric("Delete value: ")
            l_list.remove_node(node_value)
        if order == 3:
            node_value = input_to_numeric("\nSearch value: ")
            print('Found' if l_list.find_node(node_value) is True else 'Not found')
        
        if order == 4:
            l_list.print_list()

        if order == 5:
            l_list.count()

        if order == 6:
            break

start()