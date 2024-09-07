numbers = [6, 5, 3, 1, 8, 7, 2, 4]

from typing import List

def selection_sort(numbers: List) -> List:
    n = len(numbers)
    for i in range(n):
        min = i
        for j in range(i+1, n):
            if numbers[j] < numbers[min]:
                min = j
        numbers[i], numbers[min] = numbers[min], numbers[i]
    return numbers

assert selection_sort(numbers) == [1, 2, 3, 4, 5, 6, 7, 8]

print("All tests passed!")