class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    def insert(self, data):
        if self.value:
                if data > self.value:
                    if self.right is None:
                        self.right = TreeNode(data)
                    else:
                        self.right.insert(data)
                elif data < self.value:
                    if self.left is None:
                        self.left = TreeNode(data)
                    else:
                        self.left.insert(data)
        else:
            self.value = data
    
    def minValueNode(self, node):
        if node.left == None:
            return node
        return self.minValueNode(node.left)

    def find(self, value):
        if self.value is None:
            print("Дерево пусто")
            return
        elif self.value > value:
            if self.value is None:
                print ("Значение не найдено: " + str(value))
            return value
        elif self.value < value:
            if self.value is None:
                print ("Значение не найдено: " + str(value))
            return value
        else:
             print ("Значение найдено: " + str(value))

    def deleteNode(self, root, key):
        if root is None:
            return root
        
        if key < root.value:
            root.left = self.deleteNode(root.left, key)
        elif key> root.value:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp

            elif root.right is None:
                temp = root.left
                root = None
                return temp
            root.value= self.minValueNode(root.right).value
            root.right = self.deleteNode(root.right, root.value)
        return root

    def pre_order(self, node):
            if node:
                print(node.value)
                self.pre_order(node.left)
                self.pre_order(node.right)


tree = TreeNode(21)
tree.insert(28)
tree.insert(14)
tree.insert(32)
tree.insert(25)
tree.insert(18)
tree.insert(11)
tree.deleteNode(tree, 28)
tree.find(10)
tree.pre_order(tree)