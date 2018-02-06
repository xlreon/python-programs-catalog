""" Author - Sidharth Satapathy """
""" This is python 3 code """

class Node(object):
    def __init__(self,data):
        self.data = data
        self.height = 0
        self.leftChild = None
        self.rightChild = None

class AVL(object):
    def __init__(self):
        self.root = None
    def calculateHeight(self,node):
        if not node:
            return -1
        return node.height
    # If return value is > 1  -> left heavy tree -> right rotation
    # If return value is < -1 -> right heavy tree -> left rotation
    # In some cases we have to do 2 rotations right -> left or left -> right
    def checkBalance(self,node):
        if not node:
            return 0
        return self.calculateHeight(node.leftChild)-self.calculateHeight(node.rightChild) 
    def rotateRight(self,node):
        print ("Rotating right of node : ",node.data)

        tempLeftChild = node.leftChild
        t = tempLeftChild.rightChild
        tempLeftChild.rightChild = node
        node.leftChild = t

        node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        tempLeftChild.height = max(self.calculateHeight(tempLeftChild.leftChild),self.calculateHeight(tempLeftChild.rightChild))+1
        return tempLeftChild
    def rotateLeft(self,node):
        print ("Rotating left of node : ",node.data)

        tempRightChild = node.rightChild
        t = tempRightChild.leftChild
        tempRightChild.rightChild = node
        node.rightChild = t

        node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        tempRightChild.height = max(self.calculateHeight(tempRightChild.leftChild),self.calculateHeight(tempRightChild.rightChild))
        return tempRightChild
    def insert(self,data):
        self.root = self.insertNode(data,self.root)
    def insertNode(self,data,node):
        if not node:
            return Node(data)
        if data < node.data:
            node.leftChild = self.insertNode(data,node.leftChild)
        else:
            node.rightChild = self.insertNode(data,node.rightChild)
        node.height  = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        return self.settleViolation(data,node)       
    def settleViolation(self,data,node):
        balance = self.checkBalance(node)
        # case 1 left left heavy 
        if balance > 1 and data < node.leftChild.data:
            print ("left left heavy situtation.")
            return self.rotateRight(node)
        if balance < -1 and data > node.rightChild.data:
            print ("Right Right heavy situation.") 
            return self.rotateLeft(node)
        if balance > 1 and data > node.leftChild.data:
            print ("Left Right situation.")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        if balance < -1 and data < node.rightChild.data:
            print ("Right left situation.")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node) 
        return node
    def traverse(self):
        if self.root:
            self.inOrderTraverse(self.root)               
    def inOrderTraverse(self,node):
        if node.leftChild:
            self.inOrderTraverse(node.leftChild)
        print (node.data)
        if node.rightChild:
            self.inOrderTraverse(node.rightChild)
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

        if not node:
            return node
        node.height = max(self.calculateHeight(node.leftChild),self.calculateHeight(node.rightChild))+1
        balance = self.checkBalance(node)
        if balance > 1 and data < node.leftChild.data:
            print ("left left heavy situtation.")
            return self.rotateRight(node)
        if balance < -1 and data > node.rightChild.data:
            print ("Right Right heavy situation.") 
            return self.rotateLeft(node)
        if balance > 1 and data > node.leftChild.data:
            print ("Left Right situation.")
            node.leftChild = self.rotateLeft(node.leftChild)
            return self.rotateRight(node)
        if balance < -1 and data < node.rightChild.data:
            print ("Right left situation.")
            node.rightChild = self.rotateRight(node.rightChild)
            return self.rotateLeft(node) 
        return node        
avl = AVL()

array  = input("Enter the elements of the tree separated by space : ")
array = [int(x) for x in array.split(" ")]
for i in array:
    avl.insert(i) 
choice = int(input("Enter 1 to remove a node and 0 otherwise, Enter Choice : "))
while choice == 1:
    nodeToDelete = int(input("Enter node to delete : "))
    avl.delete(nodeToDelete)
    choice = int(input("Enter 1 to remove a node and 0 otherwise, Enter Choice : "))
avl.traverse()
