# You have n jobs and m workers. You are given three arrays: difficulty, profit, and worker where
# difficulty[i] and profit[i] are the difficulty and the profit of the ith job, and
# worker[j] is the ability of the jth worker (i.e., the jth worker can only complete a job with
# difficulty at most worker[j]).
# Every worker can be assigned at most one job, but one job can be completed multiple times.
# Return the maximum profit we can achieve after assigning the workers to the jobs.

"""
Example 1:
Input: difficulty = [2,4,6,8,10], profit = [10,20,30,40,50], worker = [4,5,6,7]
Output: 100
Explanation: Workers are assigned jobs of difficulty [4,4,6,6] and they get a profit of [20,20,30,30] separately.

Example 2:
Input: difficulty = [85,47,57], profit = [24,66,99], worker = [40,25,25]
Output: 0
"""

def maxProfitAssignment(difficulty, profit, worker):
    """
    :type difficulty: List[int]
    :type profit: List[int]
    :type worker: List[int]
    :rtype: int
    """
    jobs = sorted(zip(difficulty, profit))
    worker.sort()

    total_profit = 0
    best_profit = 0
    job_index = 0

    for ability in worker:
        while job_index < len(jobs) and jobs[job_index][0] <= ability:
            best_profit = max(best_profit, jobs[job_index][1])
            job_index += 1
        total_profit += best_profit

    return total_profit


assert maxProfitAssignment([2,4,6,8,10], [10,20,30,40,50], [4,5,6,7]) == 100
assert maxProfitAssignment([85,47,57], [24,66,99], [40,25,25]) == 0

print("All test cases passed!")
