""" Author - Sidharth Satapathy """
""" This code is in python 2 """

class Node(object):
    def __init__(self,name):
        self.name = name
        self.neighbours = []
        self.visited = False
        self.predecessor = None
class Graph(object):
    def __init__(self):
        self.vertices = []
    def bfs(self, startNode):
        queue = []
        queue.append(startNode)
        startNode.visited = True

        while queue:
            curr = queue.pop(0)
            print ("Node : ",curr.name)

            for vertex in curr.neighbours:
                if not vertex.visited:
                    vertex.visited = True
                    queue.append(vertex)  
    def getNode(self,name):
        for x in self.vertices:
            if x.name == name:
                return x    
    def insertNode(self,name):
        node = Node(name)
        self.vertices.append(node)                           
    def insertNodeNeighbour(self,node):
        adjacentNodes = input(f"Enter the adjacent nodes separated by space for node {node.name} : ")
        adjacentNodes = [self.getNode(x) for x in adjacentNodes.split(" ") if self.getNode(x) != None]
        node.neighbours = adjacentNodes

if __name__ == "__main__":
    g = Graph()
    name = input("Enter all nodes separate by space : ")
    name = [x for x in name.split(" ")]
    for x in name:
        g.insertNode(x)
    for i in g.vertices:
        g.insertNodeNeighbour(i)

    start = input("Enter the node to do BFS from : ")
    node = g.getNode(start)
    print (f"The BFS starting from node {node.name} is -> ")
    if node != -1:
        g.bfs(node)

