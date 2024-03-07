class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        # Reference: https://leetcode.com/problems/two-best-non-overlapping-events/solutions/1552570/very-simple-sort-greedy-no-dp-no-binary-search-no-heap-pq-bst/
        arr = []
        ans = max_value = 0
        for start, end, value in events:
            arr.append((start, True, value))
            arr.append((end + 1, False, value))
        arr.sort()
        for time, started, value in arr:
            if started:
                ans = max(ans, max_value + value)
            else:
                max_value = max(max_value, value)
        return ans
