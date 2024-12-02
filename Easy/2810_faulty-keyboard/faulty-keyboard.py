class Solution:
    def finalString(self, s: str) -> str:
        chars = []
        for c in s:
            if c == 'i':
                chars = chars[::-1]
            else:
                chars.append(c)
        return ''.join(chars)
