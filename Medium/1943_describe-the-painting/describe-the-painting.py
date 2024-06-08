class Solution:
    def splitPainting(self, segments: List[List[int]]) -> List[List[int]]:
        # Reference: https://leetcode.com/problems/describe-the-painting/solutions/1359717/python-easy-solution-in-o-n-logn-with-detailed-explanation/
        import collections
        mapping = collections.defaultdict(int)  # mapping[i]: The change in color difference at position i
        for start, end, color in segments:
            mapping[start] += color
            mapping[end] -= color
        ans, start, color = [], None, 0
        for end in sorted(mapping):
            if color:  # Current segment is painted
                ans.append((start, end, color))
            color += mapping[end]  # Paint the current position
            start = end
        return ans
