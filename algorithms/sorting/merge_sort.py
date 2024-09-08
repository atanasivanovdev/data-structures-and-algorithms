numbers = [6, 5, 3, 1, 8, 7, 2, 4]

from typing import List

def merge_sort(numbers: List) -> List:
    n = len(numbers)
    if n == 1:
        return numbers
    
    middle = n // 2
    left = numbers[:middle]
    right = numbers[middle:]

    return merge(merge_sort(left), merge_sort(right))

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i += 1

    while j < len(right):
        result.append(right[j])
        j += 1
        
    return result


assert merge_sort(numbers) == [1, 2, 3, 4, 5, 6, 7, 8]

print("All tests passed!")