"""Author - Sidharth Satapathy"""

# Problem 23
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# given a sum we have to find that a path exists resulting to that sum

def pathFinder(root,val,path,paths):
    if not root:
        return False
    if not root.left and not root.right:
        if root.data == val:
            path.append(root.data)
            paths.append(path)
            return True
        else:
            return False    
    left = pathFinder(root.left,val-root.data,path+[root.data],paths)
    right = pathFinder(root.right,val-root.data,path+[root.data],paths)
    return left or right
def hasPathWithSum(root,val):
    paths = []
    pathFinder(root,val,[],paths)
    print ("Path sum to find : ",val)
    print ("Paths : ",paths)    