""" Author - Sidharth Satapathy """
""" This is python 3 code """

def quick_sort(arr):
    quick_sort_helper(arr,0,len(arr)-1)
    return arr
def quick_sort_helper(arr,first,last):
    if first < last:
        splitPoint = partion(arr,first,last)
        quick_sort_helper(arr,first,splitPoint-1)
        quick_sort_helper(arr,splitPoint+1,last)

def partion(arr,first,last):
    pivot = arr[first]
    leftMark = first+1
    rightMark = last
    done = False 
    while not done:
        while leftMark <= rightMark and arr[leftMark] <= pivot:
            leftMark+=1
        while leftMark <= rightMark and arr[rightMark] >= pivot:
            rightMark-=1
        if rightMark < leftMark:
            done = True
        else:
            temp = arr[leftMark]
            arr[leftMark] = arr[rightMark]
            arr[rightMark] = temp        
    temp = arr[first]
    arr[first] = arr[rightMark]
    arr[rightMark] = temp
    return rightMark


array = input("Enter the array elements separated by space : ")
array = [int(x) for x in array.split(" ")]
print (f"The array after sorting is : {quick_sort(array)}")        