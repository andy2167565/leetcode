class Solution:
    def maxDistance(self, position: List[int], m: int) -> int:
        position.sort()
        
        def count(dist):  # Count the number of balls that can be placed into baskets, under the condition that the minimum distance between any two balls is dist
            ans, curr = 1, position[0]
            for pos in position[1:]:
                if pos - curr >= dist:
                    ans += 1
                    curr = pos
            return ans
        
        l, r = 0, position[-1] - position[0] + 1
        while l < r:  # Find the maximum dist such that count(dist) == m
            mid = l + (r - l) // 2
            if count(mid) >= m:
                l = mid + 1
            else:
                r = mid
        return l - 1  # l is the minimum value to fail, so l - 1 is the maximum value to succeed
