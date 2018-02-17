"""Author - Sidharth Satapathy"""

# Problem 16
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Find the total number of half nodes

def totalHalfNodes(root):
    if not root:
        return 0
    q = []
    node = None
    count = 0
    while q:
        node = q.pop()
        if node.left is not None and node.right is None:
            count += 1
        if node.right is not None and node.left is None:
            count += 1
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return count                    