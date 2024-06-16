class Solution:
    def palindromePartition(self, s: str, k: int) -> int:
        def cost(s, i, j):  # Calculate the cost of transferring one substring into palindrome
            r = 0
            while i < j:
                if s[i] != s[j]:
                    r += 1
                i += 1
                j -= 1
            return r

        def dfs(i, k):
            if (i, k) in memo:  # Case already in memo
                return memo[(i, k)]
            if n - i == k:  # Each substring only have one character
                return 0
            if k == 1:  # Need to transfer the whole substring into palindrome
                return cost(s, i, n - 1)
            ans = float('inf')
            for j in range(i + 1, n - k + 2):  # Keep turning the next part of substring into palindrome
                ans = min(ans, dfs(j, k - 1) + cost(s, i, j - 1))  # Compare different divisions to get the minimum cost
            memo[(i, k)] = ans
            return ans

        n, memo = len(s), {}
        return dfs(0, k)
