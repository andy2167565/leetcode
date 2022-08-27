class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        import math
        nums, ans = list(range(1, n + 1)), ''
        for i in reversed(range(n)):
            q, k = divmod(k, math.factorial(i))
            ans += str(nums.pop(q - 1)) if not k else str(nums.pop(q))
        return ans
