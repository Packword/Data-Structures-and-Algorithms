from AVL_tree import AVLTree


Tree = AVLTree()
root = None
while True:
    try:
        print("Какой действие вы хотите совершить? Insert - вставить элемент, "
              "\nSearch - найти элемент, Exit - выйти из программы, Delete - удалить элемент.")
        data = input()
        if data == 'Exit':
            break
        if data == 'Search':
            root_found = int(input("Какой элемент найти?\n"))
            root_found = Tree.search(root, root_found)
            if root_found:
                print("Такой элемент есть в дереве\n")
            else:
                print("Элемент не найден\n")
        else:
            if data == 'Delete':
                root_remove = int(input("Какой элемент удалить?\n"))
                root = Tree.remove(root, root_remove)
            else:
                if data == 'Insert':
                    element = int(input("Какой элемент вставить? Element: "))
                    root = Tree.insert(root, element)
                else:
                    print(1/0)
    except (TypeError, ValueError, AttributeError, ZeroDivisionError):
        print("Smth went wrong, plz try again!")
        print("Probably, you typed not a number.")
        print()
