""" Author - Sidharth Satapathy """

# To find the maximum index

def maxIndex(a,size):
    index = 0
    if size == 0:
        return 
    for i in range(0,size):
        for j in range(size-1,i,-1):
            if a[i] <= a[j] :
                if j-i >= index :
                    index = j-i
                break
    return (index) 

for i in range(0,int(input())):
    size = int(input())
    arr = [int(x) for x in input().strip().split(" ")]
    print (maxIndex(arr,size))