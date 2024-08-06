# Create a function that reverses a string
# 'Hi My name is Andrei'
# 'ierdnA si eman yM iH'
string = "Hi My name is Andrei"

def reverseString(string):
    if not isinstance(string, str):
        raise TypeError("Only strings are accepted")
    
    if len(string) < 2:
        raise ValueError("The string must be larger than one character")
    
    reversedString = []
    for i in range(len(string), 0, -1):
        reversedString.append(string[i-1])
    return ''.join(reversedString)


print(reverseString(string))

# Reverse string using slicing
print(string[::-1])