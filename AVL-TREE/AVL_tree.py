class Node(object):
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.h = 1

    def __str__(self):
        left = self.left.value if self.left else None
        right = self.right.value if self.right else None
        return 'key: {}, left: {}, right: {}'.format(self.value, left, right)


class AVLTree(object):

    def insert(self, root, key):
        if not root:
            return Node(key)
        elif key < root.value:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        root.h = 1 + max(self.getHeight(root.left),
                         self.getHeight(root.right))

        b = self.getBal(root)

        if b > 1 and key < root.left.value:
            return self.rRotate(root)

        if b < -1 and key > root.right.value:
            return self.lRotate(root)

        if b > 1 and key > root.left.value:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)

        if b < -1 and key < root.right.value:
            root.right = self.rRotate(root.right)
            return self.lRotate(root)

        return root

    def lRotate(self, z):
        y = z.right
        T2 = y.left
        y.left = z
        z.right = T2
        z.h = 1 + max(self.getHeight(z.left),
                      self.getHeight(z.right))
        y.h = 1 + max(self.getHeight(y.left),
                      self.getHeight(y.right))
        return y

    def rRotate(self, z):
        y = z.left
        T3 = y.right
        y.right = z
        z.left = T3
        z.h = 1 + max(self.getHeight(z.left),
                      self.getHeight(z.right))
        y.h = 1 + max(self.getHeight(y.left),
                      self.getHeight(y.right))
        return y

    def getHeight(self, root):
        if not root:
            return 0
        return root.h

    def getBal(self, root):
        if not root:
            return 0
        return self.getHeight(root.left) - self.getHeight(root.right)

    def preOrder(self, root):
        if not root:
            return
        print("{0} ".format(root.value), end="")
        self.preOrder(root.left)
        self.preOrder(root.right)

    def search(self, root, value):
        if root is None:
            return False
        if root.value == value:
            return True
        elif value < root.value:
            root = root.left if root.left is not None else None
            result = self.search(root, value)
        else:
            root = root.right if root.right is not None else None
            result = self.search(root, value)
        return result

    def inpre(self, root):
        while root.right is not None:
            root = root.right
        return root

    def insuc(self, root):
        while root.left is not None:
            root = root.left
        return root

    def remove(self, root, value):
        if root.left is None and root.right is None:
            root = None
            return None
        if root.value < value:
            root.right = self.remove(root.right, value)
        elif root.value > value:
            root.left = self.remove(root.left, value)
        else:
            if root.left is not None:
                q = self.inpre(root.left)
                root.value = q.value
                root.left = self.remove(root.left, q.value)
            else:
                q = self.insuc(root.right)
                root.value = q.value
                root.right = self.remove(root.right, q.value)
        if root is None:
            return root
            # update the height of the tree
        root.height = 1 + max(self.getHeight(root.left),
                              self.getHeight(root.right))

        balance = self.getBal(root)
        # Left Left
        if balance > 1 and self.getBal(root.left) >= 0:
            return self.rRotate(root)
        # Right Right
        if balance < -1 and self.getBal(root.right) <= 0:
            return self.lRotate(root)
        # Left Right
        if balance > 1 and self.getBal(root.left) < 0:
            root.left = self.lRotate(root.left)
            return self.rRotate(root)
        # Right Left
        if balance < -1 and self.getBal(root.right) < 0:
            root.right = self.rRotate(root.right)
            return self.lRotate(root)

        return root
