# 10.Write a program to find the maximum and minimum   elements in an array of integers.

def find_max_min(arr):

    max_num = arr[0]
    min_num = arr[0]
   
    for num in arr[1:]:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num

    return (max_num, min_num)

arr = [5, 1, 9, 3, 7]
max_num, min_num = find_max_min(arr)
print("Maximum number:", max_num) 
print("Minimum number:", min_num) 
