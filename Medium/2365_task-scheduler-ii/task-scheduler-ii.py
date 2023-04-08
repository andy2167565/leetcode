class Solution:
    def taskSchedulerII(self, tasks: List[int], space: int) -> int:
        # Reference: https://leetcode.com/problems/task-scheduler-ii/solutions/2388301/java-c-python-hashmap/
        import collections
        ans, last = 0, collections.defaultdict(lambda: -len(tasks) - 10)  # The last task of type i is completed on day last[i]
        for task in tasks:
            last[task] = ans = max(ans, last[task] + space) + 1  # Check if the number of days elapsed since the last task execution has exceeded by at least space days
        return ans
