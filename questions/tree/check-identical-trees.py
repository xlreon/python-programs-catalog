"""Author - Sidharth Satapathy"""

# Problem 17
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# check if 2 trees are identical

def isIdentical(root1,root2):
    if (not root1.left) and (not root1.right) and (not root2.left) and (not root2.right) and root1.data == root2.data:
        return True
    if (root1.data != root2.data) or (root1.left and not root2.left) or (not root1.left and root2.left) or (not root1.right and not root2.right) or (root1.right and not root2.right):
        return False
    left = isIdentical(root1.left,root2.left) if root1.left and root2.left else True
    right = isIdentical(root1.right,root2.right) if root1.right and root2.right else True
    return left and right   
