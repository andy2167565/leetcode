class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        import collections
        pairs, counter = 0, collections.Counter()  # {remainder: count}
        for num in arr:
            if counter[-num % k]:  # (x + y) % k = 0 -> x % k = -y % k
                pairs += 1
                counter[-num % k] -= 1
            else:
                counter[num % k] += 1
        return pairs == len(arr) // 2
