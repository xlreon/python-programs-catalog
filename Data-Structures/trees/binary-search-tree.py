""" Author - Sidharth Satapathy """
""" This is python 3 code """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

class BinarySearchTree(object):
    def __init__(self):
        self.root = None
    def insert(self,data):
        if not self.root:
            self.root = Node(data)
        else:
            self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if data <= node.data:
            if node.leftChild:
                self.insertNode(data,node.leftChild)
            else:
                node.leftChild = Node(data)
        else:
            if node.rightChild:
                self.insertNode(data,node.rightChild)
            else:
                node.rightChild = Node(data) 

    def delete(self,data):
        if self.root:
            self.root = self.deleteNode(data,self.root)
    def deleteNode(self,data,node):
        if not node:
            return node
        if data < node.data:
            node.leftChild = self.deleteNode(data,node.leftChild)
        elif data > node.data:
            node.rightChild = self.deleteNode(data,node.rightChild)
        else:
            if not node.leftChild and not node.rightChild:
                print ("Leaf node is being removed with value : ",node.data)
                del node
                return None
            if not node.leftChild:
                print ("Removing node with single right child with value : ",node.data)
                temp = node.rightChild
                del node
                return temp
            elif not node.rightChild:
                print ("Removing node with single left child with value : ",node.data)
                temp = node.leftChild
                del node
                return temp
            print ("Removing node with 2 childs with value : ",node.data)
            predecesor = self.getPredecesor(node.leftChild)
            node.data = predecesor.data
            node.leftChild = self.deleteNode(predecesor.data,node.leftChild)
        return node        

    def getPredecesor(self,node):
        if node.rightChild:
            return self.getPredecesor(node.rightChild)
        return node                        
    def getMinValue(self):
        if self.root:
            return self.getMin(self.root)
    def getMin(self,node):
        if self.leftChild:
            return getMin(self.leftChild)
        return node.data 
    def getMaxValue(self):
        if self.rightChild:
            return getMax(self.rightChild)
        return node.data
    def traverse(self):
        if self.root:
            self.inOrderTraverse(self.root)               
    def inOrderTraverse(self,node):
        if node.leftChild:
            self.inOrderTraverse(node.leftChild)
        print (node.data)
        if node.rightChild:
            self.inOrderTraverse(node.rightChild)
array = input("Enter the nodes of tree separated by space : ")
array = [int(x) for x in array.split(" ")]
bst = BinarySearchTree()
for i in array:
    bst.insert(i)
bst.traverse()
nodeToDel = int(input("Enter node to delete : "))
bst.delete(nodeToDel)
bst.traverse()