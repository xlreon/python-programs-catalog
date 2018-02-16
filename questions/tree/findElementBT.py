"""Author - Sidharth Satapathy"""

# Problem 3
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

def find(root,data):
    if not root:
        return 0
    if root.getData() == data:
        return 1
    else:
        temp = find(root.left,data)
        if temp == 1:
            return 1
        else:
            return find(root.right,data)    