"""Author - Sidharth Satapathy"""

# Problem 6
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# find the size of the binary tree with recursion

def findSize(root):
    if not root:
        return 0
    return findSize(root.left) + findSize(root.right) + 1    

