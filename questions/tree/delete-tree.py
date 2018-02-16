"""Author - Sidharth Satapathy"""

# Problem 9
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Deleting a tree

def deleteTree(root):
    if root is None:
        return
    deleteTree(root.left)
    deleteTree(root.right)
    del root