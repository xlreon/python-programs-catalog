""" Author - Sidharth Satapathy """
""" This is python 3 code """
def insertion_sort(arr):
    position = 0
    for i in range(1,len(arr)):
        position = i
        currentValue = arr[i]
        while position > 0 and arr[position-1] > currentValue:
            arr[position] = arr[position-1]
            position-=1
        arr[position] = currentValue
    return arr
array = input("Enter array elements separated by space : ")
array = [int(x) for x in array.split(" ")]

print (f"This array after sorting is : {insertion_sort(array)}")             