class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        import bisect
        start, end = [], []
        for s, e in flowers:
            start.append(s)
            end.append(e)
        start.sort()
        end.sort()
        return [bisect.bisect_right(start, t) - bisect.bisect_left(end, t) for t in people]
