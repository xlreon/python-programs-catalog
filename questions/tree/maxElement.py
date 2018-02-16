"""Author - Sidharth Satapathy"""

# Problem 1
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

maxData = float("-inifinity")

def findMax(root):
    global maxData
    if not root:
        return maxData
    if root.getData() > maxData:
        maxData = root.getData()
    findMax(root.getLeft()) 
    findMax(root.getRight())
    return maxData   

