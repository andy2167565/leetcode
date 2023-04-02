class Solution:
    def maximumCostSubstring(self, s: str, chars: str, vals: List[int]) -> int:
        char_vals = dict(zip(chars, vals))
        ans = curr = 0
        for c in s:
            curr = max(curr + char_vals.get(c, ord(c) - 96), 0)  # Reset current substring cost to 0 if it is less than 0
            ans = max(ans, curr)
        return ans
