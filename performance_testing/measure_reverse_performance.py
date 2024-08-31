import timeit

# Sample list to reverse
nums = list(range(1000000))

# Function using the built-in reverse method
def test_reverse_builtin():
    nums_copy = nums.copy()
    nums_copy.reverse()

# Function using a manual while loop
def test_reverse_while():
    nums_copy = nums.copy()
    start = 0
    end = len(nums_copy) - 1
    while start < end:
        nums_copy[start], nums_copy[end] = nums_copy[end], nums_copy[start]
        start += 1
        end -= 1

# Measure the performance of the built-in reverse method
time_builtin = timeit.timeit(test_reverse_builtin, number=10)
print(f"Built-in reverse: {time_builtin} seconds")

# Measure the performance of the manual while loop
time_while = timeit.timeit(test_reverse_while, number=10)
print(f"Manual while loop reverse: {time_while} seconds")