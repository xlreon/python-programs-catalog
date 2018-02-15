""" Author - Sidharth Satapathy """

class Coin(object):
    def __init__(self,totalCoins,values):
        self.totalCoins = totalCoins
        self.values = values
        self.memoTable = [[0]*(totalCoins+1) for x in range(len(values) + 1)]

    def solve(self):
        for i in range(len(self.values)+1):
            self.memoTable[i][0] = 1
        for i in range(1,len(self.values)+1):
            for j in range(1,self.totalCoins+1):
                if self.values[i-1] <= j:
                    self.memoTable[i][j] = self.memoTable[i-1][j] + self.memoTable[i][j-self.values[i-1]]
                else:
                    self.memoTable[i][j] = self.memoTable[i-1][j]
        print ("The number of ways that can done is : ",self.memoTable[len(self.values)][self.totalCoins])

if __name__ == "__main__":
    m = int(input("Enter the number of coins : "))
    coins = [int(x) for x in input("Enter the values of coins separated by space : ").split(" ")]
    coin = Coin(m,coins)
    coin.solve()                  
