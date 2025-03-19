# International Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes, as follows:

# 'a' maps to ".-",
# 'b' maps to "-...",
# 'c' maps to "-.-.", and so on.
# For convenience, the full table for the 26 letters of the English alphabet is given below:

# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
# Given an array of strings words where each word can be written as a concatenation of the Morse code of each letter.

# For example, "cab" can be written as "-.-..--...", which is the concatenation of "-.-.", ".-", and "-...". We will call such a concatenation the transformation of a word.
# Return the number of different transformations among all words we have.


"""
Example 1:
Input: words = ["gin","zen","gig","msg"]
Output: 2
Explanation: The transformation of each word is:
"gin" -> "--...-."
"zen" -> "--...-."
"gig" -> "--...--."
"msg" -> "--...--."
There are 2 different transformations: "--...-." and "--...--.".

Example 2:
Input: words = ["a"]
Output: 1
"""

from typing import List


def uniqueMorseRepresentations(words: List[str]) -> int:
    morse_code = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--.."]
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    morse_dict = {char: code for char, code in zip(alphabet, morse_code)}
    
    transformations = {"".join(morse_dict[char] for char in word) for word in words}
    
    return len(transformations)



assert uniqueMorseRepresentations(["gin", "zen", "gig", "msg"]) == 2, f"Test case 1 failed: {uniqueMorseRepresentations(['gin', 'zen', 'gig', 'msg'])} != 2"
assert uniqueMorseRepresentations(["a"]) == 1, f"Test case 2 failed: {uniqueMorseRepresentations(['a'])} != 1"

print("All test cases passed!")