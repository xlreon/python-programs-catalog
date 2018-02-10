""" Author - Sidharth Satapathy """
""" This code is in python 3 """

import heapq
class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []

    def __str__(self):
        return self.name

class Edge(object):
    def __init__(self,weight,start,end):
        self.weight = weight
        self.startVertex = start
        self.targetVertex = end

    def __cmp__(self,other):
        return self.cmp(self.weight,other.weight)    
    def __lt__(self,other):
        selfPriority = self.weight
        otherPriority = other.weight
        return selfPriority < otherPriority    

class Prim(object):
    def __init__(self,unvisitedList):
        self.unvisitedList = unvisitedList
        self.spanningTree = []
        self.edgeHeap = []
        self.cost = 0
    def calculateSpanningTree(self,vertex):
        self.unvisitedList.remove(vertex)
        while self.unvisitedList:
            for edge in vertex.neighbours:
                if edge.targetVertex in self.unvisitedList:
                    heapq.heappush(self.edgeHeap,edge)
            minEdge = heapq.heappop(self.edgeHeap)
            self.spanningTree.append(minEdge)
            print (f"Edge added to spanning tree {minEdge.startVertex} -> {minEdge.targetVertex}")
            self.cost = self.cost + minEdge.weight
            vertex = minEdge.targetVertex
            self.unvisitedList.remove(vertex)
    def getSpanningTree(self):
        return self.spanningTree 

node1 = Vertex("1")  
node2 = Vertex("2")  
node3 = Vertex("3")  
node4 = Vertex("4")  

edge1 = Edge(1,node1,node2)  
edge2 = Edge(1,node1,node3)  
edge3 = Edge(0.01,node1,node4)  
edge4 = Edge(1,node3,node4)  

node1.  neighbours.append(edge1)  
node1.  neighbours.append(edge2)  
node1.  neighbours.append(edge3)  
node3.  neighbours.append(edge4)  

unvisitedList = []  
unvisitedList.append(node1)  
unvisitedList.append(node2)  
unvisitedList.append(node3)  
unvisitedList.append(node4)  

algorithm = Prim(unvisitedList)  
algorithm.calculateSpanningTree(node1)          