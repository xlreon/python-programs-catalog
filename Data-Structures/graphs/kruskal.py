""" Author - Sidharth Satapathy """
""" This code is in python 3 """

class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.node = None

class Node(object):
    def __init__(self,height,nodeId,parentNode):
        self.height = height
        self.nodeId = nodeId
        self.parentNode = parentNode

class Edge(object):
    def __init__(self,weight,start,end):
        self.weight = weight
        self.startVertex = start
        self.targetVertex = end
    def __cmp__(self,otherEdge):
        return self.cmp(self.weight, otherEdge.weight)
    def __lt__(self,otherEdge):
        selfPriority = self.weight
        otherPriority = otherEdge.weight
        return selfPriority < otherPriority
class DisjointSet(object):
    def __init__(self,vertexList):
        self.vertexList = vertexList
        self.rootNodes = []
        self.nodeCount = 0
        self.setCount = 0
        self.makeSets(vertexList)
    def find(self,node):
        currentNode = node
        while currentNode.parentNode is not None:
            currentNode = currentNode.parentNode
        root = currentNode
        currentNode = node
        while currentNode is not root:
            temp = currentNode.parentNode
            currentNode.parentNode = root
            currentNode = temp
        return root.nodeId
    def merge(self,node1,node2):
        index1 = self.find(node1)
        index2 = self.find(node2)

        if index1 == index2:
            return # They are in the same set
        root1 = self.rootNodes[index1]
        root2 = self.rootNodes[index2]

        if root1.height < root2.height:
            root1.parentNode = root2
        elif root1.height > root2.height:
            root2.parentNode = root1
        else:
            root1.parentNode = root2
            root2.height = root2.height+1
    def makeSets(self, vertexList):
        for v in vertexList:
            node = Node(0,len(self.rootNodes),None)
            v.node = node
            self.rootNodes.append(node)
            self.setCount = self.setCount + 1
            self.nodeCount = self.nodeCount + 1

class Kruskal(object):
    def spanningTree(self,vertexList,edgeList):
        spanning = []
        disjoint = DisjointSet(vertexList)
        edgeList.sort()

        for edge in edgeList:
            u = edge.startVertex
            v = edge.targetVertex

            if disjoint.find(u.node) is not disjoint.find(v.node):
                spanning.append(edge)
                disjoint.merge(u.node,v.node)
        for edge in spanning:
            print (edge.startVertex.name," -> ",edge.targetVertex.name)                

vertex1 = Vertex("a") 
vertex2 = Vertex("b") 
vertex3 = Vertex("c") 
vertex4 = Vertex("d") 
vertex5 = Vertex("e") 
vertex6 = Vertex("f") 

edge1 = Edge(2,vertex1,vertex2) 
edge2 = Edge(4,vertex1,vertex4) 
edge3 = Edge(4,vertex2,vertex3) 
edge4 = Edge(4,vertex2,vertex4) 
edge5 = Edge(3,vertex2,vertex5) 
edge6 = Edge(1,vertex2,vertex6) 
edge7 = Edge(5,vertex3,vertex6) 
edge8 = Edge(2,vertex4,vertex5) 
edge9 = Edge(5,vertex5,vertex6) 

vertexList = [] 
vertexList.append(vertex1) 
vertexList.append(vertex2) 
vertexList.append(vertex3) 
vertexList.append(vertex4) 
vertexList.append(vertex5) 
vertexList.append(vertex6) 

edgeList = [] 
edgeList.append(edge1) 
edgeList.append(edge2) 
edgeList.append(edge3) 
edgeList.append(edge4) 
edgeList.append(edge5) 
edgeList.append(edge6) 
edgeList.append(edge7) 
edgeList.append(edge8) 
edgeList.append(edge9) 

algorithm = Kruskal() 
algorithm.spanningTree(vertexList, edgeList) 
