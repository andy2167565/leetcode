class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        if k > 3 * 2**(n - 1): return ''
        ans = '^'
        for i in reversed(range(n)):
            choice = sorted(set('abc') - set(ans[-1]))
            q, k = divmod(k , 2**i)
            ans += choice[q - 1] if not k else choice[q]
        return ans[1:]
