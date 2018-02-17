"""Author - Sidharth Satapathy"""

# Problem 24
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# find the sum of all elements in a binary tree

def findSum(root):
    if not root:
        return 0
    return root.data + findSum(root.left) + findSum(root.right)    