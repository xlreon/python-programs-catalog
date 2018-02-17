"""Author - Sidharth Satapathy"""

# Problem 20
# Assuming that the tree has getData(), setData(), getLeft(), getRight()

# To print all the root to leaf paths

def pathsFinder(root):
    paths = []
    pathsAppend(root,[],paths)
    print ("paths : ",paths)

def pathsAppend(root,path,paths):
    if not root:
        return 0
    path.append(root.data)
    paths.append(path)
    pathsAppend(root.left,path+[root.data],paths)
    pathsAppend(root.right,path+[root+data],paths)    
