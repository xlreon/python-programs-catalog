"""Author - Sidharth Satapathy"""

# Problem 7
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# find size of binary tree without recursion

def findSize(root):
    count = 0
    if not root:
        return 0
    queue = []
    queue.append(root)
    node = None
    while queue:
        node = queue.pop()
        count = count + 1
        if node.left is not None:
            queue.append(node.left)
        if node.right is not None:
            queu.append(node.right)
    return count            