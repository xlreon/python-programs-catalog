"""Author - Sidharth Satapathy"""

# Problem 31
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Recursive solution to print all the ancestors of a given node in binary tree

def printAncestors(root,node):
    if not root:
        return 0
    if root.left == node or root.right == node or printAncestors(root.left,node) or printAncestors(root.right,node):
        print (root.data)
        return 1
    return 0    