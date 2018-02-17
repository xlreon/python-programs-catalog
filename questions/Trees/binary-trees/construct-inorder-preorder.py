"""Author - Sidharth Satapathy"""

# Problem 29
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# Constructing a Binary tree from inorder and preorder

class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None
class Solution:
    def build(self,preorder,inorder):
        if not inorder or not preorder:
            return None
        else:
            root = Node(preorder[0])
            position = inorder.index(preorder[0])
            root.left = self.build(preorder[1:1+position],inorder[:position])
            root..right = self.build(preorder[position+1:],inorder[position+1:])
        return root            
