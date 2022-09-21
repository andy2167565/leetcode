class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
#======== <Solution 1> ========#
        return ' '.join(s.split(maxsplit=k)[:k])

#======== <Solution 2> ========#
        for i, c in enumerate(s):
            if c == ' ':
                k -= 1
                if not k:
                    return s[:i]
        return s

#======== <Solution 3> ========#
        return re.search("( ?\w+){" + str(k) + "}", s).group()
