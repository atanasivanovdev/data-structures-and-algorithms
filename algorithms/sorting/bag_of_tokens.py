# You start with an initial power of power, an initial score of 0, and a bag of tokens.
# In one move, you can play an unplayed token in one of two ways:
# Face-up: if power >= token value, lose that power and gain 1 score.
# Face-down: if score >= 1, gain that token's power and lose 1 score.
# Return the maximum score possible.

"""
Example 1:
Input: tokens = [100], power = 50
Output: 0

Example 2:
Input: tokens = [200,100], power = 150
Output: 1

Example 3:
Input: tokens = [100,200,300,400], power = 200
Output: 2
"""

def bagOfTokensScore(tokens, power):
    """
    :type tokens: List[int]
    :type power: int
    :rtype: int
    """
    tokens.sort()

    left, right = 0, len(tokens) - 1
    score = 0
    max_score = 0

    while left <= right:
        if power >= tokens[left]:
            power -= tokens[left]
            left += 1
            score += 1
            max_score = max(max_score, score)
        elif score > 0:
            power += tokens[right]
            right -= 1
            score -= 1
        else:
            break

    return max_score


assert bagOfTokensScore([100], 50) == 0
assert bagOfTokensScore([200,100], 150) == 1
assert bagOfTokensScore([100,200,300,400], 200) == 2

print("All test cases passed!")
