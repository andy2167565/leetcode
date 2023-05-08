class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
# Reference: https://leetcode.com/problems/maximize-the-confusion-of-an-exam/solutions/1499049/java-c-python-sliding-window-strict-o-n/
#======== <Solution 1> ========#
        import collections
        ans = M = 0  # M is the maximum frequency of the same character in the sliding window
        count = collections.Counter()
        for i in range(len(answerKey)):
            count[answerKey[i]] += 1
            M = max(M, count[answerKey[i]])
            if ans < M + k:
                ans += 1
            else:  # Invalid window, move left pointer by 1 step
                count[answerKey[i - ans]] -= 1
        return ans

#======== <Solution 2> ========#
        import collections
        M = l = 0
        count = collections.Counter()
        for r in range(len(answerKey)):
            count[answerKey[r]] += 1
            M = max(M, count[answerKey[r]])
            if r - l + 1 > M + k:  # Invalid window
                count[answerKey[l]] -= 1
                l += 1
        return len(answerKey) - l
