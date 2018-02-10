""" Author - Sidharth Satapathy """
""" This code is in python 3 """

import sys
from collections import defaultdict

class Node(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.minDistance = sys.maxsize
class Edge(object):
    def __init__(self,weight,start,end):
        self.weight = weight
        self.startNode = start
        self.endNode = end 
class BellmanFord(object):
    HAS_CYCLE = False
    def calculateShortestPath(self,vertexList,edgeList,startVertex):
        startVertex.minDistance = 0
        for i in range(0,len(vertexList)-1):
            for edge in edgeList:
                u = edge.startNode
                v = edge.endNode

                newDistance = u.minDistance+edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u

        for edge in edgeList:
            if self.hasCycle(edge):
                print ("Negative cycle detected.")
                BellmanFord.HAS_CYCLE = True
                return 
    def hasCycle(self,edge):
        if (edge.startNode.minDistance + edge.weight) < edge.endNode.minDistance :
            return True
        else:
            return False    
    def getShortestPath(self, startVertex):
        if BellmanFord.HAS_CYCLE:
            print ("The graph contains a negative edge.")
            node = startVertex
            while node is not None:
                print (f"The shortest path to {node.name} is ",node.minDistance)
                node = node.predecessor    

nodes = input("Enter the nodes separated by spaces : ")
nodes = nodes.split(" ")
allNodes = defaultdict()
vertexList = []
edgeList = []
for x in nodes :
    allNodes[x] = Node(x)

choice = 1
while choice == 1:
    edges = input("Enter the weight start vertex and end vertex separated by space : ")
    edges = [allNodes[x] if x in allNodes.keys() else float(x) for x in edges.split(" ")]
    edges[1].neighbours.append(Edge(edges[0],edges[1],edges[2]))
    edgeList.append(Edge(edges[0],edges[1],edges[2]))
    choice = int(input("Want to add another edge ? (1 - yes, 2 - no) : "))

startVert = input("Enter the node to calculate the shortest path from : ")
startVert = startVert.strip()
g = BellmanFord()
for x in allNodes.values():
    vertexList.append(x)
g.calculateShortestPath(vertexList,edgeList,allNodes[startVert])

if not BellmanFord.HAS_CYCLE:
    endVert = input("Enter the node to calculate the shortest path to : ")
    g.getShortestPath(allNodes[endVert])
