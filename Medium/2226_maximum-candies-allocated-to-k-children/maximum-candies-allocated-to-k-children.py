class Solution:
    def maximumCandies(self, candies: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-candies-allocated-to-k-children/solutions/1908888/java-c-python-binary-search-with-explanation/
        l, r = 0, sum(candies) // k  # l, r and mid represent the number of candies for each child
        while l < r:
            mid = (l + r + 1) // 2  # Get the higher boundary
            if sum(pile // mid for pile in candies) < k:  # Not enough piles for the children
                r = mid - 1
            else:
                l = mid
        return l
