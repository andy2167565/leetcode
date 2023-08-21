class Solution:
    def maxLength(self, arr: List[str]) -> int:
        dp = [set()]
        for s in arr:
            if len(set(s)) == len(s):  # The characters of the string are unique
                s = set(s)
                for c in dp:
                    if not s & c:  # The concatenation of s and c is unique
                        dp.append(s | c)
        return max(len(s) for s in dp)
