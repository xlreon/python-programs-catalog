"""Author - Sidharth Satapathy"""

# Problem 25
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# find the sum of all the elements in binary tree without recursion

def findSum(root):
    if not root:
        return 0
    q = []
    q.append(root)
    node = None
    sum = 0
    while q:
        node = q.pop(0)
        sum += node.data
        if node.left is not None:
            q.append(node.left)
        if node.right is not None:
            q.append(node.right)
    return sum                