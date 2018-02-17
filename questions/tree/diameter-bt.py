"""Author - Sidharth Satapathy"""

# Problem 18
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# To find the diameter of a binary tree


def height(root):
    if not root:
        return 0
    return max(height(root.left),height(root.right))+1    


def diameter(root):
    if not root:
        return 0
    lHeight = height(root.left)
    rHeight = height(root.right)
    lDiameter = diameter(root.left)
    rDiameter = diameter(root.right)
    return max(lHeight+rHeight+1,max(lDiameter, rDiameter))
    

