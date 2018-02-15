""" Author - Sidharth Satapathy """

class Maze(object):
    def __init__(self,matrix):
        self.pathMatrix = matrix
        self.matrixSize = len(matrix)
        self.solutionMatrix = [[0]*self.matrixSize for x in range(self.matrixSize)]
    def solveMazes(self):
        if self.solve(0,0):
            self.showSolution()
        else:
            print ("No path is available")
    def solve(self,x,y):
        if self.isFinished(x,y):
            return True
        if self.isValid(x,y):
            self.solutionMatrix[x][y] = 1
            if self.solve(x+1,y):
                return True
            if self.solve(x,y+1):
                return True
            if self.solve(x-1,y):
                return True
            if self.solve(x,y-1):
                return True    
            self.solutionMatrix[x][y] = 0
        return False        
    def isFinished(self,x,y):
        if x == self.matrixSize-1 and y == self.matrixSize-1:
            if self.pathMatrix[x][y] == 1:
                return True
        return False        
    def isValid(self,x,y):
        if x < 0 or x >= self.matrixSize:
            return False
        if y < 0 or y >= self.matrixSize:
            return False
        if self.pathMatrix[x][y] == 0:
            return False
        return True
    def showSolution(self):
        for x in range(self.matrixSize):
            for y in range(self.matrixSize):
                if self.solutionMatrix[x][y] == 1:
                    print (" - ",end=" ")
                else:
                    print (" @ ",end=" ")
            print ("\n")

if __name__ == "__main__":
    mazeTable = [[ 1, 1, 1, 1 ,1],[ 0, 0, 0, 1, 0],[ 1, 1, 1, 1, 0],[ 1, 0, 0, 0, 0],[ 1, 1, 1, 1, 1]]
    maze = Maze(mazeTable)
    maze.solveMazes()                                                