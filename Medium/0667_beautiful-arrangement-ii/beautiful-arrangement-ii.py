class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/1154742/JS-Python-Java-C%2B%2B-or-Simple-Mathematical-Solution-w-Explanation
        ans, a, z = [0] * n, 1, k + 1
        for i in range(k + 1):
            if i % 2:
                ans[i] = z
                z -= 1
            else:
                ans[i] = a
                a += 1
        for i in range(k + 1, n):
            ans[i] = i + 1
        return ans

#======== <Solution 2> ========#
        # Reference: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106965/Python-Straightforward-with-Explanation
        ans = list(range(1, n - k))
        for i in range(k + 1):
            if not i % 2:
                ans.append(n - k + i // 2)
            else:
                ans.append(n - i // 2)
        return ans

#======== <Solution 3> ========#
        import collections
        d = collections.deque(range(1, n + 1))
        tail, ans = False, []
        while len(d) > 0:
            if not tail:
                ans.append(d.popleft())
            else:
                ans.append(d.pop())
            if k > 1:
                tail = not tail
                k -= 1
        return ans

#======== <Solution 4> ========#
        # Reference: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/106955/Short%2Bsimple-with-explanation
        ans = list(range(1, n + 1))
        for i in range(1, k):
            ans[i:] = ans[: i - 1: -1]  # ans[i:][::-1]
        return ans

#======== <Solution 5> ========#
        # Reference: https://leetcode.com/problems/beautiful-arrangement-ii/discuss/1154794/Python-Simple-solution-explained
        ans = list(range(1, n - k + 1))
        sign = 1
        for i in range(k):
            ans.append(ans[-1] + sign * k)
            sign *= -1
            k -= 1
        return ans
