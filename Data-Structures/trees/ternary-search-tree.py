""" Author - Sidharth Satapathy """
""" This is python 3 code """

class Node(object):
    def __init__(self,character):
        self.character = character
        self.leftNode = None
        self.rightNode = None
        self.middleNode = None
        self.value = 0

class TST(object):
    def __init__(self):
        self.root = None
    def put(self,key,value):
        self.root = self.putItem(self.root, key, value, 0)
    def putItem(self,node,key,value,index):
        c = key[index]

        if node == None:
            node = Node(c)
        
        if c < node.character:
            node.leftNode = self.putItem(node.leftNode,key,value,index) 
        elif c > node.character:
            node.rightNode = self.putItem(node.rightNode,key,value,index)
        elif index < len(key)-1:
            node.middleNode = self.putItem(node.middleNode,key,value,index+1)
        else:
            node.value = value
        return node    
    def get(self,key):
        node = self.getItem(self.root, key, 0)
        if node == None:
            return -1
        else:
            return node.value
    def getItem(self,node,key,index):
        
        if node == None:
            return None
        c = key[index]
        if c < node.character:
            return self.getItem(node.leftNode,key,index)
        elif c > node.character:
            return self.getItem(node.rightNode,key,index)
        elif index < len(key)-1:
            return self.getItem(node.middleNode,key,index+1)
        else:
            return node
        return node
if __name__ == "__main__":
    tst = TST()
    choice = 1
    key = ""
    value = None
    while choice == 1:
        element = input("Enter key and value in format \"name\",value : ")
        element = element.split(",")
        tst.put(element[0],int(element[1]))
        choice = int(input("Want to enter another element ? (1 - yes, 2 - no) :"))
        
    getValKey = input("Enter the key you want to get value of : ")
    print (f"The value for key {getValKey} is {tst.get(getValKey)}")



