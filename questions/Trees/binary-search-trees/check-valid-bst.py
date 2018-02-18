""" Author - Sidharth Satapathy """

# Problem 54

# check if the given tree is a valid binary search tree or not

def findMax(root):
    max_data = 0
    if not root:
        return
    while root:    
        if max_data < root.getData():
            max_data = root.getData()
        else:
            root = root.right
    return max_data
def findMin(root):
    min_data = 99999
    if not root:                
        return
    while root:
        if min_data > root.getData():
            min_data = root.getData()
        else:
            root = root.left
    return min_data                

def checkValid(root):
    if not root:
        return 1
    if root.left != None and  findMax(root.left) > root.getData():
        return 0
    if root.right != None and findMin(root.right) < root.getData():
        return 0
    if not checkValid(root.left) or not checkValid(root.right):
        return 0
    return 1    