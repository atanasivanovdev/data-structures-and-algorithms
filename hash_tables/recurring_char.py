# Given an array = [2,5,1,2,3,5,1,2,4]:
# It should return 2

# Given an array = [2,1,1,2,3,5,1,2,4]:
# It should return 1

# Given an array = [2,3,4,5]:
# It should return undefined

input1 = [2,5,1,2,3,5,1,2,4]
input2 = [2,1,1,2,3,5,1,2,4]
input3 = [2,3,4,5]

def firstRecurringCharacter(input):
    unique_values = set()
    for value in input:
        if value not in unique_values:
            unique_values.add(value)
        else:
            return value    
        
    return None

assert firstRecurringCharacter(input1) == 2
assert firstRecurringCharacter(input2) == 1
assert firstRecurringCharacter(input3) == None