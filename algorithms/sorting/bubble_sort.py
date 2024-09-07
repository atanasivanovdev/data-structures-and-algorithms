
numbers1 = [6, 5, 3, 1, 8, 7, 2, 4]
numbers2 = [6, 5, 3, 1, 8, 7, 2, 4]

from typing import List

def bubble_sort(numbers: List) -> List:
    i = 0
    n = len(numbers) - 1
    while i < n:
        if numbers[i] > numbers[i + 1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
        
        if i + 1 == n:
            n -= 1
            i = 0
        else:
            i += 1

    return numbers

def bubble_sort_nested(numbers: List) -> List:
    n = len(numbers)
    for i in range(n):
        for j in range(n-i-1):
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]
    return numbers

assert bubble_sort(numbers1) == [1, 2, 3, 4, 5, 6, 7, 8]
assert bubble_sort_nested(numbers2) == [1, 2, 3, 4, 5, 6, 7, 8]

print("All tests passed!")