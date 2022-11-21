class TimeMap:

    def __init__(self):
        import collections
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.dict[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        arr = self.dict[key]
        if not arr: return ''
        l, r = 0, len(arr)
        while l < r:
            mid = l + (r - l) // 2
            if arr[mid][0] <= timestamp:  # bisect_right
                l = mid + 1
            else:
                r = mid
        return '' if not r else arr[r - 1][1]


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)
