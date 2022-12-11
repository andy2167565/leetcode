class Solution:
    def maxJump(self, stones: List[int]) -> int:
# Reference 1: https://leetcode.com/problems/frog-jump-ii/solutions/2897948/java-c-python-max-a-i-a-i-2/
# Reference 2: https://leetcode.com/problems/frog-jump-ii/solutions/2898316/python-always-make-the-longest-2-jump-explained-bonus-one-liner/
# Reference 3: https://leetcode.com/problems/frog-jump-ii/solutions/2898129/decently-explained-python3-code-o-n-w-image/
#======== <Solution 1> ========#
        ans = stones[1]
        for i in range(2, len(stones)):
            ans = max(ans, stones[i] - stones[i - 2])
        return ans

#======== <Solution 2> ========#
        return max([stones[i] - stones[i - 2] for i in range(2, len(stones))], default=stones[1])
