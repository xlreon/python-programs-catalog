""" Author - Sidharth Satapathy """

class Hamiltonian:
    def __init__(self, adjacencyMatrix):
        self.numberOfVertexes = len(adjacencyMatrix)
        self.hamiltonianPath = [None]*self.numberOfVertexes
        self.adjancencyMatrix = adjacencyMatrix
    def hamiltonianCycle(self):
        self.hamiltonianPath[0] = 0
        if not self.possibleSolution(1):
            print ("No feasible solution is present.")
        else:
            self.showHamiltonianPath()
    def possibleSolution(self,position):
        if position == self.numberOfVertexes:
            x = self.hamiltonianPath[position-1]
            y = self.hamiltonianPath[0]
            if self.adjancencyMatrix[x][y] == 1:
                return True
            else:
                return False
        for vertexIndex in range(1,self.numberOfVertexes):
            if self.feasible(vertexIndex,position):
                self.hamiltonianPath[position] = vertexIndex
                if self.possibleSolution(position+1):
                    return True
        return False
    def feasible(self, vertex, actualPosition):
        # Checking if there exist a path between 2 vertex
        if self.adjancencyMatrix[self.hamiltonianPath[actualPosition-1]][vertex] == 0:
            return False
        for i in range(actualPosition):
            if self.hamiltonianPath[i] == vertex:
                return False
        return True
    def showHamiltonianPath(self):
        print('Hamiltonian cycle exists: ')
        for i in range(self.numberOfVertexes):
                print(self.hamiltonianPath[i])
        print(self.hamiltonianPath[0])

if __name__ == "__main__":
    adjacencyMatrix = [[0,1,0],[1,0,1],[1,1,0]]
    hamiltonian = Hamiltonian(adjacencyMatrix)
    hamiltonian.hamiltonianCycle()
