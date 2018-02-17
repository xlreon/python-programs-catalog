"""Author - Sidharth Satapathy"""

# Problem 26
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Mirror a binary tree

def mirrorTree(root):
    if not root:
        return
    else:
        mirrorTree(root.left)
        mirrorTree(root.right)
        temp = root.left
        root.left = root.right
        root.right = temp
    return root        