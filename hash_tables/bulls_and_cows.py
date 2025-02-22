# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

 
"""
Example 1:
Input: secret = "1807", guess = "7810"
Output: "1A3B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1807"
  |
"7810"

Example 2:
Input: secret = "1123", guess = "0111"
Output: "1A1B"
Explanation: Bulls are connected with a '|' and cows are underlined:
"1123"        "1123"
  |      or     |
"0111"        "0111"
Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
"""

from collections import Counter

def getHint(secret, guess):
    bulls = sum(s == g for s, g in zip(secret, guess))

    secret_counts = Counter(secret)
    guess_counts = Counter(guess)

    cows = sum(min(secret_counts[d], guess_counts[d]) for d in secret_counts) - bulls

    return f"{bulls}A{cows}B"


# Test case 1
secret = "1807"
guess = "7810"
assert getHint(secret, guess) == "1A3B", "Test case 1 failed"

# Test case 2
secret = "1123"
guess = "0111"
assert getHint(secret, guess) == "1A1B", "Test case 2 failed"

print("All test cases passed!")