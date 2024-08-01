class Solution:
    def maximumTastiness(self, price: List[int], k: int) -> int:
        # Reference: https://leetcode.com/problems/maximum-tastiness-of-candy-basket/solutions/2947983/c-java-python-binary-search-and-sorting/
        price.sort()

        def check(diff):  # Check if the given value can be the minimum difference for any subsequence of the array price
            last, count, i = price[0], 1, 1
            while count < k and i < len(price):
                if price[i] - last >= diff:
                    last, count = price[i], count + 1
                i += 1
            return count == k

        lo, hi = 0, 10**9
        while lo < hi:
            mid = (lo + hi) // 2
            if check(mid):
                lo = mid + 1
            else:
                hi = mid
        return lo - 1
