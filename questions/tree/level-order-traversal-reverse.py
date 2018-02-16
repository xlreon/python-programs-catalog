"""Author - Sidharth Satapathy"""

# Problem 8
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Level order traversal in reverse order

def traversalReverse(root):
    if not root:
        return 0
    queue = []
    result = []
    node = None
    queue.append(root)
    result.append(root)
    while queue:
        node = queue.pop()
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queue.append(node.right)
        result.append(node)    
    while result:
        print (result.pop().getData())               