"""Author - Sidharth Satapathy"""

# Problem 21
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Find the root to leaf sum of path represented as numbers

def sumNumbers(root):
    if not root:
        return 0
    current = 0
    sum = [0]
    self.calSum(root,current,sum)
    return sum[0]
def calSum(root,current,sum):
    if not root:
        return 
    current = current*10 + root.getData()
    if not root.left and not root.right:
        sum[0] += current
        return
    self.calSum(root.left,current,sum)
    self.calSum(root.right,current,sum)    