"""Author - Sidharth Satapathy"""

# Problem 14
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Calculate the total number of leaf nodes

def calculateLeafs(root):
    if not root:
        return 0
    count = 0
    queue = []
    queue.append(root)
    node = None
    while queue:
        node = queue.pop()
        if node.left is None and node.right is None:
            count += 1
        else:
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
    return count        