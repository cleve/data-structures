from list_core import linked_list

def start():
    l_list = linked_list.LinkedList()
    while True:
        order = int(input("options:\n\n1) Add node\n2) Delete node\n3) Search node\n4) Print list\n5) Quit\n\nOption selected? "))
        if order == 1:
            node_value = int(input("Insert value: "))
            l_list.add_node(node_value)
        if order == 2:
            node_value = int(input("Insert value: "))
            l_list.remove_node(node_value)
        if order == 3:
            node_value = int(input("\nInsert value: "))
            print('Found' if l_list.find_node(node_value) is True else 'Not found')
        
        if order == 4:
            l_list.print_list()

        if order == 5:
            break

start()