""" Author - Sidharth Satapathy """
class Fibonacci(object):
    def __init__(self):
        self.memoTable = {} 
        self.memoTable[0] = 0
        self.memoTable[1] = 1
    def getFibonnaciNumber(self,number):
        if number in self.memoTable:
            return self.memoTable[number]
        self.memoTable[number-1] = self.getFibonnaciNumber(number-1)
        self.memoTable[number-2] = self.getFibonnaciNumber(number-2)
        calculateResult = self.memoTable[number-1]+self.memoTable[number-2]
        self.memoTable[number] = calculateResult
        return calculateResult

if __name__ == "__main__":
    n = int(input("Enter a number to find it Fibonacci sum : ")) 
    fib = Fibonacci()
    print (f"The fibonacci sum is : {fib.getFibonnaciNumber(n)}")       