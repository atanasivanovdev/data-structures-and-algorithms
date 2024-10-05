numbers = [6, 5, 3, 1, 8, 7, 2, 4]

from typing import List

def insertion_sort(numbers: List) -> List:
    n = len(numbers)
    for i in range(n-1):
        if numbers[i] > numbers[i+1]:
            end = i
            while end >= 0 and numbers[end + 1] < numbers[end]:
                numbers[end + 1], numbers[end] = numbers[end], numbers[end + 1]
                end -= 1
    return numbers

assert insertion_sort(numbers) == [1, 2, 3, 4, 5, 6, 7, 8]

numbers2 = [6, 5, 3, 1, 8, 7, 2, 4]
def insertion_sort_standard(numbers: List[int]) -> List[int]:
    n = len(numbers)
    for i in range(1, n):
        key = numbers[i]
        j = i - 1
        while j >= 0 and key < numbers[j]:
            numbers[j + 1] = numbers[j]
            j -= 1
        numbers[j + 1] = key
    return numbers

assert insertion_sort_standard(numbers) == [1, 2, 3, 4, 5, 6, 7, 8]

print("All tests passed!")