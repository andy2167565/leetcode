import collections, bisect
class RangeFreqQuery:

    def __init__(self, arr: List[int]):
        self.freqs = collections.defaultdict(list)
        for i, num in enumerate(arr):
            self.freqs[num].append(i)

    def query(self, left: int, right: int, value: int) -> int:
        return bisect.bisect_right(self.freqs[value], right) - bisect.bisect_left(self.freqs[value], left)


# Your RangeFreqQuery object will be instantiated and called as such:
# obj = RangeFreqQuery(arr)
# param_1 = obj.query(left,right,value)
