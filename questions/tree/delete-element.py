"""Author - Sidharth Satapathy"""

# Problem 13
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# delete an element in a binary tree

def deleteNode(root,data):
    if not root:
        return 0
    temp = None
    toDelete = None
    queue = []
    queue.append(root)
    node = None
    while queue:
        node = queue.pop()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        if node.data == data:
            toDelete = node
    if toDelete is not None:
        temp = toDelete.data
        toDelete.data = node.data
        node.data = temp
        del node
    else:
        print ("Node to delete was not found.")    
