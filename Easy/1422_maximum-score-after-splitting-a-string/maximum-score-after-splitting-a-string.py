class Solution:
    def maxScore(self, s: str) -> int:
        score = zeros = 0
        ones = s.count('1')
        for i in range(len(s) - 1):
            zeros += s[i] == '0'
            ones -= s[i] == '1'
            score = max(score, zeros + ones)
        return score
