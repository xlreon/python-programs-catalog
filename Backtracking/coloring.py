""" Author - Sidharth Satapathy """

class Color(object):
    def __init__(self, numberOfVertices, numOfColors, graphMatrix):
        self.numberOfVertices = numberOfVertices
        self.numOfColors = numOfColors
        self.colors = [0]*numberOfVertices
        self.graphMatrix = graphMatrix
    def solveColoringProblem(self):
        if self.solve(0):
            self.printSolution()
        else:
            print ("No feasible solution to given problem.")
    def solve(self,nodeIndex):
        if nodeIndex == self.numberOfVertices:
            return True
        # put all the colors
        for colorIndex in range(1,self.numOfColors+1):
            if self.isColorValid(nodeIndex,colorIndex):
                self.colors[nodeIndex] = colorIndex

                if self.solve(nodeIndex+1):
                    return True
        return False
    def isColorValid(self,nodeIndex,colorIndex):
        for i in range(self.numberOfVertices):
            if self.graphMatrix[nodeIndex][i] == 1 and colorIndex == self.colors[i]:
                return False
        return True
    def printSolution(self):
        for i in range(self.numberOfVertices):
            print (self.colors[i])

if __name__ == "__main__":      
    graphMatrix = [[0,1,0,1,0],[1,0,1,0,1],[0,1,0,1,0],[1,1,1,0,1],[0,0,0,1,0]]
    numOfColors = 3
    numOfVertices = 5
    coloringProblem = Color(numOfVertices,numOfColors,graphMatrix)
    coloringProblem.solveColoringProblem()                                