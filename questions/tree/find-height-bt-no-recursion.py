"""Author - Sidharth Satapathy"""

# Problem 11
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

def findHeight(root):
    if not root:
        return 
    queue = []
    queue.append([root,1])
    node = None
    temp = 0
    while queue:
        node, depth = queue.pop()
        temp = max(temp,depth)
        if node.left is not None:
            queue.append([node.left,depth+1])
        if node.right is not None:
            queue.append([node.right,depth+1])
    return temp