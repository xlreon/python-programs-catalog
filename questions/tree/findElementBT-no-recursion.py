"""Author - Sidharth Satapathy"""

# Problem 4
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Find an element without recursion

def find(self,root,data):
    if not root:
        return -1
    queue = []
    queue.append(root)
    node = None
    while queue:
        node = queue.pop()
        if data == node.getData():
            return 1
        if node.left is not None:
            queue.append(root.left)
        if node.right is not None:
            queue.append(root.right)
    return 0                
