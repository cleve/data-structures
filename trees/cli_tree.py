from tree_core import btree

def start():
    order = int(input("\nSelect Tree type:\n\n1) Binary tree\n2) AVL Tree\n3) Quit\n\nOption selected? "))
    # Instantiation of tree object.
    if order == 1:
        print('BINARY TREE\n')
        tree = btree.Structure()
    elif order == 2:
        print('Not implemented yet')
        return
    else:
        return
    while True:
        order = int(input("options:\n\n1) Add node\n2) Delete node\n3) Search node\n4) Height \n5) Print Tree\n6) Quit\n\nOption selected? "))
        if order == 1:
            node_value = int(input("Insert value: "))
            tree.add_node(node_value)
        if order == 2:
            node_value = int(input("Insert value: "))
            tree.remove_node(node_value)
        if order == 3:
            node_value = int(input("\nInsert value: "))
            print('Found' if tree.search_node(node_value) is not None else 'Not found')
        
        if order == 4:
            print('Height: ', tree.node_height(tree.root), '\n' )
        
        if order == 5:
            tree.print_pre_order(tree.root)

        if order == 6:
            break

start()