"""Author - Sidharth Satapathy"""

# Problem 12
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# To find the deepest in a binary tree

def deepest(root):
    if not root:
        return 0
    queue= []
    queue.append(root)
    node = None
    while queue:
        node = queue.pop()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)        
    return node.getData()