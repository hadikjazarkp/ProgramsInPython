# 6.Write a function to find the second largest number in a array.

def second_large(arr):
    arr.sort()
    print("Second largest elem is",arr[-2])

arr=[1,3,2,5,4,9]
second_larg=second_large(arr)


