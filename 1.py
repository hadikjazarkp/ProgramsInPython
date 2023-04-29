#1.Write a function to find the maximum element in a array
def names(arr):
    max_elem=arr[0]
     
    for elem in arr:
        if elem>max_elem:
            max_elem=elem
    return max_elem
arrays=[1,2,3,6]
max_elem=names(arrays)
print(max_elem)
