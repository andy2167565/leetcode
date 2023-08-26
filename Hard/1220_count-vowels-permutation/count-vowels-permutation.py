class Solution:
    def countVowelPermutation(self, n: int) -> int:
#======== <Solution 1> ========#
        import functools
        hashmap = {
            '.': ['a', 'e', 'i', 'o', 'u'],
            'a': ['e'],
            'e': ['a', 'i'],
            'i': ['a', 'e', 'o', 'u'],
            'o': ['i', 'u'],
            'u': ['a']
        }
        @functools.cache
        def dfs(count, last):
            if count == n:
                return 1
            ans = 0
            for nxt in hashmap[last]:
                ans = (ans + dfs(count + 1, nxt)) % (10**9 + 7)
            return ans
        return dfs(0, '.')

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/count-vowels-permutation/solutions/398286/simple-python-with-diagram/
        a = e = i = o = u = 1
        for _ in range(n - 1):
            a, e, i, o, u = e, a + i, a + e + o + u, i + u, a
        return (a + e + i + o + u) % (10**9 + 7)
