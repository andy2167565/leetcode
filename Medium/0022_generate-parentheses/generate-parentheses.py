class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/generate-parentheses/discuss/10283/Python-simple-stack-solution-without-recursion
        # p: Parenthesis-string built so far
        # left, right: Current count of left and right parentheses added
        ans = []
        stack = [('(', 1, 0)]
        while stack:
            p, left, right = stack.pop()
            if left == right == n:
                ans.append(p)
                continue
            if left < n:
                stack.append((p + '(', left + 1, right))
            if right < left:
                stack.append((p + ')', left, right + 1))
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/generate-parentheses/discuss/10096/4-7-lines-Python
        # p: Parenthesis-string built so far
        # left, right: Number of left and right parentheses still to add
        # parens: Collect the parentheses
        def generate(p, left, right, parens = []):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p,
            return parens
        return generate('', n, n)

#======== <Solution 3> ========#
        # Reference: https://leetcode.com/problems/generate-parentheses/discuss/10369/Clean-Python-DP-Solution
        dp = [['']] + [[] for _ in range(n)]
        for i in range(1, n + 1):
            for j in range(i):
                dp[i] += ['(' + x + ')' + y for x in dp[j] for y in dp[i - j - 1]]
        return dp[n]

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/generate-parentheses/solution/167241
        ans = []
        for i in range(n):
            for left in self.generateParenthesis(i):
                for right in self.generateParenthesis(n - i - 1):
                    ans.append(f'({left}){right}')
        return ans or ['']
