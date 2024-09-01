import timeit

def reverse_string_slicing(s):
    return s[::-1]

def reverse_string_reversed(s):
    return "".join(reversed(s))

def reverse_string_comprehension(s):
    return "".join([s[i] for i in range(len(s) - 1, -1, -1)])

def reverse_string_pointers(s):
    s = list(s) # O(n)
    start, end = 0, len(s) - 1
    while start < end: # O(n/2)
        s[start], s[end] = s[end], s[start]
        start += 1
        end -= 1
    return "".join(s) # O(n)

def reverse_string_recursive(s):
    if s == "":
        return ""
    else:
        return reverse_string_recursive(s[1:]) + s[0]


medium_str = "yoyomaster" * 60 

# Timeit setup for each function
def measure_performance():
    tests = [
        ("Slicing (medium)", lambda: reverse_string_slicing(medium_str)),
        ("Reversed (medium)", lambda: reverse_string_reversed(medium_str)),
        ("Comprehension (medium)", lambda: reverse_string_comprehension(medium_str)),
        ("Pointers (medium)", lambda: reverse_string_pointers(medium_str)),
        ("Recursive (medium)", lambda: reverse_string_recursive(medium_str)),
    ]
    
    for test_name, test_func in tests:
        time_taken = timeit.timeit(test_func, number=100)
        print(f"{test_name}: {time_taken:.6f} seconds")

# Run performance measurements
measure_performance()
