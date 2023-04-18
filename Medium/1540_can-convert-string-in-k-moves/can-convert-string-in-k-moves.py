class Solution:
    def canConvertString(self, s: str, t: str, k: int) -> bool:
        # Reference: https://leetcode.com/problems/can-convert-string-in-k-moves/solutions/779903/java-python-3-o-n-count-the-shift-displacement-w-brief-explanation-and-analysis/
        if len(s) != len(t):
            return False
        count = [0] * 26
        for cs, ct in zip(s, t):
            diff = (ord(ct) - ord(cs)) % 26  # Explanation: https://stackoverflow.com/questions/3883004/how-does-the-modulo-operator-work-on-negative-numbers-in-python
            if diff > 0 and count[diff] * 26 + diff > k:
                return False
            count[diff] += 1
        return True
