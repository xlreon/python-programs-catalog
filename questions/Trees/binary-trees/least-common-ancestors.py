"""Author - Sidharth Satapathy"""

# Problem 28
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Given 2 nodes we have to find the least common ancestors

def lca(root,alpha,beta):
    if not root:
        return None
    if root.data == alpha or root.data == beta:
        return root
    left = lca(root.left,alpha,beta)
    right = lca(root.right,alpha,beta)

    if left and right:
        return root
    else:
        return left if left else right    
