# You are given an array of logs. Each log is a space-delimited string of words,
# where the first word is the identifier.

# There are two types of logs:
# - Letter-logs: All words (except identifier) consist of lowercase English letters.
# - Digit-logs: All words (except identifier) consist of digits.

# Reorder logs so that:
# 1. Letter-logs come before all digit-logs.
# 2. Letter-logs sorted lexicographically by content; if same, sort by identifier.
# 3. Digit-logs maintain their relative ordering.

'''
Example 1:
Input: logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]
Output: ["let1 art can","let3 art zero","let2 own kit dig","dig1 8 1 5 1","dig2 3 6"]

Example 2:
Input: logs = ["a1 9 2 3 1","g1 act car","zo4 4 7","ab1 off key dog","a8 act zoo"]
Output: ["g1 act car","a8 act zoo","ab1 off key dog","a1 9 2 3 1","zo4 4 7"]
'''

def reorderLogFiles(logs):
    """
    :type logs: List[str]
    :rtype: List[str]
    """
    letter_logs = []
    digit_logs = []

    for log in logs:
        parts = log.split(' ', 1)
        identifier = parts[0]
        content = parts[1]

        if content[0].isdigit():
            digit_logs.append(log)
        else:
            letter_logs.append((identifier, content, log))

    letter_logs.sort(key=lambda x: (x[1], x[0]))

    result = [log for _, _, log in letter_logs] + digit_logs
    return result


logs1 = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]
assert reorderLogFiles(logs1) == ["let1 art can", "let3 art zero", "let2 own kit dig", "dig1 8 1 5 1", "dig2 3 6"], "Test Case 1 Failed"

logs2 = ["a1 9 2 3 1", "g1 act car", "zo4 4 7", "ab1 off key dog", "a8 act zoo"]
assert reorderLogFiles(logs2) == ["g1 act car", "a8 act zoo", "ab1 off key dog", "a1 9 2 3 1", "zo4 4 7"], "Test Case 2 Failed"

print("All test cases passed!")
