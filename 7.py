# 7.Write a function to remove duplicates from a array

def remove_duplicates(arr):
    
    return list(set(arr))

arr = [1, 2, 3, 3, 4, 5, 5]
unique_arr = remove_duplicates(arr)
print(unique_arr) # Output: [1, 2, 3, 4, 5]
