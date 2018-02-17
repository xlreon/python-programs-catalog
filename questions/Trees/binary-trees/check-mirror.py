"""Author - Sidharth Satapathy"""

# Problem 27
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Given 2 binary trees check wether they are mirror of each other or not

def checkMirror(root1,root2):
    if not root1 and not root2:
        return True
    if not root1 or not root2:
        return False
    if root1.data != root2.data:
        return False
    else:
        return checkMirror(root1.left,root2.right) and checkMirror(root1.right,root2.left)   