import matplotlib.pyplot as plt
import timeit
import math
print("Генерация дерева")
arr_1 = []
arr_2 = []
arr_3 = []
for i in range(2, 100):
    my_setup = "import random\nfrom AVL_tree import AVLTree\nfrom AVL_tree import Node" \
               "\nTree = AVLTree()\nroot = None\ni = " + str(i) + "\nfor j in range(i - 1):\n   root = Tree.insert(root, j)\nran = random.randint(1,i)"
    code_to_test = """
root_n = Tree.search(root, root.value)
    """
    arr_1.append((timeit.timeit(setup=my_setup, stmt=code_to_test, number=1)))
for i in range(2, 100):
    arr_2.append(0.1*math.log(i)/600000 + 0.0000015)
    arr_3.append(0.08*math.log(i)/600000)
# Отрисовка
search = plt.figure("Поиск")
search = plt.subplot(111)
search.plot(arr_1, color='r')
search.plot(arr_2, color='b')
search.plot(arr_3, color='g')
search.axes.set_xlabel('Elements')
search.axes.set_ylabel('time, s', color='b')
plt.show()

