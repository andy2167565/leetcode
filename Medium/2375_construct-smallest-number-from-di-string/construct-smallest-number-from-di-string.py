class Solution:
    def smallestNumber(self, pattern: str) -> str:
# Reference: https://leetcode.com/problems/construct-smallest-number-from-di-string/solutions/2422380/java-c-python-easy-reverse/
#======== <Solution 1> ========#
        ans, stack = [], []
        for i, c in enumerate(pattern + 'I', 1):
            stack.append(str(i))
            if c == 'I':  # Reverse all numbers between each pair of 'I's (the second 'I' is included)
                ans += stack[::-1]
                stack = []
        return ''.join(ans)

#======== <Solution 2> ========#
        ans = []
        for i, c in enumerate(pattern + 'I', 1):
            if c == 'I':
                ans += range(i, len(ans), -1)
        return ''.join(map(str, ans))

#======== <Solution 3> ========#
        ans, pool = [], list('987654321')
        for k in map(len, pattern.split('I')):  # Count number of 'D's between each pair of 'I's
            ans += [pool.pop() for _ in range(k + 1)][::-1]
        return ''.join(ans)
