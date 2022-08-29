class Solution:
    def countOrders(self, n: int) -> int:
#======== <Solution 1> ========#
        # Reference 1: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516968/JavaC%2B%2BPython-Easy-and-Concise
        # Reference 2: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516941/Python-O(n)-with-detailed-explanations
        res, mod = 1, 10**9 + 7
        for i in range(2, n + 1):
            res = res * (i * 2 - 1) * i % mod
        return res

#======== <Solution 2> ========#
        import math
        return (math.factorial(n * 2) >> n) % (10**9 + 7)

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/count-all-valid-pickup-and-delivery-options/discuss/516933/C%2B%2BPython-1-line-Simple-permutation-with-explanation
        import math
        return math.factorial(n) * math.prod(range(1, 2 * n, 2)) % (10**9 + 7)
