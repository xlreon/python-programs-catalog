""" Author - Sidharth Satapathy """

#code

def getSum(a,s):
    temp = s
    for i in range(0,len(a)):
        temp = s
        temp = temp - a[i]
        for j in range(i+1,len(a)):
            curr = a[j]
            if temp > 0:
                temp = temp - curr
                if temp == 0:
                    print (i+1," ",j+1)
                    return 
            else:
                break

no = int(input())
for i in range(0,no):
    inp = [int(x) for x in input().strip().split(" ") if x != " "]
    arr = [int(x) for x in input().strip().split(" ") if x != " "]
    getSum(arr,inp[1])
