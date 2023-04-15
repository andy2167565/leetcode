class Solution:
    def shortestDistanceColor(self, colors: List[int], queries: List[List[int]]) -> List[int]:
        import collections, bisect
        color_indices = collections.defaultdict(list)
        for i, c in enumerate(colors):  # Group all indices by color
            color_indices[c].append(i)
        ans = []
        for i, c in queries:
            if c in color_indices:
                index = bisect.bisect_left(color_indices[c], i)  # Search where index i can be inserted in the list
                if not index:  # i is at the beginning of the list
                    ans.append(color_indices[c][0] - i)
                elif index == len(color_indices[c]):  # i is at the end of list
                    ans.append(i - color_indices[c][-1])
                else:  # i is in the middle of the list
                    ans.append(min(i - color_indices[c][index - 1], color_indices[c][index] - i))
            else:
                ans.append(-1)
        return ans
