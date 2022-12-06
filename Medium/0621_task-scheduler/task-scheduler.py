class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        # Reference 1: https://leetcode.com/problems/task-scheduler/solutions/104507/python-straightforward-with-explanation/comments/757631
        # Reference 2: https://leetcode.com/problems/task-scheduler/solutions/760266/python-4-lines-linear-solution-detailed-explanation/
        # Reference 3: https://leetcode.com/problems/task-scheduler/solutions/761070/python-heavily-visualized-detailed-explanation/
        import collections
        counts = collections.Counter(tasks)
        max_count = counts.most_common()[0][1]
        max_count_tasks = sum(counts[k] == max_count for k in counts)  # Number of tasks with maximum count
        return max(len(tasks), (max_count - 1) * (n + 1) + max_count_tasks)  # (max_count - 1) indicates number of chunks with idle; (n + 1) indicates length of chunk with idle
