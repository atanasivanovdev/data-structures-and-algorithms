# import timeit

def fibonacci_iterative(n):
    fibobacci_seq = [0, 1]
    for i in range(2, n + 1):
        fibobacci_seq.append(fibobacci_seq[i - 2] + fibobacci_seq[i - 1])

    return fibobacci_seq[n]


def fibonacci_recursive(n): 
    if n < 2:
        return n
    
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


print(fibonacci_recursive(6))
print(fibonacci_iterative(6))

# time_recursive = timeit.timeit(lambda: fibonacci_recursive(40), number=5)
# print(f"Recursive: {time_recursive}")

# time_iterative = timeit.timeit(lambda: fibonacci_iterative(40), number=5)
# print(f"Iterative: {time_iterative}")