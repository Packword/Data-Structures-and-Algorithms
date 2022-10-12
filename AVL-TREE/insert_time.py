import matplotlib.pyplot as plt
import timeit
import math


print("Генерация дерева")
arr_1 = []
arr_2 = []
arr_3 = []

for i in range(2, 1000):
    my_setup = "import random\nfrom AVL_tree import AVLTree\nfrom AVL_tree import Node" \
               "\nTree = AVLTree()\nroot = None\ni = " + str(i) + "\nfor j in range(i - 1):\n   root = Tree.insert(root, j)"
    code_to_test = """
root = Tree.insert(root, i)
    """
    arr_1.append((timeit.timeit(setup=my_setup, stmt=code_to_test, number=1)))
for i in range(2, 1000):
    arr_2.append(1*math.log(i)/600000 + 0.0000185)
    arr_3.append(0.2*math.log(i)/600000 + 0.000005)
# Отрисовка
insert = plt.figure("Вставка")
insert = plt.subplot(111)
insert.plot(arr_1, color='r')
insert.plot(arr_2, color='b')
insert.plot(arr_3, color='g')
insert.axes.set_xlabel('Elements')
insert.axes.set_ylabel('time, s', color='b')
plt.show()
