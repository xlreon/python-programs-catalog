""" Author - Sidharth Satapathy """
""" This code is in python 2 """

class Heap(object):
    def __init__(self,size):
        self.heap = [0]*size
        self.currentPosition = -1
        self.size = size
    def insert(self,data):
        if self.isFull():
            print ("Heap is full.")
            return
        self.currentPosition= self.currentPosition + 1
        self.heap[self.currentPosition] = data
        self.heapify(self.currentPosition) 
    def heapify(self,index):
        parentIndex = int((index-1)/2)
        while parentIndex >= 0 and self.heap[parentIndex] < self.heap[index]:
            temp = self.heap[index]
            self.heap[index] = self.heap[parentIndex]
            self.heap[parentIndex] = temp
            index = parentIndex
            parentIndex = int((index-1)/2)    
    def heapSort(self):
        for i in range(0,self.currentPosition+1):
            temp = self.heap[0]
            print (temp)
            self.heap[0] = self.heap[self.currentPosition-i]
            self.heap[self.currentPosition-i] = temp
            self.heapifySort(0,self.currentPosition-i-1)
    def heapifySort(self, index, to):
        if to < 0:
            to = self.currentPosition
        while index <= to:
            leftChild = 2*index+1
            rightChild = 2*index+2
            if leftChild <= to:
                ChildToSwap = None
                if rightChild > to:
                    ChildToSwap = leftChild
                else:
                    if self.heap[leftChild] > self.heap[rightChild]:
                        ChildToSwap = leftChild
                    else:
                        ChildToSwap = rightChild
                if self.heap[index] < self.heap[ChildToSwap]:
                    temp = self.heap[index]
                    self.heap[index] = self.heap[ChildToSwap]
                    self.heap[ChildToSwap] = temp
                else:
                    break
                index = ChildToSwap
            else:
                break                         
    def isFull(self):
        if self.currentPosition == self.size:
            return True
        else:
            return False        
if __name__ == "__main__":
    size = int(input("Enter the size of the heap : "))
    heap = Heap(size)
    array = input("Enter the elements of the array separated by space : ")
    array = [int(x) for x in array.split(" ")]
    for i in array:
        heap.insert(i)
    choice = int(input("Want to sort the heap (1 - Yes, 2 - No) : "))
    if choice == 1:
        heap.heapSort()    

