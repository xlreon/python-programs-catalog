"""Author - Sidharth Satapathy"""

# Problem 1
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# without using recursion

def findMax(root):
    if not root:
        return
    queue = []
    queue.append(root)
    node = None
    maxELement = 0
    while queue:
        node = q.pop()
        if maxELement < node.getData:
            maxELement = node.getData()
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    print ("The max element is : ",maxELement)                