from tree_core import btree

def start():
    # Instantiation of tree object.
    binary_tree = btree.Structure()
    while True:
        order = int(input("options:\n1) Add node\n2) Delete node\n3) Search node\n4) Height \n5) Print Tree\n6) Quit\n\nOption selected? "))
        if order == 1:
            node_value = int(input("Insert value: "))
            binary_tree.add_node(node_value)
        if order == 2:
            node_value = int(input("Insert value: "))
            binary_tree.remove_node(node_value)
        if order == 3:
            node_value = int(input("\nInsert value: "))
            print('Found' if binary_tree.search_node(node_value) is not None else 'Not found')
        
        if order == 4:
            print('Height: ', binary_tree.node_height(binary_tree.root), '\n' )
        
        if order == 5:
            binary_tree.print_pre_order(binary_tree.root)

        if order == 6:
            break

start()