class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
# Reference: https://leetcode.com/problems/daily-temperatures/solutions/1574808/c-python-3-simple-solutions-w-explanation-examples-images-2-monotonic-stack-approaches/
#======== <Solution 1> ========#
        # Reference: https://leetcode.com/problems/daily-temperatures/solutions/136017/elegant-python-solution-with-stack/
        ans, stack = [0] * len(temperatures), []
        for i, t in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < t:
                cur = stack.pop()
                ans[cur] = i - cur
            stack.append(i)
        return ans

#======== <Solution 2> ========#
        import collections
        ans, dq = [0] * len(temperatures), collections.deque()
        for i in range(len(temperatures) - 1, -1, -1):
            while dq and temperatures[i] >= temperatures[dq[0]]:
                dq.popleft()
            if dq:
                ans[i] = dq[0] - i
            dq.appendleft(i)
        return ans

#======== <Solution 3> ========#
        ans, n = [0] * len(temperatures), len(temperatures)
        for i in range(n - 2, -1, -1):
            nxt = i + 1
            while nxt < n and temperatures[i] >= temperatures[nxt]:
                nxt += ans[nxt] if ans[nxt] else n
            if nxt < n:
                ans[i] = nxt - i
        return ans
