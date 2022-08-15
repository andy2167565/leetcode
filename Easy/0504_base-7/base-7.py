class Solution:
    def convertToBase7(self, num: int) -> str:
        if num == 0: return '0'
        ans = []
        q = abs(num)
        while q > 0:
            q, r = divmod(q, 7)
            ans.append(str(r))
        if num < 0: ans.append('-')
        return ''.join(reversed(ans))
