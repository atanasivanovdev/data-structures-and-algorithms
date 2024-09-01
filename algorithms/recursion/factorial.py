import timeit

def find_factorial_recursive(number):
    if number == 1:
        return 1
    
    return number * find_factorial_recursive(number - 1)


def find_factorial_iterative(number):
    answer = 1
    for number in range(1, number + 1):
        answer *= number

    return answer

time_recursive = timeit.timeit(lambda: find_factorial_recursive(200), number=10)
print(f"Recursive: {time_recursive}")

time_iterative = timeit.timeit(lambda: find_factorial_iterative(200), number=10)
print(f"Iterative: {time_iterative}")
