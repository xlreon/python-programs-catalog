""" Author - Sidharth Satapathy """

class RodCutting(object):
    def __init__(self,lengthOfRod,prices):
        self.lengthOfRod = lengthOfRod
        self.prices = prices
        self.memoTable = [[0]*(lengthOfRod+1) for x in range(len(prices))]
    def solve(self):
        for i in range(1,len(self.prices)):
            for j in range(1,self.lengthOfRod+1):
                if i <= j:
                    self.memoTable[i][j] = max(self.memoTable[i-1][j],self.prices[i]+self.memoTable[i][j-1])
                else:
                    self.memoTable[i][j] = self.memoTable[i-1][j]
    def show(self):
        print ("Max profit : %d"% self.memoTable[len(self.prices)-1][self.lengthOfRod])
        colIndex = self.lengthOfRod
        rowIndex = len(self.prices)-1

        while colIndex > 0 or rowIndex >0:
            if self.memoTable[rowIndex][colIndex] == self.memoTable[rowIndex-1][colIndex]:
                rowIndex = rowIndex-1
            else:
                print ("Cut : ",rowIndex,"m")
                colIndex = colIndex - rowIndex

if __name__ == "__main__":
    length = int(input("Enter the length of the rod : "))
    prices = [int(x) for x in input("Enter the prices separated by space : ").split(" ")]
    rodCut = RodCutting(length,prices)
    rodCut.solve()
    rodCut.show()