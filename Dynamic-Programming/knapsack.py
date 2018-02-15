""" Author - Sidharth Satapathy """

class Knapsack(object):
    def __init__(self,noOfItems,weightOfBag,weightOfItems,valueOfItems):
        self.noOfItems = noOfItems
        self.weightOfBag = weightOfBag
        self.weightOfItems = weightOfItems
        self.valueOfItems = valueOfItems
        self.memoTable = [[0 for x in range(self.weightOfBag+1)] for y in range(self.noOfItems+1)]
    def solveKnapsack(self):
        for i in range(self.noOfItems+1):
            for w in range(self.weightOfBag+1):

                noTakingItem = self.memoTable[i-1][w]
                takingItem = 0

                if self.weightOfItems[i] <= w:
                    takingItem = self.valueOfItems[i] + self.memoTable[i-1][w-self.weightOfItems[i]]
                self.memoTable[i][w] = max(takingItem,noTakingItem)
    def showResults(self):
        print (f"Total value : $ {float(self.memoTable[self.noOfItems][self.weightOfBag])}/-")
        w = self.weightOfBag
        for n in range(self.noOfItems,0,-1):
            if self.memoTable[n][w] != 0 and self.memoTable[n][w] != self.memoTable[n-1][w]:
                print (f"item {n} was taken.")
                w = w - self.weightOfItems[n]       

if __name__ == "__main__":
    
        numOfItems = 4
        capacityOfKnapsack = 7
        weightOfItems = [0,1,3,4,5]
        profitOfItems = [0,1,4,5,7]
        

        knapsack = Knapsack(numOfItems, capacityOfKnapsack, weightOfItems, profitOfItems)
        knapsack.solveKnapsack()
        knapsack.showResults()                        