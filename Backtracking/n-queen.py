""" Author - Sidharth Satapathy """

class Queen(object):
    def __init__(self,queens):
        self.noOfQueens = queens
        self.chessTable = [[None for i in range(queens)] for j in range(queens)]
    def solveQueen(self):
        if self.solve(0):
            self.printQueen()
        else:
            print ("There is no solution.")
    def solve(self, colIndex):
        if colIndex == self.noOfQueens:
            return True
        for rowIndex in range(self.noOfQueens):
            if self.isPlaceValid(rowIndex, colIndex):
                self.chessTable[rowIndex][colIndex] = 1
                if self.solve(colIndex+1):
                    return True
            # Backtracking and chess cell reset
            self.chessTable[rowIndex][colIndex] = 0
        return False
    def isPlaceValid(self, rowIndex, colIndex):
        # Check for row constraint
        for j in range(colIndex):
            if self.chessTable[rowIndex][j] == 1:
                return False
        # Check for diagonal bottom right to top left
        j = colIndex
        for i in range(rowIndex,-1,-1):
            if j < 0:
                break
            if self.chessTable[i][j] == 1:
                return False
            j = j - 1
        j = colIndex
        for i in range(rowIndex,len(self.chessTable)):
            if j < 0:
                break
            if self.chessTable[i][j] == 1 :
                return False
            j = j - 1
        return True

    def printQueen(self):
        for i in range(self.noOfQueens):
            for j in range(self.noOfQueens):
                if self.chessTable[i][j] == 1:
                    print (" @ ",end="")
                else:
                    print (" - ",end="")
            print ("\n")

if __name__ == "__main__":
    n  = input("Enter the number of queens : ")
    q = Queen(int(n))
    q.solveQueen()
                                
