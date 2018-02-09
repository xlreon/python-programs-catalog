""" Author - Sidharth Satapathy """
""" This code is in python 3 """
import sys
import heapq
from collections import defaultdict
class Edge(object):
    def __init__(self,weight,start,end):
        self.weight = weight
        self.startNode = start
        self.endNode = end

class Vertex(object):
    def __init__(self,name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbours = []
        self.minDistance = sys.maxsize
    def __cmp__(self,otherVertex):
        return self.cmp(self.minDistance, otherVertex.minDistance)
    
    def __lt__(self,otherVertex):
        selfPriority = self.minDistance 
        otherPriority = self.minDistance
        return selfPriority < otherPriority
class Graph(object):
    def calculateShortestPath(self,startVertex):
        q = []
        startVertex.minDistance = 0
        heapq.heappush(q,startVertex)

        while len(q) > 0:
            actualVertex = heapq.heappop(q)
            for edge in actualVertex.neighbours:
                u = edge.startNode
                v = edge.endNode
                newDistance = u.minDistance + edge.weight
                if newDistance < v.minDistance:
                    v.minDistance = newDistance
                    v.predecessor = u
                    heapq.heappush(q, v)
    def getShortestPath(self,targetVertex):
        print (f"The shortest path to vertex targetVertex {targetVertex.name} is ",targetVertex.minDistance)
        node = targetVertex
        while node is not None:
            print (" -> ",node.name)
            node = node.predecessor

nodes = input("Enter the nodes separated by spaces : ")
nodes = nodes.split(" ")
allNodes = defaultdict()
for x in nodes :
    allNodes[x] = Vertex(x)

choice = 1
while choice == 1:
    edges = input("Enter the weight start vertex and end vertex separated by space : ")
    edges = [allNodes[x] if x in allNodes.keys() else float(x) for x in edges.split(" ")]
    edges[1].neighbours.append(Edge(edges[0],edges[1],edges[2]))
    choice = int(input("Want to add another edge ? (1 - yes, 2 - no) : "))

startVert = input("Enter the node to calculate the shortest path from : ")
startVert = startVert.strip()
g = Graph()
g.calculateShortestPath(allNodes[startVert])
endVert = input("Enter the node to calculate the shortest path to : ")
g.getShortestPath(allNodes[endVert])
