""" Author - Sidharth Satapathy """
""" This is python 3 code """
def bubble_sort(arr):
    for i in range(len(arr)-1,0,-1):
        for j in range(i):
            if arr[j] >= arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    return arr

arr = input("Enter the elements of the array separated by space :")
arr = [int(x) for x in arr.split(" ")]

print (f"The Result after sorting is : {bubble_sort(arr)}")
