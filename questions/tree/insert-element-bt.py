"""Author - Sidharth Satapathy"""

# Problem 5
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Inserting a node in a Binary Tree

class BinaryTree:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
    def setData(self,data):
        self.data = data
    def getData(self):
        return self.data
    def getLeft(self) :
        return self.left 
    def getRight(self):
        return self.right
    def insertLeft(self,data):
        if self.left == None:
            self.left = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.left = self.left
            self.left = temp
    def insertRight(self,data):
        if self.right == None:
            self.right = BinaryTree(data)
        else:
            temp = BinaryTree(data)
            temp.right = self.right
            self.right = temp
    def insertByLevelOrderTraversal(self,data):
        newNode = BinaryTree(data)
        if not root:
            root = newNode
            return root
        queue = []
        queue.append(root)
        node = None
        while queue:
            node = queue.pop()
            if data == node.getData():
                return root
            if node.left is not None:
                queue.append(node.left)
            else:
                node.left = newNode
                return root
            if node.right is not None:
                queue.append(node.right)
            else:
                node.right = newNode
                return root            