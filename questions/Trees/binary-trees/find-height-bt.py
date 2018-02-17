"""Author - Sidharth Satapathy"""

# Problem 10
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# find the height of a Binary Tree

def findHeight(root):
    if root is None:
        return 0
    return max(findHeight(root.left),findHeight(root.right))+1    
