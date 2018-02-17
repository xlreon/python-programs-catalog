"""Author - Sidharth Satapathy"""

# Problem 15
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Find total numbe of full nodes

def totalFullNodes(root):
    if not root:
        return 0
    count = 0
    q = []
    q.append(root)
    node  = None
    while queue:
        node = q.pop()
        if node.left is not None and node.right is not None:
            count += 1
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return count                
