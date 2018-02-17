"""Author - Sidharth Satapathy"""

# Problem 19
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Find level max sum

def findMaxLevelSum(root):
    if not root:
        return 0
    q = []
    q.append(root)
    q.append(None)
    node = None
    level = currentSum = maxLevel = maxSum = 0
    while q:
        node = q.pop(0)
        if(node == None):
            if currentSum > maxSum:
                maxSum = currentSum
                maxLevel = level
            currentSum = 0
            if q:
                q.append(None)
                level += 1      
        else:
            currentSum += node.getData()
            if node.left is not None:
                q.append(node.left)
            if node.right is not None:
                q.append(node.right)
    return maxLevel            