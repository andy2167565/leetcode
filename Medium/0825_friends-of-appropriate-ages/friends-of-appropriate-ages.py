class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        import collections
        def request(x, y):
            return not (y <= 0.5 * x + 7 or y > x or y > 100 and x < 100)
        counter = collections.Counter(ages)
        return sum(request(x, y) * counter[x] * (counter[y] - (x == y)) for x in counter for y in counter)
