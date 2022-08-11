class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
#======== <Solution 1> ========#
        if columnNumber == 0: return ""
        from string import ascii_uppercase
        alphabet = list(ascii_uppercase)
        i, j = divmod(columnNumber-1, 26)
        return self.convertToTitle(i) + alphabet[j]

#======== <Solution 2> ========#
        result = []
        while columnNumber > 0:
            columnNumber, r = divmod(columnNumber-1, 26)
            result.append(chr(r + ord('A')))
        return ''.join(result[::-1])
