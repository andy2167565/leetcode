class Solution:
    def queryString(self, s: str, n: int) -> bool:
#======== <Solution 1> ========#
        return all(bin(i)[2:] in s for i in range(n, n // 2, -1))

#======== <Solution 2> ========#
        ans = set()
        for i in range(len(s)):
            for j in range(i, i + n.bit_length()):
                num = int(s[i:j + 1], 2)
                if 1 <= num <= n:
                    ans.add(num)
        return len(ans) == n
