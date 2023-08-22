class Solution:
    def maximumBeauty(self, items: List[List[int]], queries: List[int]) -> List[int]:
        # Reference: https://leetcode.com/problems/most-beautiful-item-for-each-query/solutions/1576050/python-4-lines-solution/
        import bisect
        items = sorted(items + [[0, 0]])
        for i in range(len(items) - 1):  # Find the maximum beauty of items[:i+1] for each i
            items[i + 1][1] = max(items[i][1], items[i + 1][1])
        return [items[bisect.bisect(items, [q + 1]) - 1][1] for q in queries]
