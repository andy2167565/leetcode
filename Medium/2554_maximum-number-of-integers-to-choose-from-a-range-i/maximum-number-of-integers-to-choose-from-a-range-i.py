class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
#======== <Solution 1> ========#
        candidates = sorted(set(range(1, n + 1)) - set(banned))
        while sum(candidates) > maxSum:
            candidates.pop()
        return len(candidates)

#======== <Solution 2> ========#
        banned, ans, currSum = set(banned), 0, 0
        for num in range(1, n + 1):
            if num not in banned:
                if currSum + num > maxSum:
                    break
                currSum += num
                ans += 1
        return ans
