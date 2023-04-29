# 18.Write a program to find the union of two arrays of integers.

def array_union(arr1, arr2):
   
    union_set = set(arr1 + arr2)

   
    union_list = sorted(list(union_set))

    return union_list


array1 = [1, 3, 5, 7]
array2 = [2, 3, 4, 6]
union = array_union(array1, array2)
print(f"The union of {array1} and {array2} is {union}.")
