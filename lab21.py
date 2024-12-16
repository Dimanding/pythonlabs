class Node:
    """
    Клас для вузла AVL-дерева
    """
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    """
    Клас для реалізації самобалансуючого AVL-дерева
    """
    # Отримання висоти вузла
    def get_height(self, node):
        if not node:
            return 0
        return node.height

    # Отримання балансу вузла
    def get_balance(self, node):
        if not node:
            return 0
        return self.get_height(node.left) - self.get_height(node.right)

    # Поворот вправо
    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Поворот вліво
    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    # Вставка нового елемента у дерево
    def insert(self, root, key):
        # Крок 1: Звичайна вставка у BST
        if not root:
            return Node(key)
        elif key < root.key:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)

        # Крок 2: Оновлення висоти батьківського вузла
        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        # Крок 3: Отримання балансу вузла для перевірки балансу
        balance = self.get_balance(root)

        # Балансування дерева
        # Лівий Лівий випадок
        if balance > 1 and key < root.left.key:
            return self.right_rotate(root)

        # Правий Правий випадок
        if balance < -1 and key > root.right.key:
            return self.left_rotate(root)

        # Лівий Правий випадок
        if balance > 1 and key > root.left.key:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        # Правий Лівий випадок
        if balance < -1 and key < root.right.key:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    # Обхід дерева: зліва -> корінь -> справа
    def inorder_traversal(self, root):
        if root:
            self.inorder_traversal(root.left)
            print(f"{root.key} ", end="")
            self.inorder_traversal(root.right)

# Приклад використання AVL-дерева
if __name__ == "__main__":
    tree = AVLTree()
    root = None

    keys = [10, 20, 30, 40, 50, 25]  # Тестові значення для вставки

    for key in keys:
        root = tree.insert(root, key)

    print("Обхід AVL-дерева у порядку зліва-корінь-справа:")
    tree.inorder_traversal(root)
    print()
