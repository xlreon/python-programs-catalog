""" Author - Sidharth Satapathy """
""" This code is in python 3 """

class Node(object):
    def __init__(self,name):
        self.name = name
        self.neighbours = []
        self.visited = False
        self.predecessor = None
class Graph(object):
    def __init__(self):
            self.vertices = []
    def dfs(self,node):
        node.visited = True
        print ("Node : ",node.name)

        for vertex in node.neighbours:
            if not vertex.visited:
                self.dfs(vertex)
    def getNode(self,name):
        for x in self.vertices:
            if x.name == name:
                return x            
    def insert(self,name):
        node = Node(name)
        self.vertices.append(node)
    def insertNeighbours(self,node):
        neighbours = input(f"Enter the neighbours of {node.name} separated by space : ")
        neighbours = [self.getNode(x) for x in neighbours.split(" ") if self.getNode(x)]
        node.neighbours = neighbours

if __name__ == "__main__":
    g = Graph()
    name = input("Enter all nodes separate by space : ")
    name = [x for x in name.split(" ")]
    for x in name:
        g.insert(x)
    for i in g.vertices:
        g.insertNeighbours(i)

    start = input("Enter the node to do DFS from : ")
    node = g.getNode(start)
    print (f"The DFS starting from node {node.name} is -> ")
    if node != -1:
        g.dfs(node)

