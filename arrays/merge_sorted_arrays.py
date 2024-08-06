# Merge sorted arrays
# arr1 = [0 ,3, 4, 31]
# arr2 = [4, 6, 30]
# result = [0, 3, 4, 4, 6, 30, 31]

arr1 = [0 ,3, 4, 31]
arr2 = [4, 6, 30]

def mergeSortedArrays(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("The parameters must be lists")
    
    merged_array = []
    arr1_pointer = 0
    arr2_pointer = 0
    total_size = len(arr1) + len(arr2)
    
    if not arr1:
        return arr2
    
    if not arr2:
        return arr1

    while 0 < total_size:
        if len(arr1) == arr1_pointer:
            merged_array.append(arr2[arr2_pointer])
            arr2_pointer += 1
        elif len(arr2) == arr2_pointer:
            merged_array.append(arr1[arr1_pointer])
            arr1_pointer += 1
        elif arr1[arr1_pointer] < arr2[arr2_pointer]:
            merged_array.append(arr1[arr1_pointer])
            arr1_pointer += 1
        else:
            merged_array.append(arr2[arr2_pointer])
            arr2_pointer += 1
        total_size -= 1

    return merged_array

# Time complexity: O(n+m)
print(mergeSortedArrays(arr1, arr2))

def mergeSortedArrays2(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("The parameters must be lists")
    
    if not arr1:
        return arr2
    
    if not arr2:
        return arr1
    
    arr1.extend(arr2)
    arr1.sort()
    return arr1
# Time complexity O((n+m)log(n+m))
# print(mergeSortedArrays2(arr1, arr2))


def mergeSortedArrays3(arr1, arr2):
    if not isinstance(arr1, list) or not isinstance(arr2, list):
        raise TypeError("The parameters must be lists")
    
    merged_array = []
    i, j = 0, 0
    n, m = len(arr1), len(arr2)
    
    if not arr1:
        return arr2
    
    if not arr2:
        return arr1

    while i < n and j < m:
        if arr1[i] < arr2[j]:
            merged_array.append(arr1[i])
            i += 1
        else:
            merged_array.append(arr2[j])
            i += 1

    if i < n:
        merged_array.extend(arr1[i:])
    if j < m:
        merged_array.extend(arr2[j:])

    return merged_array
# Time complexity O(n+m)
print(mergeSortedArrays2(arr1, arr2))